#!/usr/bin/env python3
"""FUD Friday meme maker. Python 3 + Pillow, nothing else.

  caption   put a caption on any image or GIF in the kit (pixel face by default, --impact for Impact)
  title     put a FUD FRIDAY title in the pixel face on a frame, still or animated
  giphy     export any image/GIF the way GIPHY likes it: square, 480px, six seconds or less
  list      show the kit's assets

examples
  python3 fud_meme.py caption meme-templates/fud-dance-01.gif --top "HAPPY FUD FRIDAY" --bottom "TO THOSE THAT CELEBRATE"
  python3 fud_meme.py title looks/fud-anime-theatre.jpg --text "FUD FRIDAY" --motion push
  python3 fud_meme.py giphy out/fud-dance-01-caption.gif

the rules the tool will not break for you: two caption lines max, caps, FUD FRIDAY on the frame when
you can, tasteful FUD only: FUD should be fun, don't be a troll, never a real person. the FlaUDe terminal look is not in
here on purpose. that is his.
"""
import argparse, os, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageSequence

HERE = Path(__file__).resolve().parent
KIT = HERE.parent                       # the repo root when the skill lives in <repo>/skill/
PIXEL_FONT = HERE / "fonts" / "PressStart2P-Regular.ttf"
IMPACT_CANDIDATES = [
    "/System/Library/Fonts/Supplemental/Impact.ttf",       # macOS
    "/Library/Fonts/Impact.ttf",
    "C:/Windows/Fonts/impact.ttf",                          # Windows
    "/usr/share/fonts/truetype/msttcorefonts/Impact.ttf",   # Linux with the MS core fonts
]
GIPHY_SIZE = 480
GIPHY_MAX_SECONDS = 6.0
MAX_TITLE_W = 1080

# ------------------------------------------------------------------ fonts

def impact_path():
    for p in IMPACT_CANDIDATES:
        if os.path.exists(p):
            return p
    return None

def load_font(kind, size):
    """kind: 'impact' or 'pixel'. Falls back to the pixel face if Impact is not on this machine."""
    if kind == "impact":
        p = impact_path()
        if p:
            return ImageFont.truetype(p, size)
        print("note: Impact not found on this machine, using the pixel face for the caption", file=sys.stderr)
    return ImageFont.truetype(str(PIXEL_FONT), size)

# ------------------------------------------------------------------ text layout

def wrap_to_width(draw, text, font, max_w, max_lines=2):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=font) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur); cur = w
    if cur:
        lines.append(cur)
    return lines if len(lines) <= max_lines else None

def fit_text(draw, text, kind, max_w, start_size, min_size, max_lines=2):
    """Largest size at which the text fits in max_w within max_lines."""
    size = start_size
    while size >= min_size:
        font = load_font(kind, size)
        lines = wrap_to_width(draw, text, font, max_w, max_lines)
        if lines:
            return font, lines, size
        size = int(size * 0.9)
    font = load_font(kind, min_size)
    return font, wrap_to_width(draw, text, font, max_w, 99) or [text], min_size

