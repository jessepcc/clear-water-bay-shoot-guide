# 外拍现场指南 · Shoot field guides

Mobile-first, static Chinese-language field guides for portrait shoots, one per location. The site root lists every guide; each guide lives in its own folder and is served at `/<slug>/`.

| Guide | Folder | Shoot date | Live |
| --- | --- | --- | --- |
| 清水湾 · 海滩 × 大坑墩 (Clear Water Bay beaches and Tai Hang Tun grassland) | [`clear-water-bay/`](clear-water-bay/) | 2026-10-03 | https://clearwater-bay-shoot-guide.vercel.app/clear-water-bay/ |

The repository and Vercel project keep their original Clear Water Bay names; they host every guide.

## Layout

```text
index.html          Guide index at the site root: one card per guide, newest first
assets/guide.css    Shared design system for the index and every guide
assets/guide.js     Shared behaviour: scene tabs, reference filters, image lightbox
vercel.json         Trailing-slash redirects and redirects from pre-reorganisation URLs
clear-water-bay/    One folder per guide: index.html, images/, research notes, image sources
```

## Run locally

No package installation or build is needed. From this checkout:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Open http://127.0.0.1:8000/ for the index and http://127.0.0.1:8000/clear-water-bay/ for a guide. Guide pages use relative paths (`images/…`, `../assets/…`), so a guide URL must end with `/`; both Python's server and the `trailingSlash` setting in `vercel.json` redirect `/<slug>` to `/<slug>/`.

## Add a guide

1. Choose a short kebab-case slug, such as `victoria-night`, and create `victoria-night/index.html` with its own `images/` folder. Starting from a copy of `clear-water-bay/index.html`, keep the `../assets/guide.css` stylesheet, the `../assets/guide.js` script, the `.hero-back` link to `../`, and the `#lb` lightbox markup; replace the rest.
2. Build from the shared components (`.card`, `.recipe`, `.scene-tabs`, `.ref-filters` with `.album-card`, `.gallery .shot`, `.concept`, `.timeline`, `.field-dock`) so the interactive parts need no new JavaScript. The markup each widget expects is described at the top of `assets/guide.js`.
3. Put guide-only styling in a `<style>` block in that page, overriding the `:root` tokens when the guide needs its own palette (for example, a darker one for a night shoot). Change `assets/guide.css` or `assets/guide.js` only for improvements that every guide should get, and recheck every guide afterwards.
4. Build the reference / colour-style section with the project skill at `.claude/skills/photo-style-guide/` (in Claude Code, ask for it or run `/photo-style-guide`): real references with documented popularity, credits and links, measured tone and colour, and an X-T5 film-simulation recipe that states what it cannot recreate. Keep research notes and image source records inside the guide folder, as `clear-water-bay/` does.
5. Add the guide's card at the top of the list in the root `index.html`, and add a row to the table above.

## Deploy

The existing Vercel project serves this static repository and is connected to GitHub `main`. Publishing a commit to `main` triggers its production deployment at https://clearwater-bay-shoot-guide.vercel.app/. No build command, API keys, backend services, or framework configuration are required; `vercel.json` only configures URL redirects.

Until the reorganisation, the site root was the Clear Water Bay guide, and its old links still work. The index page forwards section links such as `/#reflib` to `/clear-water-bay/#reflib`, and `vercel.json` redirects `/images/*`, `/research-notes.md` and `/image-sources.json` to the guide folder. Keep those root paths unused.
