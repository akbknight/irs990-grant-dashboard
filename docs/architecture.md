# Architecture — IRS Form 990 Grant Analysis Dashboard

## System Overview

The dashboard is a self-contained static HTML file. All grant data is pre-processed by the upstream pipeline (`form990-grant-miner`) and embedded in the dashboard at build time. No server, no database, no API calls at runtime.

```
form990-grant-miner (separate repo)
    │
    ▼
IRS 990 XML bulk data
    │ (Schedule I extraction)
    ▼
Structured grant records (CSV / JSON)
    │ (aggregation and classification)
    ▼
Dashboard data payload (embedded JSON)
    │
    ▼
index.html (Plotly.js + D3.js charts)
    │
    ▼
GitHub Pages (static hosting)
```

---

## Dashboard Structure

```
index.html
├── <head>
│   ├── Plotly.js (CDN)
│   └── D3.js v7 (CDN)
├── <body>
│   ├── KPI summary bar
│   ├── Comparison charts (donut: Jewish vs. Non-Jewish by count and dollars)
│   ├── Trend chart (bar + line combo, 2019–2024)
│   ├── US choropleth map (D3.js, state-level grant density)
│   ├── Top-N ranked tables (grantmakers, recipients)
│   ├── Subject breakdown (horizontal bar)
│   ├── State comparison (grouped bar)
│   ├── Grant size histogram
│   └── Filter controls (year, state, subject, amount range)
└── <script>
    ├── Embedded data payload (JSON arrays for all chart series)
    ├── Filter application logic
    ├── Chart initialization (Plotly.newPlot / D3.select)
    └── CSV export handler
```

---

## Data Flow

### Upstream (form990-grant-miner)

1. IRS XML bulk download from AWS S3 (`s3://irs-form-990/`)
2. ElementTree XML parsing of Schedule I records (Part II: grants to organizations)
3. Grantee name normalization and deduplication
4. Jewish classification via keyword matching
5. NTEE code subject classification
6. State aggregation and year aggregation
7. Top-N grantmaker and recipient ranking
8. Output: structured JSON arrays for each chart series

### Dashboard (this repo)

1. Pre-embedded JSON data loaded on page init
2. Plotly.js renders interactive charts with hover tooltips
3. D3.js renders US choropleth from state-level density object
4. Filter controls apply to all chart series simultaneously via event listeners
5. CSV export: filtered grant records converted to CSV string and downloaded via Blob URL

---

## Chart Library Decisions

| Chart type | Library | Reason |
|-----------|---------|--------|
| Bar, line, donut, histogram | Plotly.js | Built-in interactivity (zoom, hover, filter) with minimal configuration |
| US choropleth map | D3.js | Plotly's choropleth requires GeoJSON topology; D3.js + TopoJSON gives more control over projection and color scale |

---

## Deployment

- **Host**: GitHub Pages (`akbknight.github.io/irs990-grant-dashboard`)
- **No build step**: `index.html` is deployed directly from root
- **No environment variables**: all data is pre-embedded; no API keys required
- **Update workflow**: re-run the upstream pipeline, extract the new JSON payload, update the embedded data in `index.html`, push to main
