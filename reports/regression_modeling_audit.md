# IRS Form 990 Grant Predictive Modeling Audit & Empirical Evaluation

**Prepared:** October 2026  
**Author:** Akshay Kumar  
**Target Codebase:** `irs990-grant-dashboard`  
**Evaluation Script:** `scripts/evaluate_models.py`  
**Dataset:** `data/FoundationData19.21.csv` (93,672 raw records, 93,638 positive modeling records, 2019–2021)

---

## 1. Executive Summary & Structured Case Study

### Core Analytical Case Study (Question → Evidence → Result → Recommendation → Limitation)

- **Question:** Can foundation identity, category, and geographic location predict next-year positive individual grant dollar amounts better than simple historical medians?
- **Evidence:** Evaluated a local export of 93,672 raw IRS Form 990 Schedule I grant records (93,638 positive modeling records, 2019–2021). Evaluated seven regression architectures (OLS log, Ridge raw/log, Random Forest log, Extra Trees log, HistGradientBoosting log/MAE) against two historical baselines (Foundation-Specific Median, Global Median) using a chronological split (Train: 2019, 49,547 rows; Validation: 2020, 23,583 rows; Test: 2021, 20,508 rows). Rare-category thresholds and target statistics were fit strictly on training partitions to prevent data leakage.
- **Result:** The **Foundation-Specific Historical Median** achieved the lowest validation MAE ($72,462), outperforming all regression models (Log OLS: $72,635; Log Ridge: $72,985; HistGradientBoosting MAE: $74,352; HistGradientBoosting log: $74,624; Random Forest: $75,826). On the held-out 2021 test set (20,508 rows), the foundation median reduced MAE by **6.9% ($6,351 per award)** relative to a global median ($86,013 vs $92,365), but absolute test MAE remained high at **$86,013** alongside an $R^2$ of **0.022** against a dataset median grant of $10,000. Furthermore, on foundations with no prior history (31.7% of test records), test error deteriorated to **$94,058 MAE** ($R^2 = -0.025$).
- **Recommendation:** **Do NOT deploy regression as an automated grant-amount budgeting predictor.** The dashboard should be positioned for historical research, geographic exploration, and institutional concentration analysis, rather than automated grant forecasting.
- **Limitation:** Findings apply strictly to the local 2019–2021 export and cannot be generalized to the entire IRS Form 990 population. Modeling features were restricted to foundation identity, category, and location; they did not incorporate narrative proposal text, multi-year asset histories, or recipient financial statements.

---

## 2. Distinction: Institution-Level Scaling Trendline vs. Award-Level Prediction Benchmark

To avoid confusing institutional aggregates with individual grant predictions, the platform maintains two distinct analytical layers:

| Dimension | Institution-Level Descriptive Trendline | Individual-Award Prediction Benchmark |
|:---|:---|:---|
| **Population** | Curated subset of ~30+ major philanthropic institutions (Jewish Giving sector) | 93,672 raw / 93,638 positive grant transaction records across all reporting foundations |
| **Unit of Analysis** | Institutional aggregate (Total Capitalization vs. Mean Grant Size) | Individual grant transaction (Dollar amount per grant award) |
| **Research Question** | How does mean grant size scale with total capital pool across institutions? | Can metadata predict individual future grant amounts out-of-sample? |
| **Methodology** | Log-linear Ordinary Least Squares (OLS) baseline: $\log_{10}(\text{Mean Grant}) = \alpha + \beta \log_{10}(\text{Capital})$ | 7 regression architectures vs. 2 empirical median baselines (chronological split) |
| **Fitted Parameters** | Scaling exponent $\beta \approx 0.83$, $R^2 \approx 0.28$ | Validation MAE range: $72,462 to $102,106 |
| **Diagnostic Status** | **Descriptive comparison only.** Visualizes institutions plotting above the trendline (higher average award) vs. below (high-frequency distributors). Does **not** compute studentized residuals or Cook's distance to establish formal statistical outliers. | **Empirical out-of-sample benchmark.** Formal evaluation on held-out chronological test sets with seen/unseen foundation error decomposition. |
| **Scope & Limitations** | Aggregate summary; sensitive to institutional inclusion; does not model individual grant variance. | Dependent on historical filing continuity; high residual variance ($86k test MAE) prevents automated deployment. |

---

## 3. Dataset Scope, Population & Data Integrity

The empirical evaluation was conducted on the local export file `data/FoundationData19.21.csv`:

