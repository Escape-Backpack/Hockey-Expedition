# Hockey Road Trip: identity (concept v2)

Concept only. Style direction comes from the Codex concept board
(`Hockey-Expedition/assets/identity/hockey-road-trip-concept-board-v1.png`); this folder
redraws the badge as editable SVGs with three fixes: smaller lettering and a larger road/puck,
a keyline between puck and road so they don't merge in one colour, and an icon-only version.

| File | Use |
|---|---|
| `badge.svg` / `.png` | Full-colour badge (600 x 680) |
| `badge-one-colour.svg` / `.png` | One-colour badge for stamps, stickers, engraving |
| `icon.svg` / `.png` | Icon without text (512 x 512), for avatars and small stickers |
| `make_svgs.py` | Regenerates the SVGs. PNGs are rendered with headless Chrome. |

Palette: Midnight `#142B40`, Rink Red `#D6493E`, Ice Blue `#B9DEE8`, Ticket Cream `#F5EBDD`, Puck Black `#20252A`.
Type: Barlow Condensed (headings), Barlow (body), IBM Plex Mono (numerals).

The SVG text uses a font stack (Barlow Condensed, Oswald, Impact). Install Barlow Condensed
or convert the text to outlines before print.
