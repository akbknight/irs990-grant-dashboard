# Methodology — IRS Form 990 Grant Analysis Dashboard

## Data Source

All data derives from publicly available IRS Form 990 returns filed with the Internal Revenue Service for tax years 2019–2024. Form 990 (Return of Organization Exempt from Income Tax) requires 501(c)(3) organizations with gross receipts ≥ $200,000 or total assets ≥ $500,000 to disclose all grants and contributions paid to other organizations in Schedule I.

The IRS releases 990 data as XML bulk downloads through the IRS Statistics of Income (SOI) program and AWS S3 public dataset (`s3://irs-form-990/`). The source pipeline (`form990-grant-miner`) extracts Schedule I grant records from this XML dataset, producing the structured grant records displayed in this dashboard.

---

## Dataset Coverage

| Dimension | Coverage |
|-----------|----------|
| Tax years | 2019–2024 (6 years) |
| Total grant records | 9,693,767 |
| Total grant dollars | $550.2B |
| Grantor organizations | 501(c)(3) public charities and private foundations |
| Geographic scope | United States (all 50 states + DC) |

---

## Classification Methodology

### Jewish Philanthropic Identification

Grant records are classified as Jewish philanthropic giving based on grantee organization name matching. The classification logic applies a curated keyword and phrase list covering:
- Direct religious markers ("Jewish", "Hebrew", "Yiddish", "Israel", "Hillel", "JCC")
- Named foundations with established Jewish identity
- Federation and communal organization patterns ("Federation", "Jewish Community")

Classification is applied at the grantee level — a grantee is classified as Jewish if any matching keyword appears in its name. Grants to that grantee are then aggregated into the Jewish category.

**Known limitations**: Name-based classification misses organizations with non-identifying names; overclassifies organizations where the name is coincidentally matching. The methodology errs toward precision (fewer false positives) over recall.

### Subject Classification

Grants are classified into subject areas using NTEE (National Taxonomy of Exempt Entities) codes attached to the grantee's IRS registration. Primary NTEE codes map to subject categories: Education (B), Health (E/F/G/H), Human Services (P), Religion (X), Arts (A), Environment (C/D), International (Q), Public Benefit (W).

---

## Aggregation and Presentation

### Geographic Aggregation

Grants are aggregated to the state level using the grantee's IRS-registered state of incorporation. This is a proxy for geographic impact, not a precise measure — a national organization incorporated in one state may operate in all states.

### Trend Analysis

Year-over-year trend analysis covers 2019–2024. 2020 data reflects COVID-era giving patterns; this year shows elevated emergency relief grants to health, food security, and human services categories.

---

## Dashboard Design

The dashboard is a self-contained HTML file using Plotly.js for interactive charts and D3.js for the US choropleth. No backend is required — all data is embedded in the page at build time. This allows GitHub Pages hosting without a server.

Chart types and their rationale:
- **Donut charts**: Jewish vs. Non-Jewish share comparisons — part-of-whole relationships
- **Bar + line combo**: Trend over time — absolute volume (bars) and YoY growth rate (line) on dual axes
- **US choropleth (D3.js)**: State-level density — geographic distribution requires a map, not a table
- **Top-N ranked lists**: Grantmaker and recipient rankings — bar charts sorted descending
- **Histogram**: Grant size distribution — frequency distribution requires equal-width bins
