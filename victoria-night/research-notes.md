# Victoria Harbour portrait guide — research and verification

Prepared 2026-10-03. Shoot times are **Asia/Hong_Kong (UTC+8)**.

## Brief and evidence boundaries

- X-T5, 23mm and 75mm lenses, one Godox iT32, user-confirmed **X5**, full CTO, half CTO and included small diffuser. No stand, softbox, second flash, grey card, extra filters or required helper.
- Young adult East Asian female model. References are official adult-era promotional images, with project-age evidence below. Posing is adapted to the model's comfort, not to stereotypes or cosmetic face-matching.
- 17:00–19:00, sunset to night at Victoria Harbour. Shoot date is unspecified: **2026-10-03 is an example**, not the booking date. Summer needs a different time window for night.
- Tsim Sha Tsui public waterfront, Museum of Art exterior to the western Avenue of Stars, treated as **one compact scene area**. Ocean Terminal is a clearly labelled neighbouring westward sky/light reference, not an added shoot stop or same camera position.
- Lens models/max apertures were not reconfirmed. Ordinary f/2.8–4 starting apertures avoid depending on f/1.2 or a particular make.
- Published-file measurements are **measured**. Camera menus and button behaviour are checked in official documents. All recipe/exposure/distance/power values are **estimate**. No physical camera/flash test exists, so no recipe line is `tested`.

## Sources and environment access

Initial research attempts returned network-policy 403 errors. Source access subsequently succeeded after the environment draft included the required source/CDN hosts. Saving a draft is not itself proof of runtime access; successful HTTPS fetches of these specific pages/files were the verification. Python standard-library urllib fetched public pages and original image bytes; no login, paywall, TLS bypass or image/watermark editing was used.

Custom hosts saved with existing package-manager presets preserved: commons.wikimedia.org, upload.wikimedia.org, en.wikipedia.org, fujifilm-dsc.com, godox.com, www.godox.com, strobist.blogspot.com, blogger.googleusercontent.com, mdpr.jp, img-mdpr.freetls.fastly.net, www.discoverhongkong.com, www.hko.gov.hk. Wikimedia thumbnails used a separate host; originals on upload.wikimedia.org were downloaded instead. Official photograph previews were found by following public “全文を読む” links to canonical `/news/detail/…` pages.

The correct Godox product URL is https://www.godox.com/product-e/iT32-X5.html. Earlier guessed `product-a/it32.html` and `product-a/iT32.html` were not canonical evidence. Fujifilm `taking_photo/flash/` returned 404 after source access; use the external-flash page below.

## Official equipment documentation

