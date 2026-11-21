#!/usr/bin/env python3
"""Make portrait phone versions of every background.

    uv run --with numpy --with pillow python make_mobile.py                 # every theme
    uv run --with numpy --with pillow python make_mobile.py --only umbra    # just these

Each backgrounds/<theme>/<name>.png becomes backgrounds/<theme>/mobile/<name>.png
at 1080x2400 (9:20). The desktop images are landscape, so the full height is kept
and a 9:20 window is cut out of the width. The window is centred on the picture's
brightest feature (the mark, the lamp, the moon) rather than the middle, so the
subject survives the crop; it is clamped so it never leaves the image.
"""
import argparse
import sys
from multiprocessing import Pool
from pathlib import Path

import numpy as np
from PIL import Image

HERE = Path(__file__).resolve().parent
BACKGROUNDS = HERE / "backgrounds"
OUT_NAME = "mobile"
SIZE = (1080, 2400)
ASPECT = SIZE[0] / SIZE[1]
EXTENSIONS = (".png", ".jpg", ".jpeg", ".webp")

Image.MAX_IMAGE_PIXELS = None

# Where the brightest-feature guess picks the wrong subject, name the focal point
# yourself: "<theme>/<file>" -> horizontal centre as a 0..1 fraction of the width.
FOCUS = {
    "umbra/03-diamond-ring.png": 2226 / 3840,  # the whole eclipse, not just the bright bead on its rim
}


def focal_x(img):
    """Horizontal centre of the brightest area, as a 0..1 fraction of the width."""
    small = img.convert("L").resize((max(1, img.width // 16), max(1, img.height // 16)), Image.BILINEAR)
    a = np.asarray(small, np.float32)
    thr = np.percentile(a, 99.6)
    w = np.clip(a - thr, 0, None)
    if w.sum() < 1e-3:  # flat image: use the middle
        return 0.5
    cols = w.sum(axis=0)
    return float((cols * np.arange(a.shape[1])).sum() / cols.sum() + 0.5) / a.shape[1]


def convert(job):
    src, dst = job
    img = Image.open(src).convert("RGB")
    cw = round(img.height * ASPECT)
    fx = FOCUS.get(f"{src.parent.name}/{src.name}")
    x = round((focal_x(img) if fx is None else fx) * img.width - cw / 2)
    x = max(0, min(img.width - cw, x))
    out = img.crop((x, 0, x + cw, img.height)).resize(SIZE, Image.LANCZOS)
    dst.parent.mkdir(parents=True, exist_ok=True)
    out.save(dst, optimize=True)
    return f"{src.parent.name}/{src.name}  crop x={x}..{x + cw} of {img.width}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*", help="theme folders to process (default: all)")
    args = ap.parse_args()
    themes = sorted(p for p in BACKGROUNDS.iterdir() if p.is_dir() and (not args.only or p.name in args.only))
    jobs = [(f, f.parent / OUT_NAME / f.name)
            for t in themes for f in sorted(t.iterdir())
            if f.is_file() and f.suffix.lower() in EXTENSIONS]
    if not jobs:
        sys.exit("no backgrounds found")
    with Pool() as pool:
        for line in pool.imap(convert, jobs):
            print(line, flush=True)
    print(f"{len(jobs)} mobile backgrounds in {len(themes)} themes")


if __name__ == "__main__":
    main()
