# Data Dictionary — IRS Form 990 Grant Analysis Dashboard

## Grant Record Fields

| Field | Type | Description | Source |
|-------|------|-------------|--------|
| `ein` | string | Employer Identification Number of the grantee | IRS 990 Schedule I |
| `grantee_name` | string | Legal name of the recipient organization | IRS 990 Schedule I |
| `grantee_state` | string | 2-letter state code of grantee's IRS-registered address | IRS 990 |
| `grant_amount` | integer | Grant or contribution amount in USD | IRS 990 Schedule I, Part II |
| `tax_year` | integer | Tax year of the 990 filing (2019–2024) | IRS 990 header |
| `grantor_ein` | string | EIN of the filing (granting) organization | IRS 990 header |
| `grantor_name` | string | Legal name of the granting organization | IRS 990 header |
| `ntee_code` | string | National Taxonomy of Exempt Entities primary code | IRS Business Master File |
| `subject_category` | string | Subject classification derived from NTEE major group | Derived |
| `is_jewish` | boolean | Whether the grantee is classified as Jewish philanthropic | Derived (keyword match) |

---

## Aggregated Fields (Dashboard-Level)

| Field | Description |
|-------|-------------|
| `total_grants` | Count of grant records in the filtered dataset |
| `total_dollars` | Sum of `grant_amount` in the filtered dataset |
| `jewish_grants` | Count of grant records where `is_jewish = true` |
| `jewish_dollars` | Sum of `grant_amount` where `is_jewish = true` |
| `pct_jewish_count` | `jewish_grants / total_grants × 100` |
| `pct_jewish_dollars` | `jewish_dollars / total_dollars × 100` |

---

## Subject Category Mapping (NTEE to Dashboard)

| Dashboard Category | NTEE Major Groups |
|-------------------|------------------|
| Education | B — Education |
| Health | E — Health Care; F — Mental Health; G — Diseases; H — Medical Research |
| Human Services | P — Human Services; K — Food, Agriculture, Nutrition |
| Religion | X — Religion-Related |
| Arts & Culture | A — Arts, Culture, Humanities |
| Environment | C — Environment; D — Animal-Related |
| International | Q — International, Foreign Affairs |
| Public Benefit | W — Public, Societal Benefit; S — Community Improvement |
| Other | All remaining NTEE codes |

---

## Filter Parameters

| Filter | Values | Applied to |
|--------|--------|-----------|
| Year | 2019, 2020, 2021, 2022, 2023, 2024 | All charts |
| State | 50 states + DC | All charts |
| Subject | Education, Health, Human Services, etc. | All charts |
| Grant Size | <$10K, $10K–$100K, $100K–$1M, >$1M | All charts |

Filters are conjunctive — selecting year=2022 and state=NY returns only 2022 grants to NY-registered grantees.

---

## Classification Keywords (Jewish Identification)

A grantee is classified as Jewish if its legal name contains any of the following (case-insensitive):
`jewish`, `jewish community`, `jcc`, `hillel`, `hebrew`, `yiddish`, `israel` (in foundation/organization context), `federation` (in conjunction with other Jewish markers), and a curated list of named foundations with established Jewish identity.

Full keyword list maintained in the upstream pipeline: `form990-grant-miner/categorize_keywords.py`.
