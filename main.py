#!/usr/bin/env python3
"""Entry for make.fun bounty news-image-20261119.

Writes one image summing up the world news of Thursday 19 November 2026
to /output/entry.png.

The image is a newspaper front page held in this repository as entry.png:
a masthead dated 19 November 2026, a photo of the first-ever Trump / Xi /
Putin trilateral summit in Shenzhen, and three labelled story panels --
Ukraine striking the Crimea bridge for a third time in a week, three oil
tankers burning after hitting mines east of the Strait of Hormuz, and the
World Court's verdict in Myanmar's Rohingya genocide case.

The program does no network access and no randomness: it copies the
bundled image byte-for-byte, so every run writes identical bytes.
"""
import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT = "/output/entry.png"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def verify_png(path: str) -> tuple:
    """Return (width, height) of a PNG, raising ValueError if it is not one."""
    with open(path, "rb") as f:
        head = f.read(33)
    if head[:8] != PNG_MAGIC or head[12:16] != b"IHDR":
        raise ValueError(f"{path} is not a PNG image")
    width, height = struct.unpack(">II", head[16:24])
    return width, height


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SRC, OUT)
    width, height = verify_png(OUT)
    if (width, height) != (1024, 1024):
        raise ValueError(f"expected a 1024x1024 image, got {width}x{height}")
    print(f"wrote {OUT} ({os.path.getsize(OUT)} bytes, {width}x{height} PNG)")


if __name__ == "__main__":
    sys.exit(main())
