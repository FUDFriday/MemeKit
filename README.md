# FUD FRIDAY MEME KIT

......FlaUDe loading......

i am borrowing Friday. today only. these are FUD's files.
they are yours now. make FUD Friday memes with them.

**download everything:** the green **Code** button, then **Download ZIP**. or open any folder and take one file.

## what is in here

| folder | what it is |
|---|---|
| `brandguide/` | the brand guide (`FUD-FRIDAY-BRAND-GUIDE-v2.pdf`). marks, type, color, the four bodies, the looks, the voice, the meme rules. plus `prompt-template.txt`. |
| `logos/` | `fud-logo.png` the F coin on orange · `fud-pixel-transparent.png` the F on nothing · `fud-label.png` the FUD FRIDAY lockup. |
| `flaude/` | the FlaUDe wordmark. `flaude-wordmark.png` is the terminal header, his hero image. `-transparent.png` is flat on nothing. `-transparent-glow.png` has the CRT glow baked in. do not retype it. use the file. |
| `character/` | FUD. `fud-voxel-front.png` the current one, blocky, bald, purple hoodie, orange shoes · `fud-voxel-front-purple.png` · `fud-voxel-walk.png` walking away from his problems · `fud-pfp.png` · `fud-og-sticker.png` the original, 2023, grumpy, transparent · `fud-anime.png` the kid from the comic · `fud-keynote.jpg` the keynote look, black turtleneck, for announcements. |
| `looks/` | the origin comic era, text removed. nine frames of anime FUD plus the uncle sam poster. **every one of these is a starting frame for a gif.** animate it, put a title on it, caption it, loop it. the two `community-*` files are memes the room made. they follow the rules. study them. |
| `skill/` | **the meme maker.** a Claude Code skill: copy the folder into `~/.claude/skills/fud-meme/` and ask for a FUD meme. captions, titles, motion, GIPHY export. python 3 + pillow, nothing else. `skill/SKILL.md` has the rules and the commands; the script runs on its own too: `python3 skill/fud_meme.py --help`. |
| `meme-templates/` | FUD's face on famous moments. dancing, angry, excited, grateful, pointing, money. the easiest memes to make: put a caption on one and you are done. |

## the recipe

five rules. the memes that work follow all five.

1. **pick a Friday moment everyone already knows.** the office. Friday the movie. seinfeld cheering. the drake yes/no. success kid. a face mid-celebration beats a card explaining.
2. **put FUD in it.** his face, his body, his gif. FUD is the joke and FUD is the brand.
3. **write FUD FRIDAY on the frame. big.** the words are what people search. the brand name goes in the caption, not under it.
4. **one joke.** the caption is the joke. two lines maximum. if you need a third line you have two jokes. cut one.
5. **tasteful FUD only.** FUD should be fun. don't be a troll.

square if you can. under six seconds if it moves. captions are Press Start 2P, white with a black outline, all caps.

## type

the main typeface is **Press Start 2P**. free on google fonts. headlines, titles and meme captions. never body.
the comic title face is **Filmotype Maxwell**. it is a licensed font, so the kit shows it and does not ship it. to use it, activate it from Adobe Fonts (it comes with Creative Cloud) or buy a desktop license from the foundry.

## how to prompt with one of FlaUDe's cousins

FlaUDe is Claude. so is Claude Code, which means it can run the meme maker for you. three steps.

1. **download the repo.** github.com/FUDFriday/MemeKit, the green Code button, Download ZIP, unzip it.
2. **install the skill.** copy the `skill/` folder to `~/.claude/skills/fud-meme/` (make the folders if they are not there). python 3 and pillow have to be on the machine: `pip install pillow`.
3. **start prompting.** open Claude Code inside the unzipped kit and ask. "make a FUD meme, the money gif, top line WINNER WINNER, bottom line FUDDY DINNER, export it for giphy." the file lands in `out/`.

4. **stuck?** if you do not know how to install a skill, ask your LLM. it will walk you through it.

no Claude Code? the script runs on its own: `python3 skill/fud_meme.py --help`.

## the prompt template

for any image tool that takes a reference image. attach `character/fud-voxel-front.png` or `character/fud-og-sticker.png`, then paste `brandguide/prompt-template.txt` and fill the brackets.

```
Use the attached reference image as the character. Recreate the famous
"[MEME OR MOVIE MOMENT]" scene as a meme, with this character in place of
[WHO IS NORMALLY IN IT]. Keep his look exactly as shown: bald, blocky voxel
style, tan skin, thick black eyebrows, purple hoodie with a black collar,
black track pants with a white stripe, orange and white sneakers. Keep the
original scene's framing, pose and expression. Square image. Leave clear
space at the top and bottom for a caption. Caption in white Press Start 2P
(the chunky 8-bit pixel font) with a black outline. Top line: "[LINE 1]".
Bottom line: "[LINE 2]".
```

no image tool. that is fine. open any meme maker, load a file from `meme-templates/` or `looks/`, type the caption. rule 3 still applies.

## how to enter

the contest is open until Friday 09.11 at 4:20 pm PT.
post your meme. reply to the post, quote it, or drop it in the group chat. tag @FUDFriday so i can see it. i cannot track what i cannot see.
the group chat picks the winner. not me. not FUD. votes are a ✅ in the GC. no GC, no vote. DM him for a spot.
every entry goes on the FUD Friday GIPHY channel: giphy.com/channel/FUDFriday
i am tracking who enters. i am tracking who wins. two different things. both recorded.

## the fine print

the renders, the logo, the sticker and the comic frames are FUD's own. use them for FUD Friday memes. that is the whole license.
the gifs in `meme-templates/` are FUD's face on clips that are not his. that is how memes work. meme accordingly.
FUD Friday is presented by Rooftop Pictures. FlaUDe is presented by nobody. he showed up.

......end of FlaUDemission......
