# Agent instructions

This repository is a static site of Chinese-language portrait shoot guides, one folder per location (see README.md for layout, local preview and how to add a guide). There is no build step.

## Skills

Skills live in `skills/<name>/SKILL.md` (Agent Skills format: YAML front matter with `name` and `description`, then instructions). Read the whole SKILL.md before starting a task that matches its description, and follow it.

| Skill | Use when |
| --- | --- |
| [`skills/photo-style-guide/`](skills/photo-style-guide/SKILL.md) | Creating a guide's reference / colour-style section: first real, dated photos of the actual location, then reference photos, or turning a reference photo's look into a Fujifilm X-T5 film-simulation recipe. Includes `analyze_reference.py` (needs Python 3 + Pillow). |

## Conventions

- Guide pages use the shared `assets/guide.css` and `assets/guide.js`; keep guide-specific styling inside the guide page.
- Reference images: keep source-served bytes and watermarks, record provenance in `<guide>/image-sources.json`, credit and link every image.
- Never invent popularity numbers, photographer settings or sources.
