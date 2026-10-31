# 香港公園清新人像：研究與圖像紀錄

查核：2026-10-31。用戶要求：11 月 8 日香港公園、1 位年輕女生、清新風格；X-T5、Viltrox 75/1.2、XF23/1.4 WR，可帶 Godox iT32，詢問是否帶反光板。依目前日期採 2026-11-08（星期日）；模特年齡未知，AI 示意人物一律虛構成年女性，不使用實際模特照片。

## 完成範圍與未解決限制

- 加入 /hong-kong-park/、首頁卡片與 README；沿用共享 CSS/JS，沒有框架或 build。
- 3 個主要場景，每場 3 張真實照片；6 幅 AI 人像（3 張雙圖）與 8 個文字拍攝方案。
- 尋找過 Instagram / Xiaohongshu 真實原帖。找到可追溯單篇 ID、媒體作者歸屬和同地成人作品，但未能核實任何適合本次主題的單帖讚／收藏數。因此「popular」部分未能證實，頁面明確標示為編輯精選／無熱度數據，沒有補造數字。
- 兩套完整 X-T5 配方均為 estimate，未有實機試拍，不是參考作者設定。AI 圖不作調色目標。

## Scene evidence

三個核心場景均先建立真照，再找人像參考。照片來源、日期、授權、尺寸、SHA256、位置確認及 source-served image URL 詳列 [image-sources.json](image-sources.json)。下列非 11 月照片只補充幾何；不是 11 月色彩或即時設施證據。

