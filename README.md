# IRS Form 990 Philanthropic Grant Miner & 3D Spatial Intelligence Dashboard

> [!IMPORTANT]
> **Flagship Data Engineering & Visualization Pipeline · Part of the Akshay Kumar Technical Portfolio Ecosystem**  
> 🌐 **Executive Portfolio:** [https://akbknight.github.io/](https://akbknight.github.io/) · 💼 **LinkedIn:** [linkedin.com/in/akshaykumardl](https://www.linkedin.com/in/akshaykumardl/) · 📄 **Curriculum Vitae:** [Download PDF (369 KB)](https://akbknight.github.io/assets/Akshay_Resume.pdf)

[![Live Demo](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-0284c7?style=flat-square&logo=github)](https://akbknight.github.io/irs990-grant-dashboard/)
[![Capital Mapped](https://img.shields.io/badge/Capital%20Mapped-$550.2B-10b981?style=flat-square)](https://akbknight.github.io/irs990-grant-dashboard/)
[![Records Analyzed](https://img.shields.io/badge/Records%20Analyzed-9.7M%2B-blue?style=flat-square)](https://akbknight.github.io/irs990-grant-dashboard/)
[![Spatial Engine](https://img.shields.io/badge/3D%20Engine-Globe.gl%20%7C%20Three.js-38bdf8?style=flat-square)](https://akbknight.github.io/irs990-grant-dashboard/)
[![Analytics](https://img.shields.io/badge/Analytics-Log--Log%20Outlier%20Matrix-f59e0b?style=flat-square)](https://akbknight.github.io/irs990-grant-dashboard/)
[![Scope](https://img.shields.io/badge/Scope-2019--2024-8b5cf6?style=flat-square)](https://akbknight.github.io/irs990-grant-dashboard/)
[![Author](https://img.shields.io/badge/Author-Akshay%20Kumar-09090b?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/akshaykumardl/)
[![License: MIT](https://img.shields.io/badge/License-MIT-gray?style=flat-square)](LICENSE)

An enterprise-grade, high-throughput data engineering and visual intelligence system mapping **$550.2B in charitable capital** across **9,693,767 tax-exempt grant records** from IRS Form 990 Schedule I filings (2019–2024). Features hardware-accelerated **3D WebGL spatial flow arcs**, econometric **log-log outlier detection matrices**, choropleth heat maps, and sub-150ms client-side cross-filtering.

---

## 🌐 Live Interactive Application

👉 **Launch Live Intelligence Platform:** **[https://akbknight.github.io/irs990-grant-dashboard/](https://akbknight.github.io/irs990-grant-dashboard/)**

---

## 🏛️ Pipeline & Analytical Architecture

```mermaid
flowchart TD
    A["IRS AWS Registry\n(Form 990 XML E-Filings 2019-2024)"] -->|High-Throughput Batch Stream| B["XML Ingestion & Parsing Engine\n(Python · lxml / xml.etree)"]
    B -->|Schema Inference & Normalization| C["Forensic Validation & Deduplication\n(EIN · Tax Period · Schedule I Filings)"]
    C -->|Entity Classification & NLP Tagging| D["DuckDB Analytical Engine\n(Sub-Second Aggregate Aggregations)"]
    D -->|Aggregated Data Embed & Topologies| E["Client-Side Visual Presentation Engine"]
    
    subgraph UI ["Executive Data Intelligence Platform (Apple HIG / Palantir Aesthetic)"]
        E --> G["3D WebGL Spatial Globe\n(Globe.gl · Three.js Capital Flow Arcs)"]
        E --> H["Econometric Outlier Matrix\n(Plotly.js Log-Log Scatter Plot)"]
        E --> I["National Choropleth Heatmap\n(D3.js v7 · TopoJSON US Atlas)"]
        E --> J["Longitudinal Trajectory & Sector Breakdown\n(Dual-Axis Spline · Donut Drilldown)"]
        E --> K["Ranked Institutional Registries & Forensic Modal\n(Palantir Table · Entity Inspection Sheet)"]
    end
```

### Architecture Highlights:
1. **Dual-Tier Data Architecture**: Combines historical benchmarked aggregates derived from authoritative IRS AWS e-file XML archives ($550.2B in Schedule I disbursements) with real-time entity enrichment.
2. **Live ProPublica Nonprofit Explorer API v2 & Verified 990 PDFs**: Live client-side integration querying authoritative 9-digit EINs, verified balance sheets (assets, revenues, tax years), direct links to download official IRS Form 990 / 990-PF PDFs, and registry profiles.
3. **Source Health & Freshness Telemetry HUD**: Persistent real-time monitor displaying API connectivity, request latency, cache hit-rate (24h TTL), and data provenance badges.
4. **Deterministic Entity Classification**: Automated rule engine categorizing funding flows into Higher Education, Medical Research, Religion & Human Services, Civic Advocacy, and Philanthropic Intermediaries.
5. **Sub-150ms Client-Side Filtering**: In-memory multidimensional filtering across 6 tax years, 50 states, 10 sectors, and grant brackets with instantaneous DOM updates and zero page reloads.
6. **Executive Industrial Dark UI**: Deep onyx (`#050507`), hairline glassmorphism (`rgba(14, 18, 28, 0.75)`), luminous cyan (`#38bdf8`) and amber (`#f59e0b`) accents matching the core portfolio design token architecture.

---

## 📊 Quantitative Impact & Ledger

| Metric Dimension | Quantitative Scope | Architectural Detail |
|:---|:---|:---|
| **Total Philanthropic Capital** | **$550,214,891,420 ($550.2B)** | Aggregated Schedule I grant disbursements |
| **Total Grant Transactions** | **9,693,767 Records** | Individual recipient records processed |
| **Focal Segment (Jewish Giving)** | **275,446 Grants · $10.6B** | 2.84% grant volume / 1.93% capital flow |
| **Temporal Coverage** | **2019 – 2024 (6 Tax Years)** | Multi-year longitudinal grant tracking |
| **3D Spatial Arcs** | **20+ Global & Domestic Flow Arcs** | Real-time animated WebGL trajectory vectors |
| **Client Execution Latency** | **< 150 ms Filter Time** | Pure in-memory reactive updates |

---

## ⚡ Core Platform Capabilities

### 1. 🌍 3D WebGL Global Capital Flow Engine
- Powered by `Globe.gl` and `Three.js` with hardware-accelerated 60fps rendering.
- Visualizes cross-border philanthropic vectors: U.S. Domestic hubs to global destinations (Israel Gateway, European academic corridors, Latin American initiatives).
- Foundation HQ beacons with pulsing dynamic ripple rings.
- Live camera orbit telemetry readout (`LAT`, `LNG`, `ALT`) and 1-click orbital presets (`U.S. Domestic`, `Israel Gateway`, `Global Outflows`, `NYC Epicenter`).

### 2. 📈 Institutional Scaling Matrix & Descriptive Baseline
- Logarithmic distribution of **Institutional Capitalization vs. Average Grant Size** anchored by an empirical **log-linear OLS scaling trendline** ($\log_{10} 	ext{Mean Grant} = lpha + eta \log_{10} 	ext{Capital}$, $eta \approx 0.83$, $R^2 \approx 0.28$).
- Descriptive comparison: differentiates institutions plotting above the scaling baseline (higher mean award, such as Marcus Foundation at $1.55M avg grant) from high-frequency distributors plotting below (such as Jewish Communal Fund). *Note: This is an informal descriptive scaling comparison across ~30+ aggregate entities, not a formal studentized residual outlier test.*
- Interactive point-click trigger opening the forensic inspection sheet for any selected entity.

### 3. 🗺️ D3.js National Choropleth Heatmap
- TopoJSON-powered logarithmic heat map of all 50 U.S. states + DC.
- Dynamic hover tooltips displaying total funding, grant count, and average allocation.
- Direct click-to-filter interaction isolating any individual state across the entire telemetry dashboard.

### 4. 🍩 Dynamic Sector Donut & Longitudinal Trajectory
- 10-category breakdown with **persistent direct callout labels and shares**, plus an explicit cross-filter legend eliminating hover-only discovery friction.
- Center KPI metric readout dynamically responding to global cohort and sector filters.
- Dual-axis longitudinal volume bars and smoothed spline curve tracking capital growth across 2019–2024.

### 5. 🏢 Ranked Institutional Registries & Forensic Modal
- Tabbed registries for **Top 20 Grantmakers** and **Top 20 Recipients**.
- Displays rank, EIN, classification badge, city/state, total dollars, grant count, average grant, and visual volume progress bars.
- Apple HIG-inspired modal inspection sheet providing deep entity profiles, Schedule I notes, and a 1-click "Isolate Entity in Dashboard" filter.

### 6. 🎛️ Filter Control Center
- Real-time search query matching foundation names, states, and sectors.
- Interactive year pills, sector selectors, state filters, and cohort toggles.
- Active filter pill HUD with 1-click removal and instant CSV data export.

### 7. 🔬 Empirical Predictive Modeling Benchmark (5-Element Case Study)
- **Question:** Can foundation identity, category, and location predict next-year positive individual grant amounts better than simple historical medians?
- **Evidence:** Local export of 93,672 raw Form 990 Schedule I grant records (93,638 positive records, 2019–2021; Train 2019: 49,547 · Val 2020: 23,583 · Test 2021: 20,508; 2,435 exact duplicates preserved). Chronologically evaluated 7 regression architectures against 2 empirical baselines.
- **Candidate Benchmark (2020 Validation MAE):**
  1. *Foundation-Specific Historical Median (Baseline):* **$72,462** (Winner)
  2. *Log OLS Linear Regression:* **$72,635**
  3. *Log Ridge Regression ($\alpha=10$):* **$72,985**
  4. *HistGradientBoosting (MAE loss):* **$74,352**
  5. *HistGradientBoosting (Log target):* **$74,624**
  6. *Extra Trees (Log target):* **$75,775**
  7. *Random Forest (Log target):* **$75,826**
  8. *Global Median Baseline:* **$76,889**
  9. *Raw Target Ridge ($\alpha=10$):* **$102,106**
- **Result:** The foundation historical median won on validation MAE ($72,462). On the 2021 test holdout (20,508 rows), the foundation median reduced MAE by **6.9% ($6,351 per award)** vs a global median ($86,013 vs $92,365), but absolute test error remained **$86,013 MAE** with $R^2 \approx 0.022$ alongside a median grant of $10,000. On unseen foundations (31.7% of test records), error worsened to **$94,058 MAE** ($R^2 = -0.025$).
- **Recommendation:** **Do NOT deploy regression as an automated predictive grant budgeter.** The platform is best suited for historical research, spatial exploration, and concentration analysis.
- **Limitation:** Findings apply strictly to the local 2019–2021 export (not the full IRS population). Features exclude narrative proposals, multi-year asset histories, and recipient balance sheets. The scatter trendline is an aggregate institutional descriptive baseline, not an individual transaction predictor, and does not compute studentized residuals to establish formal statistical outliers.
- **Reproducibility:** Run `py -3.12 scripts/evaluate_models.py` or inspect [`reports/regression_modeling_audit.md`](reports/regression_modeling_audit.md).


---

## 🛠️ Technology Stack

- **Data Wrangling & Extraction**: Python 3.11, Pandas, DuckDB, `xml.etree`
- **Spatial & 3D Visualization**: Globe.gl, Three.js WebGL
- **Econometric & Statistical Charts**: Plotly.js 2.35 (WebGL accelerated)
- **Cartographic Visuals**: D3.js v7, TopoJSON US Atlas
- **Frontend Architecture**: Modern Vanilla ES6+, CSS Glassmorphism, Responsive Grid
- **Design Tokens**: Executive Industrial Dark, JetBrains Mono, Inter, Hairline Borders
- **Hosting & CI/CD**: GitHub Pages, automated verification

---

## 🚀 Local Exploration

```bash
# Clone the repository
git clone https://github.com/akbknight/irs990-grant-dashboard.git
cd irs990-grant-dashboard

# Open directly in your browser (no build steps or node_modules needed)
open index.html   # On macOS
start index.html  # On Windows
```

---

## 👤 Author & Strategic Portfolio

**Akshay Kumar**  
STEM MBA Candidate · Business Analytics & AI · American University Kogod School of Business  
Former Computer Programmer · U.S. Department of State  
- **Personal Portfolio:** [https://akbknight.github.io/](https://akbknight.github.io/)  
- **LinkedIn:** [linkedin.com/in/akshaykumardl](https://www.linkedin.com/in/akshaykumardl/)  
- **Email:** [ak8335a@american.edu](mailto:ak8335a@american.edu)

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.  
All underlying Form 990 data is public domain under U.S. Department of the Treasury guidelines.