| Dimension | Measured Scope | Audit Details |
|:---|---:|:---|
| **Raw Modeled Records** | **93,672 records** | Full raw record count in local export (2019: 49,570 · 2020: 23,588 · 2021: 20,514) |
| **File Checksum (SHA256)** | `de37e5a1004a...` | Cryptographically verified source export file |
| **Positive Modeling Records** | **93,638 records** | Excluded 29 negative adjustments and 5 zero-dollar records |
| **Split Breakdown (Positive)** | **Train: 49,547 · Val: 23,583 · Test: 20,508** | Yearly counts reflect records present in local export without inferring IRS filing lag |
| **Exact Duplicate Rows** | 2,435 records (~2.6%) | Preserved: absent unique transaction IDs, repeated grant amounts to identical recipients in a year may represent recurring tranches |
| **Distribution Skew** | Median: $10,000 · Mean: $78,767 | 75th percentile: $25,000; 90th percentile: $173,000; 99th percentile: $1,200,000; Max: $100M |
| **Capital Concentration** | Top 10 Foundations: 32.7% of dollars | Severe concentration among top foundations |
| **Cold-Start Foundation Share** | 31.7% in 2021 test set | 6,509 of 20,508 test records have foundations absent from 2019–2020 training data |

---

## 4. Candidate Model Validation Benchmark (2020 Validation Set)

All candidate models were fit strictly on 2019 data (49,547 rows) and evaluated on held-out 2020 data (23,583 rows). Categorical encodings were fit exclusively on training data to prevent lookahead leakage.

| Model Candidate | Model Architecture | Validation MAE (USD) | Validation RMSE (USD) | Validation $R^2$ | Log RMSE | Evaluation Time |
|:---|:---|---:|---:|---:|---:|---:|
| **Foundation Median (Baseline)** | Historical Fdn Median | **$72,462** | $501,040 | 0.010 | 1.892 | 0.05s |
| **OLS Log** | Linear Regression (One-Hot) | **$72,635** | $501,026 | 0.010 | 1.834 | 0.62s |
| **Ridge Log ($\alpha=10$)** | Regularized Linear (One-Hot) | **$72,985** | $503,326 | 0.001 | 1.834 | 0.39s |
| **HistGradientBoosting (MAE loss)** | Gradient Tree Ensemble | **$74,352** | $505,914 | -0.009 | 1.997 | 1.40s |
| **HistGradientBoosting (Log target)** | Gradient Tree Ensemble | **$74,624** | $506,021 | -0.010 | 1.974 | 1.00s |
| **Extra Trees (Log target)** | Randomized Forest Ensemble | **$75,775** | $507,204 | -0.015 | 2.045 | 6.42s |
| **Random Forest (Log target)** | Bagged Tree Ensemble | **$75,826** | $507,291 | -0.015 | 2.038 | 4.32s |
| **Global Median (Baseline)** | Unconditional Median | **$76,889** | $508,418 | -0.019 | 2.117 | 0.06s |
| **Ridge Raw Target ($\alpha=10$)** | Linear (Untransformed) | **$102,106** | $491,124 | 0.049 | 3.636 | 0.37s |

> **Audit Observation:** On held-out 2020 awards, tree ensembles (Random Forest, Extra Trees, Gradient Boosting) exhibited higher validation MAE ($74,352 to $75,826) than the simple foundation historical median baseline ($72,462). The simpler historical baseline yielded the lowest absolute prediction error.

---

## 5. Locked Holdout Evaluation (2021 Test Set)

The winning validation specification (**Foundation-Specific Historical Median**, falling back to Global Median for unseen foundations) was locked and evaluated on the 2021 test holdout (20,508 rows), refit on combined 2019–2020 data:

| Metric | Foundation Historical Median | Global Median Baseline | Absolute Difference | Relative Gain |
|:---|---:|---:|---:|---:|
| **Mean Absolute Error (MAE)** | **$86,013** | $92,365 | -$6,351 | **+6.9%** |
| **Root Mean Squared Error (RMSE)** | **$521,913** | $534,712 | -$12,799 | +2.4% |
| **Coefficient of Determination ($R^2$)** | **0.022** | -0.027 | +0.049 | N/A |
| **Log RMSE** | **1.942** | 2.181 | -0.239 | +11.0% |

### Generalization Performance on Seen vs. Unseen Foundations

| Evaluation Sub-Population | Rows | Share of Test Set | Sub-Population MAE (USD) | Sub-Population $R^2$ |
|:---|---:|---:|---:|---:|
| **Seen Foundations** (foundations observed in 2019–2020) | 13,999 | 68.3% | **$82,273** | 0.047 |
| **Unseen Foundations** (foundations first observed in 2021) | 6,509 | 31.7% | **$94,058** | -0.025 |

---

## 6. Dashboard Interface Alignment

In accordance with this audit:
1. **Descriptive Scatter Matrix:** Labeled as an *Institutional Scaling Matrix* with an OLS baseline ($\beta \approx 0.83$, $R^2 \approx 0.28$). Displays entities plotting above or below the scaling line without claiming formal statistical outlier status.
2. **Persistent Sector Donut:** Labels and percentages are rendered directly outside slices with a persistent horizontal legend.
3. **Reproducibility:** The benchmark script `scripts/evaluate_models.py` produces the exact figures in this report directly from `data/FoundationData19.21.csv`.