| Source checked 2026-10-03 | What it establishes | Practical interpretation |
| --- | --- | --- |
| [iT32 product](https://www.godox.com/product-e/iT32-X5.html) | Modular iT32/X5, built-in radio RX | Detach own X5, leave transmitter on camera |
| [iT32 manual](https://www.godox.com/Downloads/Godox_iT32.pdf), Chinese printed pp06–10,17–18; English pp49–53,61–62 | Power/unlock within 6s; USB-C lamp charging; X5 charges attached; receiver mode on detachment; long +/M selects TTL/M; short +/- adjusts power; 1/128–1/1, 1/3 steps | Do not invent an X5 TEST button, USB port, X3 menu or required channel-pairing ritual |
| Same manual, Chinese p08 | Orange=M, green=TTL; steady=camera connected, blinking=not connected; off=sleep/power off; red slow blink=low battery. Long minus/battery checks battery then switches off; any button wakes; camera cannot wake X5 | Power and hotshoe troubleshooting before radio changes |
| Same manual, Chinese p18 | HSS minimum output 1/16; Fujifilm HSS/rear curtain selected on camera | First session uses normal front-curtain 1/125s; rear curtain optional after test, HSS unnecessary |
| [Compatible camera list](https://www.godox.com/Downloads/Compatible_Camera_Model_List.pdf), also manual English p81 | **X5 F**, X-T5 in compatible group A | User confirmed X5, but its suffix is not confirmed by user; check hardware marking |
| [X-T5 external flash](https://fujifilm-dsc.com/en/manual/x-t5/peripherals_and_options/external_flash_units/) | Ordinary sync at 1/250s or slower; front/rear/AUTO FP options; shoe-mount flash settings | 1/125s mechanical leaves margin; no electronic/quiet shutter baseline |
| [X-T5 flash menu](https://fujifilm-dsc.com/en/manual/x-t5/menu_shooting/flash_setting/) | FLASH FUNCTION SETTING | Beginner menu path is camera F flash settings |
| [X-T5 screen setup](https://fujifilm-dsc.com/en/manual/x-t5/menu_setup/screen_set-up/) | PREVIEW WB in manual exposure for flash | View WB without dark pre-flash exposure preview |
| [X-T5 IQ menu](https://fujifilm-dsc.com/en/manual/x-t5/menu_shooting/image_quality_setting/) | Astia, Eterna, Classic Chrome, Pro Neg. Std; DR200 ISO≥250, DR400 ISO≥500; D Range Priority restrictions | Four complete JPEG recipes, all estimate; no unavailable simulation |

The manual illustrations were inspected to identify the two X5 buttons because extracted PDF text omitted button glyphs. The supplied diffuser spreads light; outdoor lack of bounce surfaces and its small emitting area prevent promising softbox softness. CTO/diffuser co-fitting is not established for the user's particular accessories; fit only when secure, otherwise use CTO alone. No claimed precise gel loss, measured colour temperature or output distance calibration.

## No-extra-gear geometry

- **On-camera:** model both hands free, 23mm environmental/full-length frames. Rotate her body and select negative space; do not pretend frontal flash becomes side light through JPEG settings.
- **Photographer-held:** right hand camera/left hand lamp, subject 1–1.5m, lateral reach40–60cm, approximate20–30°. At3m the same reach gives only about8–11°. This does not support the old draft's camera3m/lamp1m-at45° setup.
- **Model-held:** lamp roughly0.6m from face, just above eyes and front-side, tight75mm framing, camera4–6m. Lowest power1/128 first. One hand is occupied; crop feasibility must be checked. Begin f/4, ISO200–400; lowest power can still overexpose close to face, requiring distance/aperture/ISO adjustment and background rebalancing.
- For true night, start slower1/60→1/30 with a stationary face. If model-held minimum power prevents raising ISO and reach cannot increase, switch75mm to on-camera, f/2.8, ISO800,1/60s, halfCTO4000K, camera about4m, M1/32 then adjust. This explicitly trades side-light direction for ambient-exposure room and free hands; values remain estimates.
- Independent front key plus rear rim is impossible with a single unconstrained hand-held lamp; the baseline sixth scene is directional side-face light. A separate rear position would need another human to hold it, so is not a required shot.
- Slow shutter is **on-camera**, photographer uses both hands. 1/8 versus1/125 records approximately3.97 stops more ambient with fixed aperture/ISO. Flash and rear curtain do not erase accumulated face ghosting.
- No promises of reflective pavement, empty railings, building-light schedules, strong daylight suppression, or f/1.2 with a close lamp at minimum power.

## Scene evidence

Photos were acquired, located and inspected **before choosing the style portraits**. Dates are source/EXIF timestamps, not guaranteed corrected camera clocks. Actual bytes, image dimensions, original URLs, license links and SHA-256 are in [image-sources.json](image-sources.json). No resizing/re-encoding of stored images.

| Image / source | Capture date | Photographer/license | Location check and visible light | Limits |
| --- | --- | --- | --- | --- |
| [tst-sunset-2009.jpg](https://commons.wikimedia.org/wiki/File:HK_TST_Waterfront_Platform_Sunset_Evening_1.JPG) | 2009-10-07 17:17:05 | Kaohsen / CC BY-SA 3.0 | IFC on left, waterfront receding west, hazy warm sunset and deep foreground shade | October light/view direction only; old railings/facilities not current evidence |
| [tst-blue-hour-2010.jpg](https://commons.wikimedia.org/wiki/File:HK_TST_Harbour_City_Ocean_Terminal_view_blue_Victoria_Harbour_night_Oct-2010.JPG) | 2010-10-15 18:17:58 | Habact1015 / CC BY-SA 3.0 | Ocean Terminal/Tsim Sha Tsui waterfront, IFC and Bank of China opposite, blue overcast sky and city lighting | Adjacent west-side view, not Museum of Art forecourt; blurred foreground person not pose/exposure target |
| [tst-evening-2025.jpg](https://commons.wikimedia.org/wiki/File:HK_%E5%B0%96%E6%B2%99%E5%92%80_TST_Salisbury_Road_near_%E7%B6%AD%E5%A4%9A%E5%88%A9%E4%BA%9E%E6%B8%AF_Victoria_Harbour_n_%E9%A6%99%E6%B8%AF%E5%B3%B6%E5%8C%97_Kong_Island_North_evening_September_2025_R12S_03.jpg) | 2025-09-03 18:13:26 | 93MAINGMaisee Hungom / CC0 | Source identifies TST Salisbury Road; Bank of China/Admiralty skyline, public promenade railings, crowded foreground | September18:13 still bright; not October18:13 light. Retain timestamp watermark; not current construction assurance |

Scene reality: grey/blue water changes with light. Historical sunset sky/water mean b*=+18.6/+9.5, blue-hour sky/water=-30.9/-18.4, 2025 evening water=-5.7 (listed crops). These published JPG values demonstrate variability, not a forecast. Southern skyline framing gives a roughly western/camera-right setting sun. Sunset behind the model requires a changed direction/background. Crowds make75mm tight crops practical. A harbour ground-level view cannot deliver sand, close surf or a Bangkok rooftop city perspective.

## Solar calculation

Calculation dependency: `astral==3.2`, installed only in `/tmp/harbour-research-deps` for research; not an application dependency. Observer: latitude **22.294**, longitude **114.173**, elevation **5 m**. Time zone: `Asia/Hong_Kong`. Rounded to the nearest minute. Civil dusk uses the library's default depression of 6°.

| Date | Sunset | Civil dusk |
| --- | --- | --- |
| 2026-01-03 | 17:52 | 18:17 |
| 2026-04-03 | 18:39 | 19:02 |
| 2026-07-03 | 19:12 | 19:37 |
| 2026-10-03 | 18:09 | 18:32 |

2026-10-03 sun positions (degrees clockwise from north; approximate apparent elevation):

| Hong Kong time | Azimuth | Elevation |
| --- | --- | --- |
| 17:00 | 259.1° | 15.1° |
| 17:30 | 262.2° | 8.3° |
| 18:00 | 265.1° | 1.7° |
| 18:15 | 266.5° | −2.0° |
| 18:30 | 267.9° | −5.6° |
| 19:00 | 270.7° | −12.5° |

Reproduce with Astral 3.2:

```python
from astral import Observer
from astral.sun import sun, azimuth, elevation
from datetime import date, datetime
from zoneinfo import ZoneInfo

observer = Observer(22.294, 114.173, 5)
zone = ZoneInfo('Asia/Hong_Kong')
result = sun(observer, date=date(2026, 10, 3), tzinfo=zone)
print(result['sunset'], result['dusk'])
moment = datetime(2026, 10, 3, 17, 0, tzinfo=zone)
print(azimuth(observer, moment), elevation(observer, moment))
```

The shoot date remains unknown; the dates above are labelled examples. No weather forecast or final-date sky guarantee is made.

## Portrait references and popularity evidence

Selected just one matching public promotional preview per project, not whole albums. The original photographer's lighting/EXIF is **not disclosed** for these four photographs. Visible shadows and colour are observations; the proposed Godox setups are adaptations, not equipment attributions.

| Reference / publication | Adult age evidence | Popularity evidence and scope | Reason / recipe |
| --- | --- | --- | --- |
| [賀喜遥香, まっさら](https://mdpr.jp/news/detail/3156001),2022-05-16; 菊地泰久/新潮社 | Same article says turned20 on2021-08-08, project shot after that milestone; sunset at Miyakojima Yonaha Maehama | [2022-05-22](https://mdpr.jp/news/detail/3166314): official photobook Twitter>160,000, >100,000 within18h. Campaign history, not specific-photo likes or current rank | Sunset turn/look-back; warm natural light, C0 Astia |
| [金川紗耶, 好きのグラデーション](https://mdpr.jp/news/detail/4792880),2026-06-04; 三宮幹史/DONUTS・主婦の友社 | Source describes24-year-old project, Dubrovnik dusk-to-night SevenNet back cover | **Editorial pick—no verified individual/photo popularity metric.** Do not assign Nogizaka group or another member's counts | Cool water/warm face and small hand gesture; C1 Eterna, FullCTO3200K blue variation |
| [今田美桜, ラストショット](https://mdpr.jp/news/detail/1940728),2020-01-19; 三宮幹史/講談社 | Article explicitly22, Bangkok rooftop image | [2018-12-12](https://mdpr.jp/news/detail/1809790): Instagram#MVI2018 Trend award, highest Japanese-account growth rate/buzz. Historical platform award; no count invented and not this photograph | Body turned/face back, luminous near eye/cool city; C2 ClassicChrome |
| [梅澤美波, 透明な覚悟](https://mdpr.jp/news/detail/4710416),2026-01-09; 東京祐/光文社 | Explicit26, CLASSY. regular fashion model, last Florence/PiazzaleMichelangelo night shoot | [2022-12-20](https://mdpr.jp/news/detail/3514790): she represented Nogizaka46, group Weibo>3million, fourth consecutive excellent female group award. **Group only, no verified personal/photo count; photograph editorial pick** | One free hand/soft head tilt, warm face and blue bokeh; C3 ProNeg.Std |

Social-media numbers are “as reported” on their dates. No current2026 cross-platform ranking or Xiaohongshu/Instagram specific-photo engagement was verified. Imada's source also discusses Naomi Watanabe's separate engagement/follower awards; those numbers/ranks must not be attributed to Imada. Umezawa's group3million must not be labelled her personal following. Kanagawa's three scheduled livestreams are promotional activity, not a popularity metric.

## Technical colour demonstration

[David Hobby / Strobist, Using Gels to Shift the Ambient](https://strobist.blogspot.com/2017/04/using-gels-to-shift-ambient.html), publication2017-04, capture date unknown. Author publishes unshifted comparison and blue ambient boat portrait, and explicitly describes3200K, fullCTO+halfCTO, cardboard snoot, single flash, ambient underexposed2–3 stops. His actual stated setup is distinguished from the user's **single fullCTO** adaptation; no instruction to acquire a snoot or stack supplied filters. Two author-served small images are retained with credit. They are technical examples only, not EastAsian-female pose references, not claimed popular, and not the colour basis of a complete matching recipe.

## Measurement method and results

Helper: [analyze_reference.py](../skills/photo-style-guide/analyze_reference.py), Python3+Pillow. Called its `measure()` function for full frame, candidate neutral, dark and skin crops for each style photo, plus scene sky/water crops; output retained in [reference-measurements.json](reference-measurements.json). Empty lightness bands use JSON null for undefined means. Full frame uses at most400×400 sampled pixels after EXIF orientation; Lab assumes sRGB and D65. Published web JPEGs are not calibrated RAW. Mean a*/b* below are weighted across the helper's lightness bands. Watermark regions excluded from scene colour crops; no watermark removed from stored/displayed images.

Kanagawa's pale patterned dress, Imada's distant lit building and Umezawa's coated rail are **candidate neutral objects only**, with unknown pigments/lighting. They cannot establish white balance; no WB measured from whole-frame colour. Kaki's pale skirt supports visible warmth but is not a physical neutral calibration. Skin crop coordinates refer to selected visible regions and cannot represent all skin colours or all parts of the same face. Grain/compression and gamut do not reveal the original camera/film.

| File / crop | Normalised crop x0,y0,x1,y1 | L* p0.5 / p50 / p95 | p95−p5 | Chroma median | Mean a* / b* | clipped L*>97 |
| --- | --- | --- | --- | --- | --- | --- |
| tst-sunset-2009.jpg / full | full | 3.3 / 33.0 / 85.3 | 78.7 | 13.0 | +1.3 / +12.2 | 1.11% |
| tst-sunset-2009.jpg / sky | 0.68,0.01,0.88,0.26 | 67.1 / 78.3 / 86.9 | 16.4 | 18.5 | +2.5 / +18.6 | 0.00% |
| tst-sunset-2009.jpg / water | 0.08,0.56,0.27,0.61 | 24.1 / 36.7 / 40.7 | 14.1 | 10.2 | -1.2 / +9.5 | 0.00% |
| tst-sunset-2009.jpg / paving | 0.35,0.86,0.46,0.96 | 13.6 / 22.0 / 26.3 | 9.5 | 6.9 | -1.1 / +6.6 | 0.00% |
| tst-blue-hour-2010.jpg / full | full | 15.0 / 45.6 / 71.8 | 39.9 | 17.2 | +4.0 / -8.6 | 0.61% |
| tst-blue-hour-2010.jpg / sky | 0.3,0.01,0.65,0.19 | 41.4 / 44.5 / 49.5 | 7.1 | 32.8 | +7.6 / -30.9 | 0.24% |
| tst-blue-hour-2010.jpg / water | 0.6,0.48,0.72,0.54 | 26.9 / 31.0 / 34.0 | 5.7 | 18.6 | +1.8 / -18.4 | 0.00% |
| tst-evening-2025.jpg / full | full | 1.2 / 45.1 / 89.7 | 86.3 | 8.8 | -1.1 / -3.4 | 0.14% |
| tst-evening-2025.jpg / sky | 0.02,0.01,0.4,0.13 | 80.8 / 83.2 / 85.0 | 3.7 | 14.7 | -3.9 / -14.1 | 0.00% |
| tst-evening-2025.jpg / water | 0.47,0.52,0.56,0.56 | 9.6 / 54.8 / 69.8 | 42.8 | 7.0 | -2.9 / -5.7 | 0.00% |
| kanagawa-twilight.jpg / full | full | 6.5 / 33.7 / 60.3 | 50.5 | 17.9 | +15.1 / +2.1 | 0.21% |
| kanagawa-twilight.jpg / neutral-candidate-dress | 0.44,0.63,0.49,0.66 | 31.6 / 43.2 / 58.9 | 24.5 | 14.6 | +13.4 / +3.5 | 0.00% |
| kanagawa-twilight.jpg / dark-ribbon | 0.46,0.269,0.49,0.282 | 5.1 / 8.9 / 42.1 | 36.6 | 27.8 | +10.9 / +5.4 | 0.00% |
| kanagawa-twilight.jpg / skin | 0.47,0.173,0.51,0.207 | 21.3 / 47.6 / 53.8 | 22.6 | 34.5 | +29.6 / +18.4 | 0.00% |
| kanagawa-twilight.jpg / sky | 0.02,0.01,0.32,0.07 | 43.3 / 64.2 / 77.5 | 30.9 | 11.8 | +10.2 / -4.7 | 0.00% |
| imada-city-night.jpg / full | full | 0.1 / 30.0 / 83.6 | 83.1 | 30.8 | +7.9 / -21.0 | 1.45% |
| imada-city-night.jpg / neutral-candidate-lit-building | 0.125,0.58,0.151,0.61 | 13.0 / 21.0 / 44.4 | 30.3 | 17.6 | +2.5 / -17.0 | 0.00% |
| imada-city-night.jpg / dark-hair | 0.58,0.125,0.62,0.18 | 0.0 / 0.6 / 35.3 | 35.2 | 16.2 | +2.3 / +3.3 | 0.00% |
| imada-city-night.jpg / skin | 0.65,0.316,0.68,0.358 | 62.3 / 74.0 / 84.6 | 18.0 | 23.8 | +18.9 / +14.9 | 0.00% |
| imada-city-night.jpg / sky | 0.02,0.01,0.34,0.17 | 11.2 / 21.6 / 28.9 | 14.9 | 36.5 | +9.0 / -35.3 | 0.00% |
| umezawa-blue-bokeh.jpg / full | full | 10.7 / 18.8 / 67.2 | 55.5 | 17.3 | -1.5 / -10.9 | 0.00% |
| umezawa-blue-bokeh.jpg / neutral-candidate-rail | 0.67,0.923,0.88,0.935 | 10.5 / 16.9 / 34.8 | 23.3 | 10.7 | -5.7 / +0.1 | 0.00% |
| umezawa-blue-bokeh.jpg / dark-hair | 0.27,0.24,0.32,0.265 | 12.4 / 17.8 / 31.2 | 17.8 | 5.4 | -1.9 / +2.9 | 0.00% |
| umezawa-blue-bokeh.jpg / skin | 0.416,0.327,0.461,0.367 | 74.0 / 77.6 / 82.5 | 7.5 | 16.3 | +7.8 / +14.1 | 0.00% |
| umezawa-blue-bokeh.jpg / sky | 0.04,0.02,0.92,0.16 | 23.3 / 29.9 / 33.0 | 8.2 | 40.4 | +6.3 / -39.3 | 0.00% |
| kaki-sunset.jpg / full | full | 22.6 / 86.1 / 97.4 | 44.3 | 33.0 | +4.6 / +25.9 | 15.08% |
| kaki-sunset.jpg / neutral-dress | 0.48,0.6,0.56,0.65 | 31.2 / 65.8 / 70.7 | 30.3 | 28.6 | +12.1 / +28.1 | 0.00% |
| kaki-sunset.jpg / dark-hair | 0.58,0.43,0.61,0.47 | 10.7 / 15.0 / 19.7 | 8.0 | 19.7 | +14.1 / +12.0 | 0.00% |
| kaki-sunset.jpg / skin | 0.528,0.412,0.562,0.437 | 28.4 / 48.6 / 61.9 | 25.2 | 45.4 | +24.3 / +37.8 | 0.00% |
| hobby-cto.jpg / full | full | 0.0 / 12.3 / 73.2 | 73.1 | 20.3 | +0.3 / -11.6 | 1.46% |
| hobby-neutral.jpg / full | full | 0.2 / 15.3 / 63.8 | 62.1 | 7.0 | -0.2 / -4.1 | 2.51% |

Recipe interpretation: C0 warm low-spread sunset, keep skin highlights; C1 moderate spread/muted colour with warm skin against cool water; C2 dense black hair/high-spread city with bright face; C3 moderate spread, pale dark hair/cool city and lower skin chroma. Every prescription stays **estimate**: measured Lab does not identify a Fuji simulation, a numeric WB, a tone curve or a tested exposure. C1 changes the reference's purple dusk toward a blue harbour intentionally. C3's hair is comparatively light but does not prove a raised black curve; Shadows−1 cannot raise black floor.

## Searches and exclusions

- Commons searches included `Tsim Sha Tsui Victoria Harbour sunset`, Octoberbluehour, waterfrontSalisburyRoad and dated evening. Broad “Victoria Harbour” results included Canada/Scotland and unlocated boats; discarded.
- `HK TST Waterfront Platform Salisburg Road Garden Evening.JPG`,2009-10-07 17:18 (Kaohsen), museum landward image: old pre-renovation façade/layout, excluded from current location cards.
- Romain Pontida2014-05-24 19:52 six-frame harbour panorama: May season and stitched landscape,16.7MB, excluded from October single-frame exposure target. No additional panorama dependency.
- Modelpress searches: `金川紗耶 写真集 夜景`, `金川紗耶 フォロワー`, `梅澤美波 夜景`, `梅澤美波 フォロワー`, `梅澤美波 写真集 Twitter`, `梅澤美波 Instagram 万`, `今田美桜 写真集 夜景`, `新木優子 honey`, `新木優子 写真集 夜`, plus 山本舞香/久間田琳加/橋本環奈 photo-book searches. Searches are discovery, not evidence.
- Umezawa SonyMusicShop back cover in the same2026 article: white dress/flowers on daytime cliff, excluded. The **ordinary-edition nighttime back cover** was inspected and selected instead.
- Hashimoto Kanna KALEIDOSCOPE2024 pink-dress Sample-watermarked curtain portrait: indoors/soft window light, does not transfer to this kit at harbour night; excluded, no watermarks removed.
- Araki Yuko: [2019honey announcement](https://mdpr.jp/news/detail/1872599) says Instagram>3million and age25/non-no fashion model; [2024-09-04 profile](https://mdpr.jp/news/detail/4367876) says>5million. Valid historical individual metrics, but inspected article candidates involve indoor/bed/daytime or thermal-spring settings with no matching harbour-night scene, so not added solely for her following. [honey2019-10-21](https://mdpr.jp/news/detail/1885194) describes Instagram poll-winning cover, but vote total absent and the cover's light is not this night plan.
- Strobist2006sunset tutorial features a child and modifiers; not used as adult female style imagery. 2017ChinaBall/forest example uses three lights, excluded for kit mismatch. ShelleyGuy dock sunset photo is not EastAsian, unnecessary beside the matching female portrait references.
- Doubled full+halfCTO stack, cardboard snoot, stand, softbox, ND, grey card and spare power accessories: not required in user kit. Old draft's arbitrary45°lamp1m/camera3m solo geometry and rear-rim baseline were replaced.
- No exact reference exists here for harbour reflection/intentional camera-drag with this subject and kit; these are clearly labelled experiments using C1/C2 colour from real references. No generated concept or fabricated photographic evidence was added.

## Remaining physical uncertainties

Shoot date, X5's system suffix, model preference/fit, actual light-to-face distance/output, gel neutrality, diffuser co-fitting, battery state and local weather/crowds require user-equipment/onsite observation. These do not block a reviewable guide. Before shooting: fire the actual shutter at1/125s, verify power changes in two photos, compare no-flash/flash face and sky, then lock WB. Only real test images can turn prescription lines into `tested`.

## Website validation

- Headless Chromium/Playwright at **320×780,390×844,1440×900**: six scene tabs; independent portrait filters(all4,sunset1,night3,actress1,fashion1) and diagram filters(all3,position2,motion1); all12 photos/diagrams and lightboxes; button/backdrop/Escape closing, keyboard activation, focus restoration and body-scroll release.
- Scene and recipe links reveal filtered-out portrait cards; click and native hash changes both verified. All4 full recipes have15 lines each and per-line estimate labels.
- Print displays all6 scenes and all4 portrait cards, hides floating controls. No page-wide horizontal overflow; long tables scroll within their cards. Mobile hero/flash/reference screenshots inspected.
- Root has2 guide cards. Existing Clear Water Bay five scene tabs, filters(all6,beach5,park3), lightbox and legacy `/#reflib` forwarding still pass. Shared CSS/JS and old guide files unchanged.
- **36 local HTTP resources** successful; local file links, fragments and unique IDs checked. All12 provenance hashes/dimensions verified; SVGs parsed; photograph files inspected and Pillow-verified. Stored Kaki bytes equal the earlier original exactly.
- Strict JSON parsing passed for sources and measurement files (no NaN/Infinity). Each photographic portrait has credits, source link, full recipe, measurements and limitations.
- Official Godox product, Fujifilm screen setup and external-flash pages rechecked: HTTP200.
- `git diff --check` and JavaScript syntax checks passed. No site build step/package installation required, no deployment performed.

These checks validate the website and evidence records. They do not test flash output, gel response, a camera preset against an actual RAW, or the location on shoot day.

## Preview path diagnosis and export

2026-10-03: reproduced unstyled output when a server exposes only `victoria-night/`. The page's `../assets/guide.css` and `../assets/guide.js` resolve to `/assets/…`, return404 and leave default Times New Roman typography/block navigation. This reproduces a missing-asset preview failure; the user's exact preview host was not established.

Rechecked the canonical full-repository server at320,390,1440px: stylesheet loaded with text/css, navy body colour, flex navigation, correct typography/card geometry, working scene/filter/lightbox controls and no horizontal overflow. Trailing-slash routing verified. Shared assets are tracked and included in the Vercel static site; `.vercelignore` excludes `.claude/` and the new Python preview utility, not site assets. This supports deployment readiness but is not a claim that production was deployed or inspected.

`scripts/export-preview.py` generates an HTML-file-viewer preview outside the repository, embedding shared CSS/JS and unchanged source image bytes. Offline browser rendering at320,390,1440px passed: all6 scenes, both filter groups, all12 images/lightboxes and hidden-reference links, with zero HTTP requests. Embedded-image SHA-256 values matched all12 provenance entries. Mobile screenshot inspected. Site/document hyperlinks point to canonical website URLs and require publication; in-page controls work offline. Python syntax and whitespace checks passed. The exported preview is not published or a replacement for the canonical page.

## Screenshot-confirmed viewer issue

2026-10-03: user supplied a screenshot of the `victoria-night-preview.html` file tab displaying literal `<!DOCTYPE html>`, tags and CSS as formatted text. This confirms an **HTML source viewer**, not a browser with a CSS failure. The earlier wrong-root404 reproduction remains a valid separate scenario, but it was not the cause shown in this screenshot. Self-contained HTML does not turn that source viewer into a web browser; export documentation was corrected accordingly.

Rendered browser PNG exports and a complete26-page A4 PDF were generated outside the repository for actual visual review. The PDF includes all6 setup panels and all4 portrait references/recipes; all12 original image assets were loaded before capture. Print styling now gives body/reference text, recipe blocks, summary tiles and hero counters readable contrast on white, without changing the dark on-screen theme. PDF text extraction verified the beginner instructions, four subjects, recipesC0–C3 and creative setups. Browser captures showed no failed resources or JavaScript errors. PNG/first-page PDF previews were visually reviewed. No deployment was performed. File-viewer screenshots/PDFs are static review artifacts, not an interactive hosted website.
