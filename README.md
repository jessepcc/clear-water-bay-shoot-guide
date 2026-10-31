# 外拍现场指南 · Shoot field guides

Mobile-first, static Chinese-language field guides for portrait shoots, one per location. The site root lists every guide; each guide lives in its own folder beneath the site base URL, https://jessepcc.github.io/clear-water-bay-shoot-guide/.

| Guide | Folder | Shoot date | Live |
| --- | --- | --- | --- |
| 香港公園 · 把清新拍得自然（單人女生人像、圓形水簾／白橋／溫室） | [`hong-kong-park/`](hong-kong-park/) | 2026-11-08，建議 13:30–17:15 | https://jessepcc.github.io/clear-water-bay-shoot-guide/hong-kong-park/ |
| 维港 · 蓝调飞灯与城市人像 (Victoria Harbour dusk-to-night, one-light portraits) | [`victoria-night/`](victoria-night/) | 日期未定，17:00–19:00 | https://jessepcc.github.io/clear-water-bay-shoot-guide/victoria-night/ |
| 清水湾 · 海滩 × 大坑墩 (Clear Water Bay beaches and Tai Hang Tun grassland) | [`clear-water-bay/`](clear-water-bay/) | 2026-10-03 | https://jessepcc.github.io/clear-water-bay-shoot-guide/clear-water-bay/ |

The repository keeps its original Clear Water Bay name; it hosts every guide.

## Layout

```text
index.html          Guide index at the site root: one card per guide, newest first
assets/guide.css    Shared design system for the index and every guide
assets/guide.js     Shared behaviour: scene tabs, reference filters, image lightbox
.nojekyll           Publish the static files directly on GitHub Pages
skills/             Agent skills (Agent Skills format), listed in AGENTS.md
vercel.json         Trailing-slash redirects and redirects from pre-reorganisation URLs
clear-water-bay/    One folder per guide: index.html, images/, research notes, image sources
victoria-night/     X-T5 + 23mm / 75mm + iT32 / X5; CTO, off-camera flash and dusk-to-night shots
hong-kong-park/     2026-11-08 fresh portraits; real scenes, AI concepts, social-source checks, reflector / iT32 guidance
```

## Run locally

No package installation or build is needed. From this checkout:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Open http://127.0.0.1:8000/ for the index and http://127.0.0.1:8000/clear-water-bay/ for a guide. Guide pages use relative paths (`images/…`, `../assets/…`), so they also work beneath GitHub Pages' `/clear-water-bay-shoot-guide/` project prefix. Open guide URLs with their trailing `/`.

Run the server from the **repository root**, not a guide folder. Serving only `victoria-night/` makes `/assets/guide.css` and `/assets/guide.js` unavailable. Use a browser to view the served site. The Codex file tab may display HTML source as text instead of rendering a webpage; that is a viewer limitation, not a CSS failure.

For a downloadable HTML copy to open in a web browser, generate a self-contained export:

```sh
python3 scripts/export-preview.py victoria-night --output /tmp/victoria-night-preview.html
```

The export embeds shared CSS, JavaScript and original image bytes without changing the canonical guide. Download it and open it in a browser; it does **not** make an HTML source-only file viewer render a webpage. In-page controls work offline; links to other site pages and research files point to GitHub Pages and require those pages to be deployed. For review within a file viewer, provide rendered PNG or PDF exports instead. Keep generated exports outside the repository; publish the canonical site files.

## Add a guide

1. Choose a short kebab-case slug, such as `victoria-night`, and create `victoria-night/index.html` with its own `images/` folder. Starting from a copy of `clear-water-bay/index.html`, keep the `../assets/guide.css` stylesheet, the `../assets/guide.js` script, the `.hero-back` link to `../`, and the `#lb` lightbox markup; replace the rest.
2. Build from the shared components (`.card`, `.recipe`, `.scene-tabs`, `.ref-filters` with `.album-card`, `.gallery .shot`, `.concept`, `.timeline`, `.field-dock`) so the interactive parts need no new JavaScript. The markup each widget expects is described at the top of `assets/guide.js`.
3. Put guide-only styling in a `<style>` block in that page, overriding the `:root` tokens when the guide needs its own palette (for example, a darker one for a night shoot). Change `assets/guide.css` or `assets/guide.js` only for improvements that every guide should get, and recheck every guide afterwards.
4. Build the reference / colour-style section with the project skill at `skills/photo-style-guide/` (any coding agent finds it through `AGENTS.md`; in Claude Code you can also run `/photo-style-guide`): real references with documented popularity, credits and links, measured tone and colour, and an X-T5 film-simulation recipe that states what it cannot recreate. Keep research notes and image source records inside the guide folder, as `clear-water-bay/` does.
5. Add the guide's card at the top of the list in the root `index.html`, and add a row to the table above.

## Deploy

GitHub Pages publishes the root (`/`) of the `main` branch at https://jessepcc.github.io/clear-water-bay-shoot-guide/. In repository **Settings → Pages**, the publishing source is **Deploy from a branch → main → / (root)**. Publishing a commit to `main` triggers the built-in Pages deployment. The root `.nojekyll` marker disables Jekyll processing, preserving the HTML, images, JavaScript and source records as static files. No build command, extra workflow file, API keys or backend services are required.

Use relative links for site navigation and assets so the project prefix stays intact. The index forwards its old section links (for example `#reflib`) to `clear-water-bay/#reflib` within the current host and project prefix.

The existing Vercel integration remains available at https://clearwater-bay-shoot-guide.vercel.app/. Its `vercel.json` redirects from the pre-reorganisation `/images/*`, `/research-notes.md` and `/image-sources.json` URLs apply only on Vercel; GitHub Pages does not read that configuration. Guide-folder URLs and shared assets work on both hosts. Mainland-China connectivity to GitHub Pages can still vary by network.
