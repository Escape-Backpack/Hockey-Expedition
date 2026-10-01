---
id: AS-002
title: Small badge v1
type: asset
# idea | candidate | decided | built | parked
status: candidate
# image | audio | text | print
kind: image
# The prop this asset is for (one ID)
for:
# Generator or tool used
tool: Codex image generation, then redrawn as SVG
# Path from the project folder once made, e.g. assets/star-chart.png
file: assets/identity/badge.svg
# Any related record IDs, e.g. [PZ-002, Q-004]
links: [PR-004, AS-001]
# Set to an ID when this record is replaced. It then moves to the Parked tab.
superseded_by:
tags: []
---

Badge for Hockey Road Trip. The Codex PNG (`assets/identity/hockey-road-trip-small-badge-v1.png`) is the first version.
The SVG redraw (concept v2, 2026-10-01) is the working master: `badge.svg`, `badge-one-colour.svg` and an icon-only `icon.svg`. See `assets/identity/README.md`.

Changes from v1: smaller lettering with a larger road and puck, a keyline between puck and road so they stay separate in one colour, and an icon without text.

Open: text is live type with a font fallback, so convert to outlines or install Barlow Condensed before print.
