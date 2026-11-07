# 香港公園清新人像：研究與圖像紀錄

**現行行程（2026-11-07 更新）：2026-11-08 12:00 太古廣場集合，15:20 停拍、15:30 前收拾好；13:50 小休時決定，14:10 後可選亞洲協會替換溫室。2026-11-02 的 11:00–14:30 版本記錄保留在下文。以下原有午後／日落計算保留作研究歷史，不再是本次行程。**

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


## 2026-10-31 update — 圖片優先、水框姿勢

使用者要求社媒參考直接顯示照片，不展示選圖原因；依其明確要求移除可見的長篇理由、配方與來源查核分析，保留圖註作者、圖片／原帖連結，研究移至此檔。新社媒相簿8張，包含IG創作者公開媒體引用與XHS媒體圖輯，沒有把AI當作社媒真照。少量選圖而非整本相簿，下載的公開預覽保留原始bytes、任何水印、尺寸和SHA256，出處記錄於image-sources.json。未宣稱取得一般再利用授權，亦沒有移除水印。

新來源：UHK 2023-06-03〈金鐘城市綠洲香港公園〉，文章列IG @thehkcouple授權引用，選3張公園取景（白橋、岩壁通道、白柱走廊）；這個媒體授權不等同本網站取得獨立授權。am730 2026-04-22 圖輯，選龔嘉欣 @kungkaty站姿及坐姿各1。WONEDERLUST本人公開旅遊頁及連結的同名IG帳戶，1張水簾內平台站姿；照片檔名提示2018-12-08但不作已證實拍攝日。兩張XHS轉載景物圖仍採UHK共同作者歸屬，不硬指派單張作者。以上均不作流量證據，不將帳戶連結說成已確認單篇。

