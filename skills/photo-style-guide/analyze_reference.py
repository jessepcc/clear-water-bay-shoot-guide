#!/usr/bin/env python3
"""Measure the tone and colour of a reference photo, optionally against your own test shot.

Usage:
  python3 analyze_reference.py REFERENCE.jpg [TEST.jpg] [--crop x0,y0,x1,y1]

--crop takes fractions of width/height (e.g. 0,0,1,0.9 drops the bottom 10%) so
watermarks, captions and borders do not skew the numbers. Requires Pillow.

The numbers describe the *published file* (often a re-encoded web preview), not the
photographer's raw capture or settings. Use them to compare, not to claim a recipe.
"""
import math
import sys

from PIL import Image, ImageOps

BANDS = (("shadows", 0, 25), ("midtones", 25, 75), ("highlights", 75, 101))
HUES = (("red/skin", 345, 30), ("orange/skin", 30, 50), ("yellow", 50, 70), ("green", 70, 160),
        ("cyan", 160, 200), ("blue", 200, 260), ("purple/magenta", 260, 345))


def srgb_to_lab(r, g, b):
    def lin(c):
        c /= 255
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = lin(r), lin(g), lin(b)
    x = (0.4124 * r + 0.3576 * g + 0.1805 * b) / 0.95047
    y = 0.2126 * r + 0.7152 * g + 0.0722 * b
    z = (0.0193 * r + 0.1192 * g + 0.9505 * b) / 1.08883
    f = lambda t: t ** (1 / 3) if t > 0.008856 else 7.787 * t + 16 / 116
    fx, fy, fz = f(x), f(y), f(z)
    return 116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz)


def pct(sorted_vals, p):
    return sorted_vals[min(len(sorted_vals) - 1, int(p / 100 * len(sorted_vals)))]


def measure(path, crop):
    img = ImageOps.exif_transpose(Image.open(path)).convert("RGB")
    w, h = img.size
    if crop:
        x0, y0, x1, y1 = crop
        img = img.crop((int(x0 * w), int(y0 * h), int(x1 * w), int(y1 * h)))
    img.thumbnail((400, 400))
    px = list(img.get_flattened_data() if hasattr(img, 'get_flattened_data') else img.getdata())
    lab = [srgb_to_lab(*p) for p in px]
    L = sorted(v[0] for v in lab)
    m = {"file": path, "size": f"{w}x{h}", "pixels": len(px)}
    for p in (0.5, 5, 25, 50, 75, 95, 99.5):
        m[f"L p{p}"] = pct(L, p)
    m["contrast p95-p5"] = m["L p95"] - m["L p5"]
    m["% crushed (L<3)"] = 100 * sum(v < 3 for v in L) / len(L)
    m["% clipped (L>97)"] = 100 * sum(v > 97 for v in L) / len(L)
    for name, lo, hi in BANDS:
        sel = [v for v in lab if lo <= v[0] < hi]
        share = 100 * len(sel) / len(lab)
        a = sum(v[1] for v in sel) / len(sel) if sel else float("nan")
        b = sum(v[2] for v in sel) / len(sel) if sel else float("nan")
        m[f"{name}"] = (share, a, b)
    chroma = [math.hypot(v[1], v[2]) for v in lab if 15 < v[0] < 90]
    chroma.sort()
    m["chroma median"] = pct(chroma, 50) if chroma else 0
    m["chroma p90"] = pct(chroma, 90) if chroma else 0
    hue_counts = {n: 0 for n, _, _ in HUES}
    sat = [v for v in lab if 15 < v[0] < 90 and math.hypot(v[1], v[2]) > 15]
    for v in sat:
        hdeg = math.degrees(math.atan2(v[2], v[1])) % 360
        for n, lo, hi in HUES:
            if (lo <= hdeg < hi) if lo < hi else (hdeg >= lo or hdeg < hi):
                hue_counts[n] += 1
                break
    m["hues"] = {n: 100 * c / max(1, len(sat)) for n, c in hue_counts.items()}
    m["% coloured pixels"] = 100 * len(sat) / len(lab)
    return m


