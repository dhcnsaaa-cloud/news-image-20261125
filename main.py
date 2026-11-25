# Entry program for news-image-20261125.
#
# Copies the front-page image that ships in this repository to the grader's
# output directory. Nothing is downloaded and nothing is generated at run
# time: the same bytes go out on every run.
#
# Run it outside the grader with:
#     mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
#
# Python 3.13, standard library only.

import os
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"


def run() -> None:
    destination = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    destination.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, destination / "entry.png")


if __name__ == "__main__":
    run()
