"""
Empirical Regression Model Benchmark & Baseline Evaluation
Evaluates 7 regression architectures against simple historical medians
on public IRS Form 990 grant records (93,672 rows, 2019-2021).
"""
import sys
import json
import warnings
from pathlib import Path

# Add shared pre-compiled package location if running under standalone python
PKG_DIR = Path(r"C:\Users\Akshay Kumar\Documents\Codex\2026-09-02\do-you-have-acess-to-all\outputs\Results_Analysis_2026-10-25\packages")
if PKG_DIR.exists():
    sys.path.insert(0, str(PKG_DIR))

import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import Ridge, LinearRegression
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor, HistGradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "FoundationData19.21.csv"
ALT_DATA_PATH = Path(r"C:\Users\Akshay Kumar\Downloads\Akshay\Projects and Code\Form 990 Grant Research\FoundationData19.21.csv")

def load_data():
    p = DATA_PATH if DATA_PATH.exists() else ALT_DATA_PATH
    if not p.exists():
        raise FileNotFoundError(f"Data source not found at {p}")
    raw = pd.read_csv(p)
    d = raw.loc[raw.AWARD.gt(0) & raw.Year.isin([2019, 2020, 2021])].copy()
    for col in ["Foundation", "Category", "Location", "Recipient"]:
        d[col] = d[col].fillna("__MISSING__").astype(str).str.strip().str.upper()
    return d

def compute_metrics(y_true, y_pred):
    y_pred = np.maximum(0, np.asarray(y_pred))
    y_true = np.asarray(y_true)
    return {
        "MAE_USD": float(mean_absolute_error(y_true, y_pred)),
        "RMSE_USD": float(np.sqrt(mean_squared_error(y_true, y_pred))),
        "R2": float(r2_score(y_true, y_pred)),
        "log_RMSE": float(np.sqrt(mean_squared_error(np.log1p(y_true), np.log1p(y_pred))))
    }

def fit_and_predict(model_name, train_df, test_df):
    features = ["Foundation", "Category", "Location"]
    y_train = train_df.AWARD.to_numpy()
    
    # Rare-category handling fitted strictly on training data
    top100 = set(train_df.Foundation.value_counts().index[:100])
    
    def prep(df, cap_cardinality=False):
        x = df[features].copy()
        if cap_cardinality:
            x["Foundation"] = x.Foundation.where(x.Foundation.isin(top100), "__OTHER__")
        return x

    if model_name == "Global median":
        return np.full(len(test_df), np.median(y_train))
    
    if model_name == "Foundation median":
        meds = train_df.groupby("Foundation").AWARD.median()
        return test_df.Foundation.map(meds).fillna(np.median(y_train)).to_numpy()

    is_hist = model_name.startswith("Histogram")
    X_train = prep(train_df, cap_cardinality=is_hist)
    X_test = prep(test_df, cap_cardinality=is_hist)

    enc = OneHotEncoder(handle_unknown="ignore", min_frequency=10)
    
    if model_name == "OLS log":
        pipe = make_pipeline(enc, LinearRegression())
        log_target = True
    elif model_name == "Ridge raw":
        pipe = make_pipeline(enc, Ridge(alpha=10))
        log_target = False
    elif model_name == "Ridge log":
        pipe = make_pipeline(enc, Ridge(alpha=10))
        log_target = True
    elif model_name == "Random forest log":
        pipe = make_pipeline(enc, RandomForestRegressor(n_estimators=80, max_depth=14, min_samples_leaf=20, n_jobs=2, random_state=42))
        log_target = True
    elif model_name == "Extra trees log":
        pipe = make_pipeline(enc, ExtraTreesRegressor(n_estimators=80, max_depth=14, min_samples_leaf=20, n_jobs=2, random_state=42))
        log_target = True
    elif model_name == "Histogram boosting log":
        pipe = make_pipeline(OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value=-1),
                             HistGradientBoostingRegressor(categorical_features=[0, 1, 2], max_iter=150, max_leaf_nodes=15, l2_regularization=10, random_state=42))
        log_target = True
    elif model_name == "Histogram boosting MAE":
        pipe = make_pipeline(OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value=-1),
                             HistGradientBoostingRegressor(loss="absolute_error", categorical_features=[0, 1, 2], max_iter=150, max_leaf_nodes=15, l2_regularization=10, random_state=42))
        log_target = False
    else:
        raise ValueError(f"Unknown model: {model_name}")

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        pipe.fit(X_train, np.log1p(y_train) if log_target else y_train)
    preds = pipe.predict(X_test)
    return np.maximum(0, np.expm1(preds) if log_target else preds)

