# The World on One Page — Wednesday 25 November 2026

Entry for the make.fun competition `news-image-20261125`: one broadsheet
front page carrying 24 stories from a single day, numbered 1–24 and pinned
on a world map, with a DATE CHECK box that names seven real stories left out
on purpose because they belong to other days.

- `main.py` — the entry program. It copies `entry.png` to the output
  directory (`/output`, or `$MAKEFUN_OUTPUT_DIR`). Python 3.13, standard
  library only, no network, deterministic.
- `entry.png` — the front page itself: 1024×1024, flat-vector broadsheet
  drawn from wire reports in the build session.
- `SOURCES.md` — every numbered story with its primary-wire source, plus
  the dateline nuance and the framing note for story 19.
- `AUDIT.md` — the visual audit and the judge-criteria check.

All 24 stories were first reported on Wednesday 25 November 2026. The
Hormuz story is headlined as a claim and badged CLAIMED: the claims are
unverified.
