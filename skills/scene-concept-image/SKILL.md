---
name: scene-concept-image
description: Create an AI concept image of a planned shot, grounded in real photos of the actual location, when no real reference photo exists for that scene, light and pose. Use only after the photo-style-guide skill's scene research (Step 0) and reference search (Step 1) found no direct reference. Covers choosing the real base photo, writing a fact-based prompt, generating with whatever image tool the harness has, rejecting images that contradict the real scene, and labelling and recording the result honestly.
---

# Scene concept image: real scene → AI concept of the planned shot

A concept image shows the model and photographer **what the planned frame could look like at this exact spot**: where she stands, which way the light falls, how much of the scene the lens includes. It is a planning aid, never evidence. It is never a colour target for a film-simulation recipe, and never stands in for what the location looks like (see `skills/photo-style-guide/SKILL.md`, rules 7 and Step 0).

## When to use, and when not to

Use it when all of these hold:
- the guide needs a specific scene + light + pose combination;
- Step 1 of photo-style-guide found **no real reference** for it (write that down in the research notes, with the searches tried);
- you have at least one **real, located, dated photo of the spot** from Step 0 (licensed, public-domain, or taken by the user).

Do not use it to:
- replace a real scene photo you could not find (say it is missing instead);
- make a location look greener, emptier, sunnier or more dramatic than the scene reality note says it is in the shoot's season;
- recreate or imitate a specific photograph, photobook or living photographer's style ("in the style of …"), or a real person's likeness;
- depict the actual model unless she has agreed to having her photo used as generator input. By default the person is a fictional adult.

## Step 1 — Fix the facts before writing a prompt

From the photo-style-guide Step 0 notes, write a short fact sheet for the shot. Every item must come from a real scene photo, a measurement or a calculation:

- **Spot geometry:** what is left, right and behind the subject from the camera position (e.g. "granite boulders camera-left, sandy cove, wooded hill behind, open sea to the east"). Name the base photo it comes from.
- **Season and surface colours:** e.g. "October: grass mid-green with brown patches; sand pale grey-beige; sea blue-green". Use `analyze_reference.py` crops of the real photo where possible.
- **Light:** sun azimuth and elevation at the planned time and date (from a sun calculator), and the resulting direction relative to the camera and subject. At night, the actual light sources: street lamps (colour), building signage, harbour skyline.
- **Weather and visibility:** clear, hazy or overcast, from the forecast or typical conditions for the date. Say which.
- **Camera:** the X-T5 lens as a full-frame equivalent (XF 23mm ≈ 35mm, 75mm ≈ 112.5mm), camera height, distance to subject, and aperture (depth of field).
- **Subject:** fictional adult woman; wardrobe and props from the shot plan; the pose as a single action ("walking along the wet sand, looking back over her right shoulder").
- **Crowd and clutter:** what is realistically in frame at that time (other beachgoers, lifeguard tower, railings, power lines). Keep them unless the composition genuinely excludes them.

## Step 2 — Generate

Prefer methods that keep the real scene's geometry:

1. **Image editing / image-to-image with the real scene photo as input** (e.g. models that accept a reference image and an edit instruction, or img2img and inpainting in Stable Diffusion-type tools). Add the subject and adjust the light; keep the landscape. Only use input photos whose licence allows modification (CC BY / BY-SA, public domain, the user's own). Never use an "all rights reserved" photo as input.
2. **Text-to-image** when no usable base image exists. Describe the fact sheet literally, and plan for more rejected images.

Prompt template (fill every line from the fact sheet; no style names of real photographers, brands or people):

```
Photograph of a fictional adult woman in her twenties at [spot description from fact sheet],
[pose as one action], wearing [wardrobe].
Camera: [35mm / 112.5mm full-frame equivalent], eye level / waist level, [distance] m away, [aperture] depth of field.
Light: [sun direction relative to subject and camera, elevation, hard/soft], [weather].
Scene details that must match reality: [3–6 concrete items: landmarks, vegetation state, sand colour, clutter].
Natural colours as seen in the real scene; no added glow, no exaggerated saturation, no fantasy elements.
```

If the harness has no image-generation tool, write the filled prompt (and the base photo link) to `<guide>/concept-prompts.md`, tell the user which kind of tool to run it in (one that accepts a reference image for editing is best), and stop. Do not fabricate an image by other means.

## Step 3 — Reject anything that contradicts the real scene

Compare each generated image side by side with the real base photo and the fact sheet. Reject it if any of these fail:

- **Geometry:** landmarks, coastline shape and horizon position are consistent with the real spot; no invented cliffs, piers, islands or buildings.
- **Light physics:** shadows fall away from the sun's stated direction; the rim light is on the side facing the sun; the sky brightness fits the sun's elevation; night lights have plausible colours and positions.
- **Season and colour:** vegetation and ground colours are no more saturated than the real photo. Run `python3 skills/photo-style-guide/analyze_reference.py real.jpg concept.jpg --crop …` on the same region (grass, sand, sea). A large chroma excess means regenerate or tone it down.
- **Lens:** the field of view and background compression match the stated focal length (a 112.5mm-e frame should not show a wide coastline).
- **Person:** an adult; normal anatomy (hands, limbs, eyes); not resembling a real, identifiable person; modest, appropriate wardrobe for a public location.
- **Artefacts:** no garbled text or signs, warped horizons, or duplicated objects.

Write in the research notes how many images were generated and how many were rejected, and why.

## Step 4 — Save, label and record

- Save as `<guide>/images/concept-<spot>-<shot>.jpg`, about 640–960 px on the long edge and under ~150 KB, the size of the existing concept images. Keep any provenance metadata (C2PA / content credentials) the generator embeds; do not strip it.
- In the page: keep the existing label pattern `AI概念示意 · 非实地照片` (AI concept illustration · not a real photo) on or next to the image, plus `基于实景：<link to real base photo>` (based on the real scene: …). Use the `.concept` markup in `clear-water-bay/index.html` so the shared lightbox works. Put the real scene photo (or its link) next to the concept, so nobody mistakes the concept for the location.
- In `<guide>/image-sources.json`, add an entry with `"type": "ai-concept"` and: `file`, `generator` (tool and model name/version as shown by the tool), `generated` (date), `base_image` (URL and licence, or "none, text-to-image"), `prompt` (exact text), `fact_sheet` (short), `sha256`, `width`, `height`, `rejected_variants` (count).
- Never use a concept image as a colour or tonal target for the Fujifilm recipe. Recipes come only from real references (photo-style-guide Step 3).

## Final checklist
- [ ] Research notes show no real reference exists for this scene + light + pose, with the searches tried.
- [ ] Every fact-sheet item traces to a real scene photo, a measurement or a sun/forecast calculation.
- [ ] The base image's licence allows modification, or text-to-image was used.
- [ ] Geometry, light direction, season colour, lens and person checks all passed; rejected variants are counted.
- [ ] The image is labelled `AI概念示意 · 非实地照片` with a `基于实景` link, shown next to a real scene photo, and recorded in `image-sources.json` with its prompt and generator.