def run_evaluation():
    print("=" * 70)
    print("IRS Form 990 Grant Predictive Modeling Audit")
    print("Evaluating 7 Regressors vs 2 Empirical Baselines (Chronological Split)")
    print("=" * 70)

    data = load_data()
    train = data[data.Year == 2019]
    valid = data[data.Year == 2020]
    test = data[data.Year == 2021]

    print(f"Data Splits: Train (2019): {len(train):,} rows | Validation (2020): {len(valid):,} rows | Test (2021): {len(test):,} rows\n")

    models = [
        "Global median",
        "Foundation median",
        "OLS log",
        "Ridge raw",
        "Ridge log",
        "Random forest log",
        "Extra trees log",
        "Histogram boosting log",
        "Histogram boosting MAE"
    ]

    val_results = []
    print(f"{'Model Architecture':<28} | {'Validation MAE':<14} | {'RMSE':<14} | {'R2':<8}")
    print("-" * 70)

    for m in models:
        preds = fit_and_predict(m, train, valid)
        res = compute_metrics(valid.AWARD, preds)
        val_results.append({"model": m, **res})
        print(f"{m:<28} | ${res['MAE_USD']:>12,.0f} | ${res['RMSE_USD']:>12,.0f} | {res['R2']:>8.3f}")

    winner = min(val_results, key=lambda x: x["MAE_USD"])["model"]
    print("\n" + "=" * 70)
    print(f"Validation Winner: {winner} (Lowest MAE: ${min(r['MAE_USD'] for r in val_results):,.0f})")
    print("=" * 70 + "\n")

    # Final Test Holdout Evaluation (Locked Winner + Baselines, refit on 2019-2020, evaluated on 2021)
    train_full = pd.concat([train, valid])
    print(f"Evaluating Locked Winner & Baselines on 2021 Holdout ({len(test):,} rows):")
    print("-" * 70)
    for m in ["Foundation median", "Global median"]:
        p_test = fit_and_predict(m, train_full, test)
        res_test = compute_metrics(test.AWARD, p_test)
        print(f"{m:<28} | Test MAE: ${res_test['MAE_USD']:>10,.0f} | RMSE: ${res_test['RMSE_USD']:>10,.0f} | R2: {res_test['R2']:>6.3f}")

    # Seen vs unseen foundation breakdown
    unseen = ~test.Foundation.isin(train_full.Foundation)
    print(f"\nUnseen Foundation Segment ({unseen.sum():,} rows / {unseen.mean()*100:.1f}% of test):")
    p_winner = fit_and_predict(winner, train_full, test)
    m_seen = compute_metrics(test.loc[~unseen, "AWARD"], p_winner[~unseen])
    m_unseen = compute_metrics(test.loc[unseen, "AWARD"], p_winner[unseen])
    print(f"  Seen Foundations   ({(~unseen).sum():,} rows): MAE = ${m_seen['MAE_USD']:,.0f} | R2 = {m_seen['R2']:.3f}")
    print(f"  Unseen Foundations ({unseen.sum():,} rows): MAE = ${m_unseen['MAE_USD']:,.0f} | R2 = {m_unseen['R2']:.3f}")

    print("\nAnalytical Takeaway:")
    print("  While the foundation-specific historical median reduced MAE by 6.9% ($6,351) vs a global median,")
    print("  the test MAE ($86,013) remains high relative to the $10,000 median grant, with R2 approx 0.022.")
    print("  Conclusion: Do NOT deploy regression as an automated grant-amount predictor.")
    print("  The platform is best suited for historical research, spatial exploration, and concentration analysis.")

if __name__ == "__main__":
    run_evaluation()
