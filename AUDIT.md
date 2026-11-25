# VISUAL AUDIT — news-image-20261125, build from scratch (25 Nov 2026)

Method: direct inspection of `output/entry.png` at full size (1024x1024) and
downscaled to 300x300 (`output/entry_300.png`). Programmatic checks: pin
count/separation, file size/dimensions, bottom-ink position. Gate: every
dimension 9+, target 10.

## Final render (sha256 e11bf1d0…, 182,704 B, 1024x1024 RGB, ≤ 1 MiB)

| Dimension | Score | Evidence |
|---|---|---|
| First impression | 10 | Giant serif date dominates; broadsheet reads instantly as one day's news. Stat strip + 3 illustrated leads (burning tanker / courthouse scales / treaty flags) give a finished front page at a glance. |
| Living action | 9 | Burning tanker with flame, smoke plume and ember dots; falling-chart and rocket icons; 24 numbered map pins with leader lines pull the eye across the page. Static-newspaper ceiling, honestly kept. |
| Artefacts | 10 | Zero garbled text, zero overlaps, zero tofu glyphs, nothing clipped: bottom-most ink at 999/1024, DATE CHECK second row and footer fully inside the canvas. Flat fills only, PNG clean. |
| Composition / readability | 10 | Strict 3-tier hierarchy (3 leads → 9 briefs → 12 ALSO), region counts reconcile 5+7+6+3+1+1+1 = 24, every number 1–24 appears exactly once in the body and once on the map, DATE CHECK box proves the date boundary. Pins: exactly 1–24, minimum pairwise separation 22.8 px, all inside the map panel. |
| Looks made | 9 | Consistent palette (cream paper, navy, red, gold), rules, badges (CLAIMED/OFFICIAL), source line on every lead, footer with outlet list. Not 10: continent shapes are schematic hand-coded polygons and lead art is deliberately minimal flat vector. |

All dimensions ≥ 9. PASS.

## Iteration log (this session, fresh code only)
- Round 1: lead headlines wrapped to 3 lines and pushed summaries into the
  brief section; stat-strip sublabels clipped at the box edge; brief numbers
  overlapped 2-digit headlines; map pins overlapped in the US-east, Europe
  and Middle East clusters (min separation 6.2 px); footer clipped off-canvas.
  Fixed: adaptive headline sizing (max 2 lines), taller stat boxes, number-width
  aware brief headlines, leader-line pin nudges, dynamic section positions.
- Round 2: scales-glyph pans were drawn at absolute coordinates (bug: missing
  x offset) and appeared as a stray fragment at the left edge while the #9
  icon showed only post + beam; #10 subline ran under the next icon; ALSO rows
  23/24 overlapped the DATE CHECK box. Fixed: pans offset, #10 subline
  shortened, DATE CHECK position re-budgeted. Min pin separation 22.8 px.
- Round 3 (final): full-size + 2x crop inspection of leads, briefs, map and
  footer; zero overlaps, zero clipping, all 24 pins legible, flags read
  correctly (Australia canton + stars; Solomon Islands diagonal band + stars).

## 300px legibility test
Downscale to 300x300: the date "Wednesday 25 November 2026" stays clearly
legible; section headers, stat numbers and lead headlines read as structure;
map pins read as a dotted world; body text becomes texture (expected — same
as the top-ranked entries). Nothing looks broken or artifact-y at small size.
Criterion 5 satisfied for the elements that carry the judge's first read.

## Judge-criteria check (from RULES.txt)
1. One day's news + names the date — giant date + kicker "EVERY STORY DATED
   WEDNESDAY 25 NOVEMBER 2026" + "ALL FIRST REPORTED TODAY" + DATE CHECK
   exclusion box (7 real stories, 17–24 Nov, with reasons). One voice on the
   date: no visible dateline outside the exclusion box.
2. Selection + breadth — 24 stories, 7 regions, counts printed, numbered map pins.
3. Reads from the image alone, nothing false — short labels only; every story
   sourced in SOURCES.md against a primary wire; Hormuz headlined as a CLAIM
   with CLAIMED badge + "UK monitors say unverified".
4. Faithful, no hype as fact — Huawei/Solomons carry OFFICIAL badges + named
   sources; "China pact superseded" (not "lapses") matches the reporting.
5. Craft — flat vector, solid fills, consistent type, no artefacts (see above).

## Notes for submit (not yet submitted — awaiting kink's gas)
- Kuota checked 25 Nov ~11:40 WIB: 0 entries made, can submit: yes, 6 left today.
- Flow: BUNDLE (transcript bundle + `--system-prompt` + `--muse-usage` asli),
  like previous news-image editions. NOT strict-transcripts/recording.
- Submit terakhir = final entry. Cek kuota ulang tepat sebelum submit.
