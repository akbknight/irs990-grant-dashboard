# IRS Form 990 Grant Analysis Dashboard

Interactive dashboard analyzing **$550B+ in grants** from IRS Form 990 filings (2019–2024), with a focus on Jewish philanthropic giving in America.

## Live Dashboard

👉 **[View the Dashboard](https://akbknight.github.io/irs990-grant-dashboard/)**

## Key Statistics

| Metric | Value |
|--------|-------|
| Total Grants | 9,693,767 |
| Total Dollars | $550.2B |
| Jewish Grants | 275,446 |
| Jewish Dollars | $10.6B |
| % Jewish (by count) | 2.84% |
| Years Covered | 2019–2024 |

## Dashboard Features

- **KPI Summary Bar** — Key metrics at a glance
- **Jewish vs Non-Jewish Comparison** — Donut charts for count and dollar splits
- **Trend Over Time** — Bar + line combo chart (2019–2024)
- **US Choropleth Map** — State-level Jewish grant density (D3.js)
- **Top 20 Grantmakers** — Ranked by total dollar amount
- **Top 20 Recipients** — Ranked by total dollars received
- **Subject Breakdown** — Education, Religion, Health, and more
- **State-by-State Comparison** — Jewish vs Non-Jewish by state
- **Grant Size Distribution** — Histogram by grant amount range
- **Interactive Filters** — Year, state, subject, expense type, grant amount
- **CSV Export** — Download filtered results

## Tech Stack

- **Plotly.js** — Interactive charts with hover tooltips
- **D3.js** — US choropleth map
- **Vanilla HTML/CSS/JS** — Single self-contained file, no build step
- **GitHub Pages** — Static hosting

## Data Source

All data derived from publicly available IRS Form 990 returns (2019–2024).

## License

MIT
