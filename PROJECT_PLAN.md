# Project Plan — IRS Form 990 Grant Analysis Dashboard

## Objective

Build an interactive dashboard analyzing $550B+ in grants from IRS Form 990 filings (2019–2024), with a focus on Jewish philanthropic giving in America. The dashboard visualizes grant patterns by year, geography, subject area, and grant size — with full interactive filtering and CSV export.

## Scope

### In Scope
- KPI summary bar (total grants, total dollars, Jewish subset statistics)
- Jewish vs. Non-Jewish comparison (donut charts by count and dollars)
- Trend over time (bar + line combo, 2019–2024)
- US choropleth map (state-level Jewish grant density, D3.js)
- Top-20 grantmakers and recipients ranked by dollars
- Subject breakdown by NTEE category
- State-by-state comparison (Jewish vs. Non-Jewish)
- Grant size histogram
- Interactive filters (year, state, subject, grant size range)
- CSV export of filtered results
- Static GitHub Pages hosting

### Out of Scope
- Real-time 990 data fetching (data is pre-processed and embedded)
- Individual-level donor or recipient profiles
- Trend forecasting or predictive analytics

## Data Source

IRS Form 990 Schedule I (grants to organizations ≥ $5,000), 2019–2024. Processed by the upstream `form990-grant-miner` pipeline. Jewish classification via grantee name keyword matching.

## Execution Phases

### Phase 1 — Core Dashboard (Complete)
- [x] All chart types implemented with interactive Plotly.js and D3.js
- [x] Jewish classification applied to 9.6M records
- [x] Interactive filters across all chart series
- [x] CSV export functionality
- [x] GitHub Pages deployment

### Phase 2 — Documentation Upgrade (Complete)
- [x] docs/methodology.md — data source, classification methodology, chart design decisions
- [x] docs/architecture.md — data flow from upstream pipeline to dashboard
- [x] docs/decision_log.md — 4 key decisions with rationale
- [x] docs/data_dictionary.md — all fields, aggregations, NTEE mapping, filter parameters
- [x] reports/research_notes.md — 990 data background, sector context, known gaps
- [x] reports/results.md — key findings, geographic concentration, COVID impact, validation

## Success Criteria

- [x] 9.6M grant records processed and visualized
- [x] All chart types interactive with hover tooltips
- [x] Filters apply consistently across all charts simultaneously
- [x] CSV export functional
- [x] No AI-generated residue in any file
- [x] Live GitHub Pages deployment