def notes(m):
    out = []
    if m["L p0.5"] > 12:
        out.append(f"Darkest 0.5% only reaches L{m['L p0.5']:.0f}: either faded blacks or nothing dark in frame. "
                   "Re-measure a crop of something that should be black (hair, rock shadow). If it is faded: no in-camera "
                   "setting lifts the black point (Shadows -2 only softens shadow contrast); it needs a curve in post.")
    elif m["% crushed (L<3)"] > 2:
        out.append("Deep, partly crushed blacks: Shadows +1..+2 or a contrasty sim (Classic Chrome, Classic Neg., Velvia).")
    if m["L p99.5"] < 90:
        out.append(f"Highlights top out at L{m['L p99.5']:.0f}: soft/muted whites. Highlights -1..-2 and/or DR200-400, "
                   "possibly exposure -1/3.")
    elif m["% clipped (L>97)"] > 3:
        out.append("Clipped whites are part of the look (bright, airy). Expect +2/3..+1 EV and Highlights 0..+1; "
                   "check that skin is not the part clipping.")
    c = m["contrast p95-p5"]
    out.append(f"Tonal spread p5-p95 = {c:.0f} L units ({'low' if c < 55 else 'high' if c > 80 else 'moderate'} contrast "
               "for a typical outdoor scene; compare against your test shot in the same light, not in isolation).")
    for band in ("shadows", "midtones", "highlights"):
        share, a, b = m[band]
        if share < 3 or math.isnan(a):
            continue
        tint = []
        if b > 6: tint.append("warm/yellow")
        if b < -4: tint.append("cool/blue")
        if a > 5: tint.append("magenta/red")
        if a < -4: tint.append("green")
        if tint:
            out.append(f"{band.capitalize()} lean {' + '.join(tint)} (a*={a:+.1f}, b*={b:+.1f}). Whole-frame means include "
                       "the scene's own colours; for white balance, --crop a neutral (white dress, cloud, grey rock).")
    sh, hl = m["shadows"], m["highlights"]
    if sh[0] >= 3 and hl[0] >= 3 and not math.isnan(sh[2] + hl[2]) and hl[2] - sh[2] > 8:
        out.append("Split tone: highlights warmer than shadows. Characteristic of Classic Neg. / Nostalgic Neg. "
                   "(amber highlights) or of warm light with cool skylight in shadows.")
    out.append(f"Chroma median {m['chroma median']:.0f}, p90 {m['chroma p90']:.0f} "
               "(roughly: <15 muted like Classic Chrome/Eterna, 15-25 natural like Astia/Provia/Pro Neg., >25 vivid like Velvia).")
    return out


def show(m):
    print(f"\n== {m['file']} ({m['size']}, {m['pixels']} sampled px)")
    print("  Lightness L* percentiles: " + "  ".join(f"p{p}={m[f'L p{p}']:.0f}" for p in (0.5, 5, 25, 50, 75, 95, 99.5)))
    print(f"  crushed {m['% crushed (L<3)']:.1f}%  clipped {m['% clipped (L>97)']:.1f}%  contrast(p95-p5) {m['contrast p95-p5']:.0f}")
    for band in ("shadows", "midtones", "highlights"):
        share, a, b = m[band]
        print(f"  {band:<10} {share:5.1f}% of frame  a*={a:+6.1f} (green-/magenta+)  b*={b:+6.1f} (blue-/yellow+)")
    print(f"  chroma median {m['chroma median']:.1f}  p90 {m['chroma p90']:.1f}  coloured px {m['% coloured pixels']:.0f}%")
    print("  hue share of coloured px: " + ", ".join(f"{k} {v:.0f}%" for k, v in m["hues"].items() if v >= 1))
    print("  Observations:")
    for n in notes(m):
        print("   - " + n)


def main(argv):
    crop = None
    if "--crop" in argv:
        i = argv.index("--crop")
        crop = tuple(float(x) for x in argv[i + 1].split(","))
        argv = argv[:i] + argv[i + 2:]
    if not 1 <= len(argv) <= 2:
        sys.exit(__doc__)
    ms = [measure(p, crop) for p in argv]
    for m in ms:
        show(m)
    if len(ms) == 2:
        r, t = ms
        print("\n== Test shot minus reference (move settings to shrink these)")
        for k in ("L p5", "L p50", "L p95", "contrast p95-p5", "chroma median"):
            print(f"  {k:<16} {t[k] - r[k]:+6.1f}")
        for band in ("shadows", "midtones", "highlights"):
            print(f"  {band:<16} a* {t[band][1] - r[band][1]:+5.1f}   b* {t[band][2] - r[band][2]:+5.1f}")
        print("  Compare like with like: same kind of light and a similar crop. Near mid-grey, +1/3 EV raises L p50 by ~5.\n"
              "  b*/a* -> WB shift R/B, contrast -> Highlights/Shadows, chroma -> Color: calibrate the step size on your own\n"
              "  camera (shoot one scene at shift 0 and R+2, Color 0 and +2) instead of trusting fixed conversions.")


if __name__ == "__main__":
    main(sys.argv[1:])