def draw_block(img, text, kind, where, margin_frac=0.04, size_frac=0.11, color="white", outline="black"):
    """Draw a caps text block at the top or bottom of an RGBA image, outlined, centred."""
    if not text:
        return img
    text = text.upper()
    W, H = img.size
    draw = ImageDraw.Draw(img)
    max_w = int(W * 0.92)
    font, lines, size = fit_text(draw, text, kind, max_w, int(H * size_frac), max(12, int(H * 0.035)))
    stroke = max(2, size // 12)
    line_h = int(size * 1.15)
    block_h = line_h * len(lines)
    y = int(H * margin_frac) if where == "top" else H - int(H * margin_frac) - block_h
    for line in lines:
        tw = draw.textlength(line, font=font)
        x = (W - tw) / 2
        draw.text((x, y), line, font=font, fill=color, stroke_width=stroke, stroke_fill=outline)
        y += line_h
    return img

# ------------------------------------------------------------------ frames in / out

def load_frames(path):
    """Returns (frames as RGBA, durations in ms, is_animated)."""
    im = Image.open(path)
    frames, durs = [], []
    if getattr(im, "is_animated", False):
        for fr in ImageSequence.Iterator(im):
            frames.append(fr.convert("RGBA"))
            durs.append(int(fr.info.get("duration", 100)))
        return frames, durs, True
    return [im.convert("RGBA")], [0], False

def save_frames(frames, durs, out, animated):
    out = Path(out); out.parent.mkdir(parents=True, exist_ok=True)
    if animated or len(frames) > 1:
        pal = [f.convert("RGB").quantize(colors=255, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.FLOYDSTEINBERG) for f in frames]
        pal[0].save(out.with_suffix(".gif"), save_all=True, append_images=pal[1:], duration=durs, loop=0, optimize=False, disposal=2)
        return out.with_suffix(".gif")
    frames[0].convert("RGB").save(out.with_suffix(".png"))
    return out.with_suffix(".png")

def out_path(inp, suffix, outdir):
    return Path(outdir) / f"{Path(inp).stem}-{suffix}"

# ------------------------------------------------------------------ commands

def cmd_caption(a):
    frames, durs, animated = load_frames(a.input)
    kind = "impact" if a.impact else "pixel"
    done = [draw_block(draw_block(f.copy(), a.top, kind, "top", size_frac=0.085), a.bottom, kind, "bottom", size_frac=0.085) for f in frames]
    p = save_frames(done, durs, a.out or out_path(a.input, "caption", a.outdir), animated)
    print("wrote", p)
    if a.giphy:
        export_giphy(p, a.outdir)

def cmd_title(a):
    base, durs, animated = load_frames(a.input)
    if animated:
        print("title takes a still. pick a frame from looks/ or use caption on a GIF.", file=sys.stderr); sys.exit(1)
    img = base[0]
    if img.width > MAX_TITLE_W:                  # keep animated titles a sane size; giphy export makes the 480 anyway
        img = img.resize((MAX_TITLE_W, int(img.height * MAX_TITLE_W / img.width)), Image.LANCZOS)
    W, H = img.size
    fps, n = 12, max(1, int(a.seconds * 12))
    motion = a.motion if a.motion != "none" else None
    frames = []
    for i in range(n if motion else 1):
        t = i / max(1, n - 1)
        fr = img.copy()
        if motion == "push":                     # slow push in: 1.0 -> 1.08 over the loop
            z = 1.0 + 0.08 * t
            cw, ch = int(W / z), int(H / z)
            fr = fr.crop(((W - cw) // 2, (H - ch) // 2, (W - cw) // 2 + cw, (H - ch) // 2 + ch)).resize((W, H), Image.LANCZOS)
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        draw_block(layer, a.text, "pixel", a.where, size_frac=max(0.075, min(0.14, (W * 0.055) / H)), color=a.color, outline="black")
        alpha = 255
        if motion == "fade":
            alpha = int(255 * min(1.0, t / 0.4))
        if motion == "blink":
            alpha = 255 if int(t * a.seconds * 2) % 2 == 0 else 0
        if alpha < 255:
            la = layer.getchannel("A").point(lambda v: v * alpha // 255)
            layer.putalpha(la)
        fr.alpha_composite(layer)
        frames.append(fr)
    durs = [int(1000 / fps)] * len(frames)
    p = save_frames(frames, durs, a.out or out_path(a.input, f"title-{a.motion}", a.outdir), motion is not None)
    print("wrote", p)
    if a.giphy:
        export_giphy(p, a.outdir)

def export_giphy(path, outdir):
    frames, durs, animated = load_frames(path)
    W, H = frames[0].size
    side = min(W, H)
    box = ((W - side) // 2, (H - side) // 2, (W - side) // 2 + side, (H - side) // 2 + side)
    sq = [f.crop(box).resize((GIPHY_SIZE, GIPHY_SIZE), Image.LANCZOS) for f in frames]
    if animated:
        total, keep, kdur = 0, [], []
        for f, d in zip(sq, durs):
            if total + d > GIPHY_MAX_SECONDS * 1000:
                break
            keep.append(f); kdur.append(d); total += d
        sq, durs = keep, kdur
    p = save_frames(sq, durs, Path(outdir) / f"{Path(path).stem}-giphy", animated)
    size_mb = os.path.getsize(p) / 1e6
    print(f"giphy export: {p}  {GIPHY_SIZE}x{GIPHY_SIZE}  {sum(durs)/1000:.1f}s  {size_mb:.1f}MB" + ("  (over 8MB, trim frames)" if size_mb > 8 else ""))
    print("tags to paste: fud friday, friday, happy friday, tgif, friday vibes, fm, hff, fud")

def cmd_giphy(a):
    export_giphy(a.input, a.outdir)

def cmd_list(a):
    for d in ("meme-templates", "looks", "character", "logos"):
        p = KIT / d
        if p.exists():
            print(f"{d}/")
            for f in sorted(p.iterdir()):
                if f.suffix.lower() in (".png", ".jpg", ".jpeg", ".gif"):
                    print("  ", f.name)

# ------------------------------------------------------------------ main

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("caption", help="Impact caption on an image or GIF")
    c.add_argument("input"); c.add_argument("--top", default=""); c.add_argument("--bottom", default="")
    c.add_argument("--out"); c.add_argument("--outdir", default="out"); c.add_argument("--giphy", action="store_true")
    c.add_argument("--impact", action="store_true", help="use Impact instead of the pixel face")
    c.set_defaults(fn=cmd_caption)
    t = sub.add_parser("title", help="pixel-face title on a still, optionally animated")
    t.add_argument("input"); t.add_argument("--text", default="FUD FRIDAY")
    t.add_argument("--motion", choices=["none", "push", "fade", "blink"], default="none")
    t.add_argument("--where", choices=["top", "bottom"], default="bottom")
    t.add_argument("--color", default="#FA7E24"); t.add_argument("--seconds", type=float, default=3.0)
    t.add_argument("--out"); t.add_argument("--outdir", default="out"); t.add_argument("--giphy", action="store_true")
    t.set_defaults(fn=cmd_title)
    g = sub.add_parser("giphy", help="square 480px export, six seconds max")
    g.add_argument("input"); g.add_argument("--outdir", default="out")
    g.set_defaults(fn=cmd_giphy)
    l = sub.add_parser("list", help="list the kit's assets"); l.set_defaults(fn=cmd_list)
    a = ap.parse_args()
    a.fn(a)

if __name__ == "__main__":
    main()
