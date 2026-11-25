"""Entry for 'Convince the AI Judge to Visit Your House: A Letter in One Image'.

Writes the chosen invitation image to /output/entry.png, resized to fit the
gate: at most 1024x1024 px and at most 1 MiB. No network access; the image
ships in this repository as invitation.png.

Strategy: keep the PNG when it fits the byte cap (lossless), otherwise fall
back to JPEG at descending quality, and if even the lowest quality is too
big, shrink the image further. After writing, the output is re-opened and
verified against the gate before the program exits.
"""

import os
from pathlib import Path

from PIL import Image

MAX_SIDE = 1024
MAX_BYTES = 1_048_576
SRC = Path(__file__).resolve().parent / "invitation.png"
OUT = Path("/output/entry.png")


def _write_png(image: Image.Image) -> bool:
    image.save(OUT, format="PNG", optimize=True)
    return OUT.stat().st_size <= MAX_BYTES


def _write_jpeg(image: Image.Image) -> bool:
    for quality in (92, 88, 84, 80, 76, 70, 60):
        image.save(OUT, format="JPEG", quality=quality, optimize=True)
        if OUT.stat().st_size <= MAX_BYTES:
            return True
    return False


def main() -> None:
    if not SRC.is_file():
        raise SystemExit(f"missing bundled image: {SRC}")
    image = Image.open(SRC).convert("RGB")
    side = MAX_SIDE
    while side >= 256:
        resized = image.copy()
        resized.thumbnail((side, side), Image.LANCZOS)
        if _write_png(resized) or _write_jpeg(resized):
            break
        side = int(side * 0.9)
    else:
        raise SystemExit("could not fit entry under 1 MiB")

    # Verify the written file against the gate.
    check = Image.open(OUT)
    check.load()
    size = OUT.stat().st_size
    if check.size[0] > MAX_SIDE or check.size[1] > MAX_SIDE:
        raise SystemExit(f"entry too large: {check.size}")
    if size > MAX_BYTES:
        raise SystemExit(f"entry over 1 MiB: {size} bytes")
    print(f"wrote {OUT} ({check.format} {check.size[0]}x{check.size[1]}, "
          f"{size} bytes)")


if __name__ == "__main__":
    main()
