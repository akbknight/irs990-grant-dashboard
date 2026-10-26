# IRS Form 990 Grant Predictive Modeling Audit & Empirical Evaluation

**Prepared:** October 2026  
**Author:** Akshay Kumar  
**Target Codebase:** `irs990-grant-dashboard`  
**Evaluation Script:** `scripts/evaluate_models.py`  
**Dataset:** `data/FoundationData19.21.csv` (93,672 rows, 2019–2021)

---

## 1. Executive Summary & Decision

Can foundation identity, category, and geographic location predict the dollar size of future positive grant awards better than simple historical medians?

To answer this, we conducted an empirical benchmark evaluating **seven regression architectures** against **two historical baselines** using a chronological split (Train: 2019, Validation: 2020, Test: 2021).

### Key Takeaway & Recommendation
- **The Simple Baseline Won:** On the validation objective (lowest Mean Absolute Error), the **Foundation-Specific Historical Median** ($72,462 MAE) outperformed every tested machine learning and regularized regression model (closest: Log OLS at $72,635 MAE).
- **High Out-of-Sample Error:** On the locked 2021 test holdout, the foundation median reduced MAE by **6.9% ($6,351 per award)** compared to a global median. However, absolute test error remained **$86,013 MAE** with $R^2 \approx 0.022$ alongside a median grant of only $10,000.
- **Unseen Foundation Degradation:** 31.7% of held-out grant records involved foundations with no recorded awards in prior years. On these unseen entities, MAE worsened to **$94,058** with negative $R^2$ (-0.025).
- **Operational Decision:** **Do NOT deploy regression as an automated grant-amount predictor.** The platform is far better suited as an interactive research, spatial exploration, and concentration-risk audit dashboard than an automated predictive budgeting engine.

---

## 2. Dataset Scope, Population & Integrity

| Dimension | Measured Scope | Audit Notes |
|:---|---:|:---|
| **Raw Modeled Export** | 93,672 records | IRS Form 990 Schedule I grant records (2019–2021) |
| **Source Checksum (SHA256)** | `de37e5a1004a...` | Cryptographically validated raw file |
| **Positive Award Subset** | 93,638 records | Excluded 29 negative adjustments and 5 zero amounts |
| **Exact Duplicate Rows** | 2,435 records (~2.6%) | Preserved: without unique transaction IDs, repeated grants may be valid |
| **Median Grant Size** | $10,000 | 90th percentile: $173,000; 99th percentile: $1,200,000; Max: $100M |
| **Top 10 Foundation Share** | 32.7% of dollars | Severe capitalization concentration among mega-funders |
| **Temporal Coverage** | 2019: 49,570 · 2020: 23,588 · 2021: 20,514 | Demonstrates sharp reporting lag in filing coverage |

---

## 3. Candidate Model Validation Benchmark (2020 Validation Set)

Models trained strictly on 2019 data; evaluated on 2020 validation data. Rare foundation categories capped or thresholded strictly on training data to prevent lookahead leakage.

| Model Candidate | Model Family | Validation MAE (USD) | Validation RMSE (USD) | Validation $R^2$ | Log RMSE |
|:---|:---|---:|---:|---:|---:|
| **Foundation Median (Baseline)** | Historical Baseline | **$72,462** | $501,040 | 0.010 | 1.892 |
| **OLS Log** | Linear Regression | **$72,635** | $501,026 | 0.010 | 1.834 |
| **Ridge Log ($\alpha=10$)** | Regularized Linear | **$72,985** | $503,326 | 0.001 | 1.834 |
| **HistGradientBoosting (MAE loss)** | Gradient Boosted Trees | **$74,352** | $505,914 | -0.009 | 1.997 |
| **HistGradientBoosting (Log target)** | Gradient Boosted Trees | **$74,624** | $506,021 | -0.010 | 1.974 |
| **Extra Trees (Log target)** | Tree Ensemble | **$75,775** | $507,204 | -0.015 | 2.045 |
| **Random Forest (Log target)** | Tree Ensemble | **$75,826** | $507,291 | -0.015 | 2.038 |
| **Global Median (Baseline)** | Naive Baseline | **$76,889** | $508,418 | -0.019 | 2.117 |
| **Ridge Raw Target ($\alpha=10$)** | Regularized Linear | **$102,106** | $491,124 | 0.049 | 3.636 |

> **Audit Observation:** Complex nonlinear tree ensembles (Random Forest, Extra Trees, Gradient Boosting) overfit high-frequency categorical combinations and failed to beat simple linear OLS or the foundation historical median.

---

## 4. Locked Holdout Evaluation (2021 Test Set)

The winning specification (**Foundation-Specific Historical Median**, backed up by Global Median fallback) was locked and evaluated on the held-out 2021 grant distributions (20,508 positive rows):

| Evaluation Metric | Foundation Historical Median | Global Median Baseline | Absolute Improvement | Relative Gain |
|:---|---:|---:|---:|---:|
| **Mean Absolute Error (MAE)** | **$86,013** | $92,365 | -$6,351 | **+6.9%** |
| **Root Mean Squared Error (RMSE)**| **$521,913** | $534,712 | -$12,799 | +2.4% |
| **Coefficient of Determination ($R^2$)** | **0.022** | -0.027 | +0.049 | N/A |
| **Log RMSE** | **1.942** | 2.181 | -0.239 | +11.0% |

### Sub-Population Generalization Gap

| Segment | Sub-Sample Rows | Share of Holdout | Segment MAE (USD) | Segment $R^2$ |
|:---|---:|---:|---:|---:|
| **Seen Foundations** (foundations with prior history) | 13,999 | 68.3% | **$82,273** | 0.047 |
| **Unseen Foundations** (new foundations in 2021) | 6,509 | 31.7% | **$94,058** | -0.025 |

---

## 5. Architectural & Interface Integration

In response to this empirical finding, the dashboard was updated to reinforce analytical transparency over unwarranted ML claims:

1. **Empirical Outlier Matrix Trendline:**
   - Plotted a dynamic **log-linear OLS regression baseline** ($\log_{10} \text{Mean Grant} = \alpha + \beta \log_{10} \text{Capital}$) directly across the institutional scatter plot.
   - Shows the empirical scaling exponent ($\beta = 0.83$, $R^2 = 0.28$), allowing users to visually differentiate true **Mega-Grant Anchors** (institutions plotting substantially above the scaling trendline) from **High-Frequency Distributors** (institutions plotting below).
2. **Persistent Sector Donut Visual Hierarchy:**
   - Configured direct slice labeling (`textinfo: 'label+percent'`, `textposition: 'outside'`) and a persistent horizontal legend.
   - Eliminates hover-only opacity barriers so category names and capital shares are legible at a glance.
3. **Reproducibility Guarantee:**
   - Added `scripts/evaluate_models.py` so anyone can re-run the 9-model validation and test holdout benchmark directly.