重要更正：香港公園環形水簾有可入內的看台及踏步，原指南只建議外側步道過於狹窄，已改為可在當日開放及路面情況容許時進入看台停定拍攝；不鼓勵站在水流下淋水或在濕踏步跑跳。[官方噴泉廣場](https://hkp.lcsd.gov.hk/tc/facilities/fountain-plaza)水簾09:00–18:00，保養為每月最後星期二及三（假期順延），11月8日星期日不在例行保養日，但現場封閉仍優先。

真正「水框」是從環形水簾入口缺口望向中央看台：左右流水、上方金屬框／玻璃頂骨架、後方中央柱與圓凳，不是人造長方形瀑布。確認自Commons真照及官方設施描述。新姿勢配6個獨立虛構成年人示意，精確輸入和生成檢查另記來源JSON。


水框生成完成：3次生成、3張雙圖接受、0次重生成、0張拒收；共6個新姿勢。輸入為HK Arun（2011-01-20 EXIF15:04）CC BY-SA3.0與Thomas Au（2015-02-28 16:44）CC BY2.0的同一噴泉入口真照，非他人的人像風格模仿。幾何可辨認：弧形金屬頂、三角鋼架與玻璃頂、中央柱、原有圓凳、內側平台及入口踏步。人體可見手指／肢體檢查合理、未讓人物在流水下淋水、未跳躍。部分站姿接近入口邊，文字統一指示站入平台內側、入口只通行；構圖不承諾像素級建築與人流。色彩以真照植被作視覺與近似crop比對（water-frame-measurements.txt），無幻想綠或金色光束，AI不作調色目標。全部新PNG unchanged copy保留metadata，授權改作採CC BY-SA4.0。

原參考區的「選圖理由、測量、不能做到、長篇熱度核實」已依使用者要求移出前台，保留本檔及來源JSON。卡片僅標圖題、作者／原帖、照片來源及短姿勢提示。不顯示沒有實際圖片的Tatler／木屋候選；也沒有把攝影師網站混合其他公園的圖冒充同一機位。

驗證（本次更新）：首頁及指南本地連結／錨點、25個圖片檔SHA256通過。Chromium驗證8張真照、6個水框Pose、5/6/2/8張的水景/IG/XHS/全部篩選、鍵盤與滑鼠放大、原有場景tabs、320/390/1440px無水平溢出及無JS錯誤；已查看手機版真照相簿和水框區截圖。共享CSS／JS未改動。

## 2026-11-02 update — 11:00–14:30 行程與亞洲協會可選站

使用者改為約11:00太古廣場集合、14:30前拍完，新增亞洲協會真實參考；並補充這次屬私人、非商業用途。主線保留水框與白橋，12:50小休，13:10後選溫室／綠蔭或亞洲協會，14:20停拍留10分鐘收拾。亞洲協會替換尾段，並非額外塞入主線；由公園前往正義道預留15–20分鐘步行及上坡是行程估算，並未現場計時。若到場才得知不能拍，直接提早收工，沒有安排趕回公園。11:30–14:20光線建議改為完整陰影與臉向明亮天空，不再等待日落／低角度金光。既有AI概念生成prompt與歷史太陽計算保留原始紀錄，不能當成新午間行程的光線保證。

### 亞洲協會真實場景證據

先檢視5張Commons照片，採用3張不同背景，全部保留來源提供的960px預覽原始bytes；授權、SHA256和尺寸加入image-sources.json。圖片不是AI，也不是模特姿勢實拍；A1–A3是編輯提出的姿勢與鏡頭起點，並非原攝影者設定，亦不宣稱熱門。

| 本地檔案／來源 | 日期與作者／授權 | 能確認／不能確認 |
| --- | --- | --- |
| [scene-asia-walkway.jpg](https://commons.wikimedia.org/wiki/File:Walkway_at_the_Asia_Society_Hong_Kong.jpg) | 2016-11-17 12:24:14，來源EXIF及描述；Nick-D / CC BY-SA 4.0 | 11月午間歷史實景：玻璃欄杆、上層橋板、樹林與地面光斑；位置22.275940,114.165329。相機時鐘未獨立校準；不是2026天氣、可進入範圍或人流保證。 |
| [scene-asia-stone-wall.jpg](https://commons.wikimedia.org/wiki/File:Former_Explosives_Magazine_of_the_Old_Victoria_Barracks_Magazine_A_01.JPG) | 2012-05-05 16:58:23，來源描述及EXIF；Tksteven / CC BY 3.0（擇CC授權） | Magazine A石牆、大門、消防栓及庭院；只作建築背景參考。5月下午不能代表11月午間採光，勿阻門或消防設施。 |
| [scene-asia-entrance.jpg](https://commons.wikimedia.org/wiki/File:Asia_Society_Hong_Kong_Center_Entrance_2021.jpg) | 摘要April 2021；EXIF 2021-04-10 15:05；Wpcpey / CC BY 4.0 | 正義道入口簷篷、前地、灰牆和高樓，位置22.275558,114.165100。只核對建築與入口方向，不代表11月光線或入口可佔用。 |

另外檢視Wpcpey的2016-03-25天橋及2021-04-10 Yasumoto Bridge照片，幾何一致；為免重複同一橋景，未另存網站。天橋示例地面有斑駁硬光，故拍法明確要求在無臉部光斑的位置停步，沒有宣稱全橋均勻柔光。石牆和入口的75mm半身構圖屬建議，須按實際可站位置調整。

### 開放與私人攝影查核（2026-11-02）

- [香港旅遊發展局場地頁](https://www.discoverhongkong.com/eng/place-to-go/travel.guide-asia-society-hong-kong-center.html)與[政府電影場地庫](https://fpf.ccidahk.gov.hk/en/location/detail.php?id=1746)確認9 Justice Drive、歷史軍火庫與新舊建築／兩層天橋。場地庫列聯絡2103 9511、External Affairs；正式外景拍攝書面申請平均2週，收費按個案。這是外景場地資料，不能由此推論一般遊客拍照也須租場、投保或繳費。
- [中心官方GlueUp展覽頁](https://asiasocietyhk.glueup.com/event/mother-exhibition-curator-led-guided-tours-191234/)列m<other>光影廊道2026-10-09至11-08、週二至日11:00–18:00、Lighting Passage、免費入場。頁首sold out與票種指10月17／24日導賞，未當作11月8日一般入場售罄。只在指南標為該展覽時段，不將它擴大成全場開放或拍攝許可；當日展覽也可能增加人流。
- 官方主站visit頁無法存取，未聲稱讀過現行全場訪客守則。商店網站營業時間不能推論全場時段。OpenHouse2025活動日程及2012開幕資料不當成2026現況。
- 政府場地庫連結的[Filming and Photography Guidelines PDF](https://fpf.ccidahk.gov.hk/sc/forms/ASHK_App_EC.pdf)實際頁腳為July 2014，不能把搜尋引擎近期收錄時間當作新規日期。文件有正式攝影申請（10工作天）且未明列私人非商業隨拍豁免；scope及definitions主要描述影視／攝影製作，同時申請段用語廣泛，無法據此確定一般遊客手持相機人像的適用範圍。因此前台標為「規定待確認」，不斷言私人隨拍一定需正式申請，也不保證私人非商業用途必定免申請。
- 搜尋涵蓋Asia Society Hong Kong Center personal/non-commercial photography policy、官方域名personal/commercial/flash與中文私人／人像攝影。第三方旅遊頁及訪客評語提到一般無閃拍照，但沒有可核實的現行官方豁免條文，未用作免申請證明；其他城市／機構的museum photography政策不適用。
- 可由使用者先致電或入場時向接待處確認兩人私人手持相機人像，以及閃燈／反光板能否使用；此可選站先按自然光計劃。未代使用者發送任何訊息或申請，亦沒有把場地確認變成部署本網站的前置批准。

### 本次驗證

本地驗證通過：4頁HTML的本地連結／錨點與重複ID、28個圖片檔SHA256及尺寸、舊行程時間移除、新行程與可選分流。Chromium以GitHub Pages子路徑驗證320／390／1440px無水平溢出、全部圖片載入、亞洲協會3張放大及Escape關閉、原有水景／IG／XHS／全部篩選5／6／2／8張、午間晴天tab、首頁新時間；沒有JS錯誤或HTTP失敗。已檢視390px行程與亞洲協會截圖。沿用共享CSS／JS，沒有變更其他指南內容。

## 2026-11-05 update — 使用者指定的兩篇小紅書逐圖拍法

使用者提供兩個連結，要求按其中照片增加拍攝指南；沿用其先前偏好：顯示照片與簡短拍法，前台不放選圖理由、數據分析或長篇熱度論述。新區放在原有靈感相簿前，7組公開預覽原圖可放大、按兩篇篩選；每組附對應香港公園站位、XF23mm／Viltrox75mm起點、姿勢及廣東話口令，較長的取景／對焦細節收在details。沒有生成新AI人像。

### 原帖與取用紀錄

| 使用者連結／原帖ID | 公開署名、發佈時間（HKT） | 所選原帖圖序／用途 |
| --- | --- | --- |
| [8nNemu4h5jP](https://xhslink.cn/o/8nNemu4h5jP)／6ae312210000000002037e7f | 發佈者💤mmm，《捞捞香港深圳互勉摄影师！》，2026-10-29 17:30:09；原帖是邀約攝影師合作的公開作品集，提到與不同攝影師合作，未逐張列攝影署名 | 圖1→X1側臉／花束（原拼圖2格）；圖2→X2回望／撥髮（原拼圖3格）；圖5→X3手部／胸前手勢（原拼圖4格）。只選3/7個原圖檔，不整篇複製。 |
| [8o6jXzqn9mx](https://xhslink.cn/o/8o6jXzqn9mx)／6aec0898000000001402ab53 | 發佈者五月，《互勉｜听风动》，2026-11-05 12:39:52；公開人像作品，依原帖署名，不另外推測被攝者身分 | 圖1→X4坐下抬眼；圖2→X5長椅側靠；圖3→X6手搭肩前；圖5→X7風吹髮。只選4/6張，不整篇複製。 |

發佈時間來自公開分享頁time欄位轉換，不是照片拍攝時間。兩篇皆未確認拍攝地點、原始相機／鏡頭／曝光，不能因背景有綠地、湖面或長椅就宣稱香港公園實拍。原帖人物也不等同本次模特；本次只借鑑姿勢、光線方向及構圖，沒有做身分辨識或拿照片生成新人物。

一般桌面入口會導向登入；兩篇官方手機分享頁則直接回HTTP200並帶原帖及圖片資料，無須登入。使用正常手機網頁入口讀取公開內容，沒有使用帳戶cookies、登入、驗證繞過或第三方付費抓取服務。檔案使用公開頁實際提供的H5_DTL預覽URL，以HTTPS取得原始bytes，保留小紅書水印及作者既有拼圖版式，沒有裁剪、調色、拆分或清除水印。CDN網址可能時效到期，網站展示使用本地檔案；原帖仍連使用者提供的短連結。

7個檔案完整來源、發佈者、原帖圖序、日期、尺寸及SHA256已記入image-sources.json；版權仍屬原創作者，不宣稱CC或其他一般再利用授權。第一篇公開分享頁資料於2026-11-05顯示92讚／8收藏，第二篇欄位空白；此為單次資料快照，不作「熱門」判定，前台依使用者要求不顯示熱度分析。

### 對應現場與取景限制

- 真實公園環境沿用原有11月噴泉、人工湖及溫室證據，不新增未核實的草地或湖邊站位。X1／X2可用公眾步道，以75mm收窄綠葉背景或23mm保留白橋；不要求重現原帖大片草坡。X3只借胸前手勢，未要求到水邊俯身；暖逆光與霧感不是本次午間光線保證。
- X4／X5只有遇到合適、乾爽、空置的公眾座椅才拍，沒有定位或保證與原帖同款長椅；X5可略過，X4可改站姿，不把欄杆當椅面。X6／X7可用原有樹蔭或獲准的溫室公開步道；以臉朝明亮天空及較暗綠葉背景作起點。
- 建議距離按景別估算：75mm肩上／近鏡約1.5–2.5m、半身約3m；23mm帶環境約2–3m，坐姿與椅子約1.5–2m。這些不是原帖EXIF，也沒有實機試拍。風吹髮用1/800–1/1000s、AF-C近眼，長椅靜態1/320–1/500s；以現場光線與模特舒適度微調。
- 花束、花瓣、淺色披肩皆為可省略道具；可自備，不採園內花葉，也不要求換成原帖相同衣服。7組起手按自然光安排，沒有推測原帖是否用了閃燈。
- 行程時間維持11:00太古廣場集合、14:20停拍、14:30前收好。先挑3款替換原時段姿勢，水框仍優先；13:10後若改去亞洲協會，只在職員容許的地點拍適用近鏡，沒有增加新必到站或保證長椅。

### 色彩量測與參數信心

本次新增的是原圖拍法，沒有另造一套「原作者配方」。色彩連到既有完整C1／C2，仍為未實機測試的estimate；沒有宣稱精準匹配新照片。原圖有拼圖、局部調色及不同光線，全幅偏綠不等於白平衡偏綠。量測全檔、分格及無水印的白衣／膚色／頭髮分析窗，詳見[xhs-reference-measurements.txt](xhs-reference-measurements.txt)；分析窗不會改動網站圖片。

- X2上格（crop 0,0,1,0.325）：L* p5/p50/p95約15.6/56.1/96.1，跨度80.5；不能把大片綠地的全幅a*當膚色或WB目標。
- X2白衣（crop 0.55,0.24,0.60,0.28）：L*中位88.5，高光a*約−4.2／b*−1.3；X3右下白衣（crop 0.70,0.90,0.74,0.94）：L*中位89.2，高光a*約−1.2／b*+5.6。兩者光線／處理不同，不用一個WB偏移硬套整篇。
- X7全幅：L* p5/p50/p95約14.1/57.8/94.7，跨度80.6，chroma中位4.5；這是該低彩度預覽的數值，含背景與水印，不代表所有膚色低彩度。X7膚色窗（crop 0.40,0.35,0.45,0.39）及X1黑髮窗另留原始量測，不當成已校準色卡。
- 新卡片所列光圈／快門／距離均為本指南建議。沒有試拍，未使用tested標記；低角度逆光、光暈、抬黑位或選擇性膚色仍靠現場光與RAW後製，不由Fujifilm配方保證。

### 本次驗證

4頁HTML本地連結／錨點、重複ID及35個圖片檔SHA256／尺寸通過。Chromium用GitHub Pages子路徑驗證320／390／1440px無水平溢出、所有圖片載入；新增兩篇篩選3／4／7組與原有水景／IG／XHS／全部篩選5／6／2／8張互不干擾。7張按鈕以滑鼠或鍵盤開放大圖、Escape關閉、7個細節展開均正常；11:00–14:30行程、8段時間軸及亞洲協會3張實景仍在，首頁摘要更新。沒有JS錯誤或HTTP失敗。已檢視390px的X1、X5、X7原圖與口令卡片截圖；共享CSS／JS及其他兩份指南未改動。


## 2026-11-07 update — 12:00 集合、每站只換一次鏡、插畫地圖

使用者改為約12:00太古廣場集合，要求避免同一站內來回換鏡（每站最多換一次），並希望指南在現場更易查閱。全部行程時間順延1小時：12:30水框、13:20白橋、13:50小休、14:10溫室或亞洲協會、15:20停拍、15:30收好。

- 鏡頭次序：噴泉23→75、白橋75→23、溫室／亞洲協會23→75。上一站最後用的鏡就是下一站第一支，步行途中不用換。白橋改為先拍75mm（X2、08、04）再換23mm拍03；溫室06位若退不到3m，在23mm段先拍半身作後備，不再換回。
- 插畫地圖：OpenStreetMap Overpass取得公園步道、水體、建築及Asia Society範圍（© OpenStreetMap contributors，ODbL），再以等距長方投影（每度約103,040m經向、110,750m緯向）手繪化重畫。太古廣場→噴泉廣場約350m、白橋→亞洲協會約800m，為OSM步道網絡Dijkstra最短路徑（樓梯權重×1.6）估算，未經現場計時。
- 約位／示意：圓形水簾入口缺口方向（按步道接近方向推斷為東南）、假山瀑布（湖的源頭西端）及溫室內部花槽／圓柱位置均未有平面圖核對，地圖及卡片已標明以現場為準。
- 太陽位置：以低精度太陽位置公式（Astronomical Almanac近似）計算22.277N、114.163E於2026-11-08 HKT：12:30方位189°／高51°、13:30 209°／46°、14:30 225°／38°、15:00 231°／33°、15:30 236°／27°。溫室約12m高，14:00後東北面步道入陰影為按此推算，未計樹木遮擋。
- 機位扇形：23mm／75mm在APS-C水平視角約54°／18°。
- 天氣：香港天文台九天預報（11月7日查閱）11月8日大致多雲，有陽光時段，早上一兩陣微雨，25–29°C。
- 剔選紀錄只存在瀏覽器localStorage（hkp-shots-1108），不上傳。
