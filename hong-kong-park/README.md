# 香港公園 · 清新女生人像

2026-11-08（星期日），11:00太古廣場集合，14:20停拍、14:30前收工。X-T5、XF23mm F1.4 WR、Viltrox75mm F1.2；Godox iT32/X5-F可選。

主線：水框 → 白橋 → 小休 → 溫室／樹蔭。13:10後可改去亞洲協會，替換溫室段；附3張可放大的真實場景照片與姿勢建議。私人輕裝人像拍攝規定尚待中心確認，不把正式場地申請文件當作遊客拍照的確定規則。

Live: https://jessepcc.github.io/clear-water-bay-shoot-guide/hong-kong-park/

從repository root運行`python3 -m http.server 8000 --bind 127.0.0.1`，開http://127.0.0.1:8000/hong-kong-park/。

- [指南](index.html)：8張真照參考、6個新水框Pose（AI示意）、原有8個方案、2套完整富士配方、反光板與閃燈判斷。
- [研究紀錄](research-notes.md)：IG/XHS來源與讀取限制、未核實熱度、排除的機位。
- [影像來源](image-sources.json)：授權、日期、雜湊、生成prompt；真照與AI分列。
- [量測](reference-measurements.txt)：真實預覽及概念色度檢查；AI不是調色目標。

社媒參考全部標明核實程度，沒有可驗證的單帖讚藏數；不宣稱為熱門榜。配方均為未實機測試的estimate。

離線export：`python3 scripts/export-preview.py hong-kong-park --output /tmp/hong-kong-park-preview.html`。
