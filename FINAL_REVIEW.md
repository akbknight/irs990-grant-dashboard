# Final Review — IRS Form 990 Grant Analysis Dashboard

## Summary

Interactive dashboard analyzing 9,693,767 grant records totaling $550.2B from IRS Form 990 filings (2019–2024), with focused analysis of Jewish philanthropic giving ($10.6B, 275,446 grants). Built as a self-contained static HTML file with Plotly.js charts and a D3.js US choropleth map. Hosted on GitHub Pages.

---

## What Was Built

### Chart Suite (9 visualizations)
- **KPI summary bar**: Total grants, total dollars, Jewish subset, percentage shares
- **Donut charts**: Jewish vs. Non-Jewish split by grant count and dollar volume
- **Bar + line combo**: Trend 2019–2024 (volume bars + YoY growth rate line)
- **US choropleth map**: State-level Jewish grant density (D3.js + Albers USA projection)
- **Top-20 grantmakers**: Ranked by total dollars, horizontal bar
- **Top-20 recipients**: Ranked by total dollars, horizontal bar
- **Subject breakdown**: NTEE category distribution, horizontal bar
- **State comparison**: Jewish vs. Non-Jewish by state, grouped bar
- **Grant size histogram**: Distribution across $<10K / $10K–$100K / $100K–$1M / >$1M bins

### Interactive Features
- 4 filter controls (year, state, subject, grant size) applied simultaneously to all charts
- Hover tooltips on all Plotly charts and D3 map
- CSV export: filtered grant records downloaded as Blob URL

### Technical Implementation
- Plotly.js (CDN) for bar/line/donut/histogram charts
- D3.js v7 (CDN) for US choropleth with TopoJSON state boundaries
- Vanilla JS filter application via event listeners
- All data pre-embedded in HTML at build time — no runtime fetching
- No build step, no dependencies to install

---

## Documentation Added

- `docs/methodology.md` — data source (IRS 990 XML), classification method, chart library decisions
- `docs/architecture.md` — upstream pipeline → embedded data → dashboard; chart library rationale
- `docs/decision_log.md` — 4 decisions: pre-embedded data, Plotly+D3 split, name-based classification, NTEE codes
- `docs/data_dictionary.md` — all fields, aggregations, NTEE → subject mapping, filter parameters, keyword list reference
- `reports/research_notes.md` — IRS 990 data source background, sector benchmarks, known gaps
- `reports/results.md` — key findings, geographic concentration, COVID impact, validation against published benchmarks

---

## Known Limitations

1. Jewish classification is name-based — organizations with non-identifying names are not captured
2. Grantee state reflects IRS-registered state, not state of grant impact
3. 2020 data reflects pandemic-era emergency giving — not representative of normal-year patterns
4. Dashboard update requires re-running upstream pipeline; data is not live
