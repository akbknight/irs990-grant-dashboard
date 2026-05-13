# Decision Log — IRS Form 990 Grant Analysis Dashboard

## Decision 1: Pre-embedded data over runtime API calls

**Decision:** Embed the processed grant data directly in the HTML file at build time rather than fetching from an API at runtime.

**Rationale:** The grant dataset (9.6M records aggregated to ~50KB of chart-ready JSON) is static — IRS 990 filings for a given year do not change after the IRS publishes them. There is no reason to re-fetch this data on every page load. Pre-embedding eliminates network latency, removes the need for an API server, and allows hosting on GitHub Pages with no infrastructure cost.

**Tradeoff:** Updating the dashboard requires re-running the upstream pipeline and updating the embedded payload. This is acceptable because the data only needs updating when the IRS publishes a new filing year (~once annually).

---

## Decision 2: Plotly.js for charts, D3.js for map

**Decision:** Use Plotly.js for bar/line/donut/histogram charts and D3.js specifically for the US choropleth.

**Rationale:** Plotly.js provides high-quality interactive charts with built-in zoom, pan, hover tooltips, and legend filtering with minimal code. However, Plotly's choropleth chart requires either Mapbox (requires API key) or a built-in USA map (low resolution with limited color scale control). D3.js with TopoJSON gives full control over state boundaries, projection (Albers USA), and the sequential color scale needed to show density variation across a 100× range.

**Tradeoff:** Two chart libraries increase bundle size, but both are loaded from CDN (no build step required) and the combined load is ~2MB — acceptable for a data-heavy analytical dashboard.

---

## Decision 3: Name-based Jewish classification over external taxonomy

**Decision:** Classify Jewish philanthropic grants using a curated grantee name keyword list rather than relying on NTEE codes or external classification databases.

**Rationale:** NTEE codes classify the mission of an organization (education, religion, health) not its cultural identity. A Jewish federation running a food bank would be classified as "Human Services" under NTEE, not as Jewish philanthropy. Name-based classification captures cultural identity directly. The keyword list is curated, documented, and reproducible.

**Tradeoff:** Name-based classification has precision vs. recall tradeoffs — organizations with non-identifying names are missed; coincidental name matches may over-classify. The methodology errs toward precision (conservative classification).

---

## Decision 4: Subject classification via NTEE codes

**Decision:** Use NTEE codes from IRS registrations for subject classification rather than NLP-based classification of grant descriptions.

**Rationale:** NTEE codes are standardized, consistently applied across all 990 filers, and directly available in the IRS dataset. NLP-based classification of grant description text would require labeled training data, is inconsistently formatted across filers, and adds pipeline complexity without a clear quality advantage over the existing standardized taxonomy.

**Tradeoff:** NTEE codes reflect the grantee's primary mission, not the specific purpose of a given grant. A health organization might receive a grant for unrelated education purposes, and that grant would still be classified as "Health."
