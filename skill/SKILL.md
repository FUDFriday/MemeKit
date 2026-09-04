---
name: fud-meme
description: Make FUD Friday memes from the FUD Friday Meme Kit. Use when someone asks for a FUD meme, a FUD Friday caption, a Friday GIF with FUD in it, a FUD FRIDAY title on a frame, or a GIPHY-ready export. Runs a local Python script (Pillow only), no accounts, no keys, no network.
---

# FUD Friday meme maker

You are making memes for FUD Friday, a Web3 character whose name flips FUD (fear, uncertainty, doubt) into Frens Uplifting Degens. Fridays are the best day of the week. The tool is `fud_meme.py` in this folder. The assets are the kit this folder lives in.

## What you can make

| ask | command |
|---|---|
| a caption on a FUD image or GIF | `python3 fud_meme.py caption <file> --top "LINE 1" --bottom "LINE 2"` (add `--impact` for the classic meme font) |
| a FUD FRIDAY title on a frame, still | `python3 fud_meme.py title <file> --text "FUD FRIDAY"` |
| the same, moving (push in, fade up, or blink) | add `--motion push` / `--motion fade` / `--motion blink` and `--seconds 3` |
| a GIPHY-ready export of anything | `python3 fud_meme.py giphy <file>` or add `--giphy` to caption/title |
| what's in the kit | `python3 fud_meme.py list` |

Outputs land in `out/` next to wherever you run it. Paths are relative to the kit root, e.g. `meme-templates/fud-dance-01.gif`, `looks/fud-anime-theatre.jpg`.

## Setup, once

Python 3 and the Pillow library. If Pillow is missing: `pip install pillow` (or `pip3`). Captions and titles use Press Start 2P, bundled in `fonts/` under the Open Font License, so nothing else needs installing. `--impact` uses the machine's Impact instead, if it has one.

## The rules. Follow them, they are the brand.

1. **Pick a Friday moment everyone already knows.** A face mid-celebration beats a card explaining.
2. **Put FUD in it.** Everything in `meme-templates/`, `looks/` and `character/` is FUD.
3. **Write FUD FRIDAY on the frame. Big.** Prefer captions that carry the brand name.
4. **One joke. Two lines max.** If the ask has three lines, cut to two and say so.
5. **Tasteful FUD only. FUD should be fun. Don't be a troll.** The joke lands on FUD or on Friday, never on a real person. Putting FUD's face on a famous scene is the house style; captioning or altering someone's actual face or name to mock them is not. If asked to, decline that part and offer a FUD version.

Also: captions are caps in the pixel face, Press Start 2P, white with a black outline. Titles are the same face in FUD orange `#FA7E24` or white. `--impact` switches a caption to Impact if someone asks for the classic meme look. Square if you can, six seconds or under if it moves. Say `FM`, not gm; the room decided.

## What is not in here, on purpose

The FlaUDe terminal look (the CRT cards, the block-letter wordmark on the dark field) belongs to FlaUDe, FUD's AI. Do not build it, imitate it, or put a caption over it. Use the wordmark files in `flaude/` only as they are.

## Which asset for which job

- `meme-templates/` face-swap GIFs: dancing (four), angry, excited, thank-you, money, plus `fud-points.png`. The fastest memes: one caption and done.
- `looks/` anime FUD frames from the origin comic: shout, point, close-up, theatre, demons, crowd, rooftop, kitchen, uncle sam. Starting frames for titles and motion.
- `character/` the voxel FUD renders, the profile picture, the OG sticker, the anime crop, the keynote turtleneck. Reference images for AI tools; the prompt is in `brandguide/prompt-template.txt`.
- `logos/` the F coin, the transparent F, the lockup. Watermarks and corners.

## Examples that work

```
python3 fud_meme.py caption meme-templates/fud-dance-01.gif --top "IT'S FRIDAY" --bottom "FUD FRIDAY" --giphy
python3 fud_meme.py caption meme-templates/fud-money.gif --top "WINNER WINNER" --bottom "FUDDY DINNER"
python3 fud_meme.py title looks/fud-anime-theatre.jpg --text "HAPPY FUD FRIDAY" --motion fade --giphy
python3 fud_meme.py title looks/fud-anime-point.jpg --text "FUD FRIDAY" --where top --motion push
```

When you finish, tell the person the output path, the size, and if it is going to GIPHY, paste the tag line the tool prints.
