---
name: photo-style-guide
description: Build the photo-style / reference section of a shoot guide in this repo — find real reference photos with documented social-media or publication popularity, include or link them with credits, measure their tone and colour, and translate that into a specific Fujifilm X-T5 film-simulation recipe with an honest statement of what the camera cannot recreate. Use when creating a new guide (e.g. victoria-night/), adding references or "recipes" to a guide, or when asked how to get "this look" on the Fujifilm.
---

# Photo style guide: real references → Fujifilm recipe

The goal is a reference section a photographer can use on location: real photos people actually engaged with, each with credit and source, a measured description of its look, and an X-T5 recipe with every parameter filled in. Generic advice ("use Classic Chrome for a moody look", "shoot in golden hour") is a failure of this skill. Every claim must be traceable to a link, a measurement, or a stated assumption.

The Clear Water Bay guide is the worked example: `clear-water-bay/research-notes.md` (evidence and exclusions), `clear-water-bay/image-sources.json` (provenance) and the `#reflib` section of `clear-water-bay/index.html` (presentation).

## Honesty rules (non-negotiable)

1. **Popularity needs a dated source.** "Popular", "trending" or "viral" may only be written next to a link that shows it: a press report with numbers (followers, views, sales, chart position), an official account's metric reported on a date, or a platform's own trend report. Write the number, the date and "as reported". If you cannot find evidence, label the image **Editorial pick — no popularity evidence** and say why it is still included.
2. **Never invent numbers or rankings.** Xiaohongshu and Instagram mostly need a login, so counts usually cannot be verified from here. Say so instead of estimating. Search phrases are "discovery terms", not evidence.
3. **Never present a recipe as the photographer's settings.** Most photobook references are film or heavily graded. Unless the photographer or publisher published settings (link it), the recipe is "a starting point to approximate this file on an X-T5".
4. **Separate light from processing.** Golden backlight, haze, sunset colour and flash are things that happen on location. Write them as shooting instructions (time, direction, distance), not as camera settings.
5. **State what the camera cannot do.** Lifted or faded black points, halation around lights, bloom or mist, split toning beyond what a film simulation does, and selective colour shifts all need post-processing or a physical filter. Write a "做不到" (can't do in-camera) line for every reference.
6. **Measure the file you actually have.** Web previews are resized and re-encoded, and sometimes watermarked. Report numbers as properties of that file, and crop out watermarks before measuring.
7. **No AI images as colour targets.** AI concept art may illustrate composition, clearly labelled, but is never a reference to match.
8. **Rights and people.** Use only publicly published promotional or official images. Keep the original bytes and watermarks, credit the photographer and publisher, and never bypass paywalls or logins or copy a whole album. When the subject's age matters, document it from a source, as `clear-water-bay/research-notes.md` does.
9. **Confidence on every recipe line:** `measured` (from the script), `tested` (checked against your own test shot), or `estimate` (visual judgement). Never leave a line unlabelled.

## Step 1 — Find references with real evidence

Decide what the guide needs first: location type, light (time of day, weather, night or day), subject, gear (X-T5 with XF 23mm ≈ 35mm-e and 75mm ≈ 112.5mm-e), and the 2–4 looks the shoot is going for. Then look for references that match **the same kind of light**. A sunset reference cannot be matched at noon, and a night neon reference cannot be matched under streetlights alone.

Where evidence is usually findable:

| Source | What it proves | Notes |
| --- | --- | --- |
| Press articles about photobooks or campaigns (e.g. mdpr.jp / Modelpress, Oricon news) | Official preview images with photographer credits in captions; reported follower, view and sales figures with a date | The images are the publisher's public promotional versions. Read the caption for the photographer; article portraits may be by someone else. |
| Official photobook, brand or photographer accounts (X, Instagram, YouTube) | Engagement on the official post | Cite counts only if they are visible or reported, with the date seen. |
| Platform trend reports (Pinterest Predicts, Instagram/Meta trend reports) | Growth in a style or search term | These are forecasts or search growth, not portrait popularity. Quote the method footnote. |
| Fashion and culture press (Vogue etc.) | That a social trend was observed in a given month | Distinguish the fashion trend from your photographic interpretation. |
| Published recipe sites (e.g. Fuji X Weekly) | That a named recipe exists, with its exact settings | Link it if used, and never attribute it to the reference photographer. |

Write search queries in the language of the source (Japanese for photobooks, Chinese for HK/XHS, English for Pinterest and Vogue). Combine location, light and genre terms, for example `夜景 ポートレート 写真集 先行カット`, `維港 夜景 人像`, `Hong Kong night portrait Classic Neg`. Record queries that produced nothing as well.

Reject a candidate when:
- you cannot find a credit;
- the location or light does not transfer to this shoot (an interior, a pool, the wrong time of day);
- the only evidence is "it looks popular";
- the subject's age or consent is unclear;
- the only copy is behind a login.

Write each rejection into the guide's research notes under "Exclusions", as the Clear Water Bay notes do.

## Step 2 — Include or link the photo

- **Downloadable public promotional image:** save the exact bytes the source page serves, without re-encoding, cropping or removing watermarks:
  ```sh
  curl -L -o <guide>/images/<subject-book-scene>.jpg '<source_image URL>'
  sha256sum <guide>/images/<file>.jpg
  python3 -c "from PIL import Image; print(Image.open('<guide>/images/<file>.jpg').size)"
  ```
  Then add an entry to `<guide>/image-sources.json` with the same fields as `clear-water-bay/image-sources.json`: `file`, `source_page`, `source_image`, `source_caption`, `sha256`, `width`, `height`, `credit`, `public_reference_checked`. Look at the downloaded file before using it, because some hosts return a placeholder.
- **Not appropriate or not possible to download** (login wall, Instagram or XHS post, blocked host): link it and describe it in one sentence. Mark the analysis `estimate` (visual), since it cannot be measured. If the network blocks the host, ask the user to save the image into the guide folder rather than skipping it.
- In the page, every reference image carries the photographer and publisher credit and a link to the source page, following the `.ref.album-card` / `.reference-photo` markup in `clear-water-bay/index.html`, so the shared lightbox works.

## Step 3 — Analyse the look

### 3a. Describe the light (shooting instructions)
Write down:
- the light's direction relative to the subject (front, side, back, top);
- its hardness (hard sun, open shade, overcast, mixed artificial);
- the colour of the light versus the colour in the shadows (warm sun with cool skylight shadows is light, not a recipe);
- the time of day or source, and flash, if visible (hard shadow edge, bright subject against a darker background).

Turn this into what to do on location: the time window, which way the model faces, and the focal length and distance with the X-T5 lenses.

### 3b. Measure
Run the helper on the full frame, then on crops of specific regions:

```sh
python3 skills/photo-style-guide/analyze_reference.py <guide>/images/ref.jpg
python3 skills/photo-style-guide/analyze_reference.py <guide>/images/ref.jpg --crop 0.40,0.55,0.60,0.80   # e.g. the white dress
```

- **Full frame:** tonal range (L\* percentiles, crushed and clipped share, p5–p95 spread), overall chroma, and hue balance.
- **Neutral crop** (white dress, grey rock, cloud): this is the only honest white-balance reading. A whole-frame "cast" in a sea-and-sky picture is mostly the scene's own colours.
- **Something that should be black** (hair, deep shadow): this tells faded blacks apart from a frame with nothing dark in it.
- **Skin crop:** hue and chroma of skin. Compare it with your test shot rather than with fixed targets.

Paste the relevant numbers into the guide's research notes. The script prints observations, and its own caveats say where a number cannot decide the question.

### 3c. Map to X-T5 settings

| Measured / seen | X-T5 starting point | Honest limit |
| --- | --- | --- |
| Darkest black object reads L\* > ~12 (faded) | Shadows −1 to −2, DR200; Pro Neg. Std, Eterna or Astia | A raised black floor cannot be made in-camera. Name the curve to apply in post, or accept deeper blacks. |
| Highlights top out below L\* ~90, nothing clipped | Highlights −1 to −2, DR200 (ISO ≥250) or DR400 (ISO ≥500), exposure −⅓ | DR settings protect highlights; they cannot recover clipped ones. |
| Large clipped area that is part of the look (airy, overexposed) | +⅔ to +1 EV, Highlights 0, DR100 | Check that the clipped part is sky or dress, not skin. |
| Low p5–p95 spread (soft) | Pro Neg. Std, Eterna or Astia; Highlights −1, Shadows −1 | Mist or flare softness is optical: shoot into light, or use a diffusion filter. Clarity −2 to −3 only approximates it. |
| High spread, dense shadows | Classic Chrome, Classic Neg. or Pro Neg. Hi; Shadows +1 to +2 | — |
| Neutral crop b\* > +5 (warm) | WB shift R+1 to +3 / B−1 to −3, or a higher Kelvin value (renders warmer) | Calibrate your own step size: shoot shift 0 and R+2 and compare. |
| Neutral crop b\* < −4 (cool) | WB shift B+1 to +3 / R−1 to −2, or a lower Kelvin value | — |
| Neutral crop a\* > +4 (magenta) / < −4 (green) | Fuji has only R/B axes: R and B both + gives magenta, both − gives green | — |
| Highlights warmer than shadows (split tone) | Nostalgic Neg. (amber highlights) or Classic Neg.; else a warm WB in cool light | No independent highlight/shadow toning in-camera. |
| Chroma median < 15 (muted) | Classic Chrome, Eterna, Eterna Bleach Bypass, or Color −2 to −4 | — |
| Chroma median 15–25 (natural) | Astia, Provia, Pro Neg. Hi/Std; Color 0 to +1 | — |
| Chroma median > 25 (vivid) | Velvia or Color +2 to +4 | Velvia pushes skin toward red. Check skin hue. |
| Deep saturated blue sky or sea with gradation | Color Chrome FX Blue Weak/Strong | — |
| Saturated reds, oranges or yellows that keep gradation | Color Chrome Effect Weak/Strong | — |
| Visible film grain | Grain Weak/Strong, Small/Large; mark `estimate` | Grain at web size is usually compression. Do not promise a grain match. |
| Glow or halation around lights (night, CineStill-style) | Tungsten WB (~3000–3400 K) with Eterna or Classic Neg. for a teal cast; Highlights −1 | Red halation is not a camera setting; it needs post or a filter. Say so. |

### 3d. Film simulation characteristics (X-T5)
Confirm the exact list in the official menu page before prescribing: https://fujifilm-dsc.com/en/manual/x-t5/menu_shooting/image_quality_setting/. If a simulation (for example Reala Ace) is not in that list, do not prescribe it for the X-T5.

| Simulation | Tonality | Colour | Typical fit |
| --- | --- | --- | --- |
| Provia / Standard | Medium | Neutral, standard | Baseline when nothing else fits |
| Velvia / Vivid | Hard | High saturation | Landscape-led frames; risky on skin |
| Astia / Soft | Soft on skin | Rich sky and foliage | Outdoor portraits with blue and green |
| Classic Chrome | Hard shadows | Muted, cyan-leaning blues | Documentary, overcast, urban |
| Pro Neg. Hi | Medium-hard | Natural skin | Portraits in contrasty light |
| Pro Neg. Std | Soft | Low saturation, natural skin | Soft light, faded or pastel looks |
| Classic Neg. | Hard | Hue shifts (snapshot negative film character) | Nostalgic street and night |
| Nostalgic Neg. | Softer shadows | Amber in highlights | Warm, 1970s-print feel |
| Eterna / Cinema | Very soft | Low saturation | Cinematic, night, flat grade |
| Eterna Bleach Bypass | Hard | Very low saturation | Gritty, desaturated |
| Acros / Monochrome (+Ye/R/G), Sepia | — | B&W | Monochrome references |

### 3e. Write the recipe with every parameter
Fill in every line, each marked `measured`, `tested` or `estimate`:

```
Film simulation · Grain (roughness/size) · Color Chrome Effect · Color Chrome FX Blue ·
White balance (+ R/B shift or Kelvin) · Dynamic range · Highlights · Shadows · Color ·
Sharpness · High ISO NR · Clarity · Exposure compensation · Lens, aperture, shutter, ISO range
```

Ranges on the X-T5: Highlights and Shadows −2 to +4 (½ steps); Color, Sharpness and High ISO NR −4 to +4; Clarity −5 to +5; WB shift R/B −9 to +9; DR200 needs ISO ≥250 and DR400 ISO ≥500 (see the manual link above). D Range Priority disables the tone curve and DR, so do not combine them in one recipe.

### 3f. Validate with a test shot when possible
Shoot one frame in similar light, then compare:
```sh
python3 skills/photo-style-guide/analyze_reference.py ref.jpg my-test.jpg --crop ...
```
Move one setting at a time to shrink the reported differences, then mark the changed lines `tested`. If no test shot exists, say "untested" in the guide.

## Output in the guide

For each reference, in Chinese (the guide's language), in the guide's reference section:

1. The image (or link), with credit and source link.
2. **为什么选它 (why it was chosen):** the popularity evidence with number, date and link, or "编辑精选，无热度数据" (editor's pick, no popularity data) with the reason.
3. **光线 / 现场怎么拍 (light / how to shoot it on location):** time, direction, distance and lens, from 3a.
4. **测量 (measured):** 2–4 numbers that drive the recipe (e.g. "白裙 b\*=+9 偏暖；最暗处 L\*18 黑位抬起" — white dress b\*=+9, warm; darkest point L\*18, raised black floor).
5. **X-T5 起始配方 (starting recipe):** the full recipe from 3e in the dark `.how` / `.recipe` block, with confidence labels.
6. **做不到 (can't do in-camera):** what needs post, a filter, or different light.

In `<guide>/research-notes.md`, add a table row per reference covering:
- source and date;
- the evidence and what it does and does not prove;
- the measurements;
- the recipe confidence.

List the rejected candidates under "Exclusions".

### Specific vs generic — the bar

- Generic (reject): "Use Classic Chrome and shoot at golden hour for a dreamy film look."
- Specific (accept; illustrative numbers): "Backlit, sun about 15° above the horizon behind her left shoulder. The white dress measures b\*=+11 (warm) and the darkest hair only reaches L\*21, so the blacks are faded. On the X-T5: Astia, WB Daylight R+2/B−2 (measured), DR200, Highlights −1, Shadows −2 (measured), Color 0, CCE Weak (estimate), exposure +⅓ (estimate). Can't do in-camera: the raised black floor at L\*21 needs a curve in post. Without it, expect deeper hair shadows than the reference. Shoot 17:10–17:35 in October; before that the sun is too high for this rim light."

## Final checklist
- [ ] Every "popular" claim has a number, date and link, or the reference is labelled as an editorial pick.
- [ ] Every image is credited and linked; downloaded files are in `image-sources.json` with sha256.
- [ ] Light is described as shooting instructions, separate from the recipe.
- [ ] Measurements come from the full frame plus neutral and dark crops (watermarks cropped out).
- [ ] The recipe has every parameter, each labelled measured, tested or estimate, and uses only simulations listed in the X-T5 manual.
- [ ] Every reference has a "can't do in-camera" line.
- [ ] Rejected candidates and unverifiable platform data are written down in the research notes.
