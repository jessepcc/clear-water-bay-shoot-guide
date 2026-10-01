# 清水湾女生外拍现场指南

A mobile-first, static Chinese-language field guide for Clear Water Bay beaches and the Tai Hang Tun country-park grassland. Prepared for the Fujifilm X-T5, Fujinon XF 23mm F1.4 and Viltrox AF 75mm F1.2.

The guide includes five scene presets, eight verified public reference images from six photobooks, location and posing prompts, and a sourced 2026 social-media trend section. Original reference-image bytes and sample watermarks are preserved. Publication years, photographer credits and official behind-the-scenes material are identified separately.

## Run locally

No package installation or build is needed. From this checkout:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Use a browser to inspect `index.html`. Verify all five camera-scene controls, the beach/grassland reference filters, and image viewers with the close button, backdrop, and Escape key. Check mobile and desktop layouts. Research sources and selection limits are documented in [research-notes.md](research-notes.md).

## Deploy

The existing Vercel project serves this static repository and is connected to GitHub `main`. Publishing a commit to `main` triggers its production deployment at https://clearwater-bay-shoot-guide.vercel.app/. No build command, API keys, backend services, or framework configuration are required.