| 檔案 | 拍攝日期／時段 | 作者／授權 | 確認位置與用途 |
| --- | --- | --- | --- |
| [images/scene-pond06.jpg](https://commons.wikimedia.org/wiki/File:HK_%E4%B8%AD%E7%92%B0_Central_%E9%87%91%E9%90%98_Admiralty_%E9%A6%99%E6%B8%AF%E5%85%AC%E5%9C%92_Hong_Kong_Park_waterfall_pool_November_2022_Px3_06.jpg) | 2022-11-27 11:05:16 | SUAXINGPWOO Kaliu / CC BY-SA 4.0 | Circular water curtain, white building left, curved public path right; same landmark as LCSD Fountain Plaza. November outdoor season evidence. Daylight; weather not recorded. |
| [images/scene-waterfall02.jpg](https://commons.wikimedia.org/wiki/File:HK_%E4%B8%AD%E7%92%B0_Central_%E9%87%91%E9%90%98_Admiralty_%E9%A6%99%E6%B8%AF%E5%85%AC%E5%9C%92_Hong_Kong_Park_waterfall_pool_November_2022_Px3_02.jpg) | 2022-11-27 11:04:30 | SUAXINGPWOO Kaliu / CC BY-SA 4.0 | Circular curtain behind symmetric stepped stream, pale tiled walls and two bowl fountains; same Fountain Plaza. November season evidence; not the artificial-lake rock waterfall. |
| [images/scene-fountain2008.jpg](https://commons.wikimedia.org/wiki/File:Hong_Kong_Park_large_fountain.JPG) | 2007-05-22; local time unknown | BrokenSphere / CC BY-SA 3.0 | Historical Fountain Plaza geometry only. May photo is not November colour or current facilities evidence. |
| [images/scene-rockfall2020.jpg](https://commons.wikimedia.org/wiki/File:HK_ML_%E5%8D%8A%E5%B1%B1%E5%8D%80_Mid-levels_%E5%A0%85%E5%B0%BC%E5%9C%B0%E9%81%93_Kennedy_Road_%E9%A6%99%E6%B8%AF%E5%85%AC%E5%9C%92_Hong_Kong_Park_flora_green_leaves_February_2020_SS2_05.jpg) | 2020-02-13 15:21:56 | Sumiouyat Yee / CC BY-SA 4.0 | Curved white balustrade, rock waterfall, stone retaining cylinder and overhead bridge. February photo used for architecture and safe walkway geometry only. |
| [images/scene-rockfall2010.jpg](https://commons.wikimedia.org/wiki/File:Hong_Kong_Park_%E9%A6%99%E6%B8%AF%E5%85%AC%E5%9C%92_%285292020463%29.jpg) | 2008-11-30 15:53 | InSapphoWeTrust / CC BY-SA 2.0 | Artificial-lake waterfall, white balustrade, frog sculptures and visitors. Date is 2008-11-30, not 2010 (numeric suffix in local ID is not capture year). November vegetation and crowd evidence; not an exact 2026 forecast. |
| [images/scene-rockfall.jpg](https://commons.wikimedia.org/wiki/File:Hong_Kong_Park_waterfall.JPG) | 2007-05-22; local time unknown | BrokenSphere / CC BY-SA 3.0 | Rock cliff and overhead bridge match LCSD Artificial Lake and 2020 photo. Geometry only; May not used for November colour. |
| [images/scene-humid32.jpg](https://commons.wikimedia.org/wiki/File:Humid_Plant_House_-_Hong_Kong_Park_Conservatory_-_IMG_9832.JPG) | 2011-02-21; EXIF 01:32:00, local time unreliable | Daderot / Public domain | Glass roof lattice, pale structural column, broad leaves and curved stone planter identify Humid Plant House. EXIF clock conflicts with daylight; do not assert night opening. Climate controlled year-round; historical planting only. |
| [images/scene-humid34.jpg](https://commons.wikimedia.org/wiki/File:Humid_Plant_House_-_Hong_Kong_Park_Conservatory_-_IMG_9834.JPG) | 2011-02-21; EXIF 01:33:01, local time unreliable | Daderot / Public domain | Same conservatory roof, labelled plants and stone planter; supplemental historical layout, not current exact plant placement. |
| [images/scene-humid37.jpg](https://commons.wikimedia.org/wiki/File:Humid_Plant_House_-_Hong_Kong_Park_Conservatory_-_IMG_9837.JPG) | 2011-02-21; EXIF 01:35:27, local time unreliable | Daderot / Public domain | Interior humid-house rock waterfall; not the exterior artificial-lake waterfall. Supplemental indoor plant context only; no model is placed on this rockwork. |

室外 November 基準：噴泉 2022-11-27 上午、人工湖 2008-11-30 下午。水面灰綠／灰藍，葉叢有明暗與黃綠差別，不是清一色青綠；11 月噴泉照片沒有媒體預覽同量的粉紅花。歷史照片中的樓宇、路燈、白牆、告示牌及遊人不能假裝消失。白橋與圓形水簾是不同設施。

溫室 2011 年照片只確認架構。官方說濕地植物室全年 23–33°C，故可用作全年室內環境的歷史線索，但不能保證植物排列。EXIF 的 01:32–01:35 與採光不符，標當地時段未知，不能推論凌晨開放。

### 官方核對（2026-10-31）

- [LCSD Visit](https://hkp.lcsd.gov.hk/en/visit)：戶外06:00–23:00；溫室及觀鳥園09:00–17:00，免費；金鐘 B/C1、中環 J2/K；沒有園內公眾車位。頁面修訂2026-10-21。
- [官方地圖](https://hkp.lcsd.gov.hk/en/map)及[設施](https://hkp.lcsd.gov.hk/en)：圓形噴泉廣場、人工湖岩壁瀑布、溫室位置與設施名稱。
- [溫室](https://hkp.lcsd.gov.hk/en/facilities/conservatory)：玻璃頂、濕地植物室氣候與天氣關閉條件。頁上 Close 是當時狀態，不能當成11月8日停開公告。
- [藝趣坊](https://hkp.lcsd.gov.hk/en/activities/artscorner)、[2026期新聞](https://www.info.gov.hk/gia/general/202512/30/P2025123000339p.htm)：茶具文物館旁週末及公眾假期12:00–18:00，人流預留。
- [天文台九天天氣](https://www.hko.gov.hk/tc/wxinfo/currwx/fnd.htm)：出發前再查，沒有把估計天氣寫成預報。

## 太陽位置及時間

香港時間 HKT / UTC+8，2026-11-08。日落約17:43，核對 [timeanddate](https://www.timeanddate.com/sun/hong-kong/hong-kong?month=11&year=2026) 與多個香港日照表（差異約1分鐘，站點及折射定義可不同）。HKO 月曆PDF工具讀取到檔案但本機下載無法解析，不用作已核實的分鐘數來源。

以下是 NOAA fractional-year 近似法，座標22.277N,114.162E，方位自正北順時針。公式依 [NOAA solar equations](https://gml.noaa.gov/grad/solcalc/solareqns.PDF)，不是實測、不是建物遮蔭模型：

| HKT | 方位 | 高度 |
| --- | --- | --- |
| 14:00 | 217.9° | 42.5° |
| 15:00 | 231.3° | 32.7° |
| 16:00 | 240.9° | 21.2° |
| 17:00 | 248.2° | 8.6° |

實際園內受光受山、樹和樓宇影響。方案以 open shade / diffuse sky light 作穩妥分支，不保證16:30有斜陽。路線13:30–17:15只為建議，步行時間估算；溫室主拍排15:35–16:15，預留關門緩衝。

## 社媒來源及熱度查核

| 來源 | 證明了甚麼 | 不證明甚麼／處置 | 配方 |
| --- | --- | --- | --- |
| [龔嘉欣香港公園報道](https://www.am730.com.hk/article/1026298), 2026-04-22 | 具名成年女性、同一公園、日間散步照片與留言報道 | 不公布攝影者、器材、讚數；帳戶kungkaty有真實身份，未找到確切單篇ID。只連結，不 rehost、不量測 | C1，全部estimate，獨立起點 |
| [Tatler Hong Kong Park 段落](https://www.tatlerasia.com/lifestyle/travel/best-city-parks-hong-kong)嵌[IG Bs5QtnkDXhO](https://www.instagram.com/p/Bs5QtnkDXhO/) | 真實嵌入的單篇URL與編輯出處Coco Marett | IG fetch throttled，作者、內容、日期、熱度未知；僅 discovery，不當姿勢／調色參考 | 不配方 |
| [小太阳timing 原帖](https://www.xiaohongshu.com/explore/670a40cf000000002401745c)＋[UHK](https://hk.ulifestyle.com.hk/activity/detail/20064146/), 2025-05-11 | UHK列作者與原帖；文章後段噴泉預覽可與Commons圓形水簾／階梯流水核對 | 原帖300031不可訪問；原發帖日、單張歸屬、讚藏未知。媒體列兩個作者但未逐張歸屬；不將流水圖硬歸某一人。不 rehost | C2，全estimate；場景色調量測與設定分開 |
| [笨笨不笨 原帖](https://www.xiaohongshu.com/explore/680c91b0000000001c00d272)＋同UHK | 可追溯原帖ID及媒體署名 | 小木屋／鞦韆無法定位，原帖不可讀；不作場景證據，不稱其已證實為AI或假照 | 不配方；排除機位 |
| [Tracy Wong / Ayumi](https://tracywongphoto.com/headshot-portraits-hong-kong-park-ayumi-suzuki/) | 攝影師原始作品，社交／職業用途的成年女性自然光人像與拍攝說明 | 頁內混合香港公園／長江公園／遮打花園，逐張不明；沒有可核實人氣，不能當IG熱門帖；只連結 | C2，全estimate |

### 搜尋紀錄與排除

搜尋過 `site.instagram.com/p/ "Hong Kong Park" "portrait"`、`site.instagram.com "香港公園" 人像`、`"Hong Kong Park" "instagram.com/p"`、`"香港公園" "instagram" "likes"`、`site.xiaohongshu.com/explore "香港公园" 写真`、`"香港公园" "写真" "小红书" 瀑布`、`龔嘉欣 香港公園 路過 公園 打卡 Instagram`，以及Commons的Hong Kong Park waterfall November / conservatory。

- IG單篇受限，小紅書原帖回傳不可用；沒有繞過登入、刪水印或把搜尋頁假稱原帖。
- 排除九龍公園噴水池范冰冰話題：地點不同。
- 排除童話木屋／鞦韆作必拍：未能定位。
- 排除其他公園、其他城市及來源不明的「清新女孩」聚合圖。
- 排除沒有作者、只有「熱門」敘述或跨平台彙總人次的頁面；Airial的view／like彙總不拿來支持IG/XHS原帖熱度。
- Tatler另有IG B7iqgqfp6HY（觀鳥園），未讀到內容，且不將觀鳥園列人像補光站。
- 一般Instagram／小紅書搜尋詞僅為 discovery terms，沒有將它們計入真實參考作品。
- 木屋圖雖出現在媒體，不代表已確認地點或真實性；不從文章宣傳語外推。
- 原本下載的「path09」其實是鳥類宣傳橫額；path01/02是路旁蕨牆細節，不能代表一條可站模特的林道，已從輸出排除。
- 部分嘗試的 Commons 檔名404，不列為證據；只列成功下載且視覺檢查的9張。

## 真實預覽的量測

UHK公開預覽流水圖：來源 bytes 存於本次 /tmp/hk-xhs/7.webp，只作閱讀分析，未放網站。對應URL記錄於下方；無水印被移除，測量只用內框crop。文章是2025-05-11，照片拍攝日期未知，因此只作可轉用的色彩方向，不作11月季節證據。原檔逐張作者歸屬不明。

- inner frame crop0.05,0.05,0.95,0.95：L* p5=19／p95=93，chroma median7.9，clipped1.8%。
- 白牆crop0.75,0.33,0.85,0.36：亮部a*=+2.6／b*=−3.2，L* p50=87；只說預覽白牆略偏冷，不能反推作者WB。
- 暗樹幹crop0.85,0.04,0.93,0.18：p0.5=8／p5=11／median17；不是標準黑色，不能證實褪黑曲線。
- 沒有主體皮膚可量測；不能以植物綠色推斷臉色。
- 所有配方行均estimate；沒有將從L*讀數映射出的建議假標成實測相機參數。沒有實機test shot，不標tested。
- C1 ASTIA用作膚色及綠葉起點；C2 PRO Neg.Std柔化反差。兩者DR200 ISO≥250，D Range Priority Off。其他參數完整寫在頁面。
- [X-T5官方影像選單](https://fujifilm-dsc.com/en/manual/x-t5/menu_shooting/image_quality_setting/)核對過：ASTIA／PRO Neg.Std、tone curve半級範圍、DR200最低ISO250、DR400最低500。官方2026選單已列REALA ACE，但本指南沒有依賴它。

完整測量輸出見 [reference-measurements.txt](reference-measurements.txt)。這些是網頁重壓縮檔的性質，不是現場的實體色度；不作皮膚美白目標。

## AI 概念圖

以上搜尋沒有找到可直接對應「圓形水簾＋散步/撥髮」「白橋＋停步/回頭」「指定溫室花槽＋慢行/肩上人像」的同背景、光線、姿勢真實人像，因此依專案scene-concept-image skill用授權實景作輸入。

使用 image_gen.imagegen（工具未回報模型版本），生成3次、每次1張雙圖，共6幅構圖。3張全接受，0次重生成／0張拒收。原始PNG unchanged copy，保留工具提供metadata，未重新編碼以避免剝除內容憑證，故比skill建議的640–960px/150KB大。出處、精確prompt、base license、SHA256及人工檢查寫於image-sources.json。AI派生圖水簾／白橋採CC BY-SA4.0；Daderot底圖public domain。

- Fountain：圓形水幕在左、弧形步道在右、背後建築和遊人可辨；人物在乾步道，沒有進水。全身與半身有區分。水印來源原照另完整展示。
- Bridge：白欄杆、石牆圓柱、假山瀑布和高架橋主要結構保留；人物留在鋪面，不坐欄杆；近鏡背景更壓縮。細部非像素級複製，場勘為準。
- Greenhouse：玻璃頂、圓柱、石槽及闊葉可辨，人物在花槽外，不踩植物；室內採柔光而非虛構金光。實際植物和步道空間須現場確認。
- 光線以陰天／開揚陰影分支作示意，不保證當日晴或陰；沒有捏造太陽束或夜燈。
- 人物為虛構成年女性，衣著適合公園，手與肢體人工檢查正常。三組不是實際模特，也不承諾同一真人外觀或服裝細節完全一致。
- 比較真照／概念圖近似植被crop的色度與視覺飽和度，詳測量檔；兩個取景不同，數值不是色彩匹配。無需因不同裁切的綠葉比例差異重生成。AI從不作配方來源。

## 補光查核與實務判斷

[Godox原廠手冊](https://www.godox.com/Downloads/Godox_iT32.pdf)列iT32＋X5-F支援X-T5及TTL/HSS。沒有把用戶「可以帶iT32」當作已擁有X5-F或助手。機械快門MS、1/200s留同步餘量；一般同步上限1/250s核對[Fujifilm flash docs](https://fujifilm-dsc.com/en/manual/x-t5/peripherals_and_options/external_flash_units/)。不用電子快門打一般閃光。

補光TTL−1.3EV、白板60–80cm／0.6–1m、燈距1–1.5m等均是建議起點estimate，不是廠商曝光保證。手動1/128–1/64只作1.5m、F2.8、ISO250、陰影測試，現場重測。HSS減輸出；小罩與向天空跳閃不會產生大面積柔光。單人攝影師＋模特可不帶板；有助手則白面優先。

## 驗證

靜態驗證通過：首頁及3份指南的本地連結、章節ID／錨點、12個圖片SHA256。Chromium經本地HTTP服務驗證通過：320／390／1440px無水平溢出、圖片載入、場景tab、5組參考篩選、滑鼠與鍵盤lightbox開關、打包勾選、無JavaScript錯誤。既有共享CSS／JS未改動。離線export使用專案既有scripts/export-preview.py成功，產物放/tmp，不提交大份export。

量測的UHK來源預覽URL：https://resource02.ulifestyle.com.hk/ulcms/content/article/image/w1280/2025/05/20250509174523_00b67fb4c55eb08a3b586dd5614017b90a884f66.webp
SHA256：070d1ed3813e0a7de2d27e659ff8a7b8f9865b40f997ab34adfd60323c9b8610
