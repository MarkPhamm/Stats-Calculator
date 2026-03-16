import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score, classification_report, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

try:
    import xgboost as xgb
    XGB_AVAILABLE = True
except ImportError:
    XGB_AVAILABLE = False


def main():
    st.title("⚡ XGBoost (Extreme Gradient Boosting)")

    if not XGB_AVAILABLE:
        st.error("XGBoost is not installed. Run `pip install xgboost` and restart.")
        return

    tab1, tab2 = st.tabs(["📚 Theory & Visualization", "🛠️ Practical Analysis"])

    # ==========================================
    # TAB 1: Theory — fully dynamic
    # ==========================================
    with tab1:
        st.header("What Makes XGBoost Special?")
        st.markdown(r"""
        XGBoost is an **optimised, regularised** Gradient Boosting framework.

        | Feature | Description |
        |---------|-------------|
        | **Regularisation** | L1 + L2 terms prevent overfitting |
        | **2nd-order gradients** | Uses Hessian (Newton's method) for faster convergence |
        | **Tree pruning** | Removes nodes with negative gain (`gamma`) |
        | **Parallel splits** | Column-block structure enables parallelism |
        | **Missing values** | Learns optimal default direction automatically |
        """)

        st.divider()

        # ── Simulation 1: Learning Curves ────────────────────────────────
        st.subheader("📉 Sim 1 — Train vs. Test Loss Curves")
        st.caption("Tune parameters and observe how log-loss evolves over boosting rounds.")
        col_ctrl1, col_plot1 = st.columns([1, 2])
        with col_ctrl1:
            n_est_1  = st.slider("n_estimators",   10, 300, 100, step=10,   key="xgb_s1_n")
            lr_1     = st.slider("Learning Rate",  0.01, 0.5, 0.1, step=0.01, key="xgb_s1_lr")
            depth_1  = st.slider("max_depth",      1, 10, 3,                key="xgb_s1_d")
            subsamp  = st.slider("subsample",      0.4, 1.0, 0.8, step=0.05, key="xgb_s1_sub")
            st.info("Watch for the point where test loss stops decreasing — that's your ideal n_estimators.")

        with col_plot1:
            X1, y1 = make_classification(n_samples=400, n_features=12, random_state=42)
            X1_tr, X1_te, y1_tr, y1_te = train_test_split(X1, y1, test_size=0.25, random_state=42)
            m1 = xgb.XGBClassifier(n_estimators=n_est_1, learning_rate=lr_1, max_depth=depth_1,
                                    subsample=subsamp, eval_metric="logloss",
                                    random_state=42, verbosity=0)
            m1.fit(X1_tr, y1_tr,
                   eval_set=[(X1_tr, y1_tr), (X1_te, y1_te)], verbose=False)
            res = m1.evals_result()

            fig1, ax1 = plt.subplots(figsize=(7, 3.5))
            ax1.plot(res["validation_0"]["logloss"], label="Train Loss", color="#00AEEF")
            ax1.plot(res["validation_1"]["logloss"], label="Test Loss",  color="#FF6B6B")
            best_r = int(np.argmin(res["validation_1"]["logloss"]))
            ax1.axvline(best_r, color="green", linestyle="--", alpha=0.7,
                        label=f"Best round: {best_r+1}")
            ax1.set_xlabel("Round"); ax1.set_ylabel("Log Loss")
            ax1.set_title(f"XGBoost Loss Curves  LR={lr_1}, depth={depth_1}, sub={subsamp}")
            ax1.legend(fontsize=8); ax1.grid(alpha=0.3)
            plt.tight_layout()
            st.pyplot(fig1); plt.close(fig1)

        st.divider()

        # ── Simulation 2: Regularisation effect ─────────────────────────
        st.subheader("🛡️ Sim 2 — L1 vs L2 Regularisation")
        st.caption("Slide the regularisation strength and see how test accuracy responds.")
        col_ctrl2, col_plot2 = st.columns([1, 2])
        with col_ctrl2:
            n_informative_2 = st.slider("Informative features", 2, 15, 5, key="xgb_s2_inf")
            n_est_2  = st.slider("n_estimators",  20, 200, 80, step=10, key="xgb_s2_n")
            alpha_max = st.slider("Max α / λ to test", 1, 20, 10,       key="xgb_s2_max")
            st.info("Strong regularisation helps on noisy data but can underfit if too aggressive.")

        with col_plot2:
            X2, y2 = make_classification(n_samples=500, n_features=20,
                                          n_informative=n_informative_2, random_state=42)
            X2_tr, X2_te, y2_tr, y2_te = train_test_split(X2, y2, test_size=0.2, random_state=42)
            alphas = np.linspace(0, alpha_max, 12)
            l1_accs, l2_accs = [], []
            for a in alphas:
                m_l1 = xgb.XGBClassifier(n_estimators=n_est_2, reg_alpha=float(a), reg_lambda=0.0,
                                          verbosity=0, random_state=42)
                m_l1.fit(X2_tr, y2_tr)
                l1_accs.append(accuracy_score(y2_te, m_l1.predict(X2_te)))

                m_l2 = xgb.XGBClassifier(n_estimators=n_est_2, reg_alpha=0.0, reg_lambda=float(a),
                                          verbosity=0, random_state=42)
                m_l2.fit(X2_tr, y2_tr)
                l2_accs.append(accuracy_score(y2_te, m_l2.predict(X2_te)))

            fig2, ax2 = plt.subplots(figsize=(7, 3.5))
            ax2.plot(alphas, l1_accs, marker="o", label="L1 (reg_alpha)", color="#00AEEF")
            ax2.plot(alphas, l2_accs, marker="s", label="L2 (reg_lambda)", color="#9B59B6")
            ax2.set_xlabel("Regularisation Strength"); ax2.set_ylabel("Test Accuracy")
            ax2.set_title(f"L1 vs L2  ({n_informative_2} informative / 20 total features)")
            ax2.legend(); ax2.grid(alpha=0.3)
            plt.tight_layout()
            st.pyplot(fig2); plt.close(fig2)

    # ==========================================
    # TAB 2: Practical
    # ==========================================
    with tab2:
        st.header("Train XGBoost on Your Data")
        uploaded_file = st.file_uploader("Upload CSV/Excel", type=["csv", "xlsx"], key="xgb_upload")

        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith(".csv") else pd.read_excel(uploaded_file)
            df = df.fillna(df.median(numeric_only=True))
            st.write("**Data Preview:**", df.head())

            task = st.radio("Task Type", ["Classification", "Regression"], horizontal=True, key="xgb_task")
            target_col = st.selectbox("Select Target Column", df.columns, key="xgb_target")
            numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns.tolist()
            if target_col in numeric_cols:
                numeric_cols.remove(target_col)
            feature_cols = st.multiselect("Select Feature Columns", numeric_cols, key="xgb_features")

            col_a, col_b, col_c, col_d = st.columns(4)
            n_est   = col_a.slider("n_estimators",  10, 500, 100, key="xgb_n")
            lr_val  = col_b.slider("Learning Rate", 0.01, 0.5, 0.1, key="xgb_lr")
            max_d   = col_c.slider("max_depth",      1, 15, 3,    key="xgb_depth")
            sub     = col_d.slider("subsample",      0.4, 1.0, 0.8, key="xgb_sub")

            with st.expander("⚙️ Regularisation"):
                cr1, cr2 = st.columns(2)
                reg_alpha  = cr1.number_input("reg_alpha (L1)",  0.0, 10.0, 0.0, key="xgb_alpha")
                reg_lambda = cr2.number_input("reg_lambda (L2)", 0.0, 10.0, 1.0, key="xgb_lambda")

            if feature_cols and st.button("🚀 Train XGBoost"):
                X = df[feature_cols].values
                y = df[target_col].values
                X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)

                if task == "Classification":
                    model = xgb.XGBClassifier(n_estimators=n_est, learning_rate=lr_val,
                                              max_depth=max_d, subsample=sub,
                                              reg_alpha=reg_alpha, reg_lambda=reg_lambda,
                                              random_state=42, verbosity=0,
                                              eval_metric="logloss")
                    model.fit(X_tr, y_tr, eval_set=[(X_tr, y_tr), (X_te, y_te)], verbose=False)
                    y_pred = model.predict(X_te)
                    st.success(f"✅ Accuracy: **{accuracy_score(y_te, y_pred):.2%}**")
                    with st.expander("📋 Classification Report"):
                        st.dataframe(pd.DataFrame(classification_report(y_te, y_pred, output_dict=True)).transpose().round(3))

                    st.subheader("📈 Loss Curve on Your Data")
                    res = model.evals_result()
                    fig_lc, ax_lc = plt.subplots()
                    ax_lc.plot(res["validation_0"]["logloss"], label="Train")
                    ax_lc.plot(res["validation_1"]["logloss"], label="Test")
                    ax_lc.set_xlabel("Round"); ax_lc.set_ylabel("Log Loss")
                    ax_lc.legend(); ax_lc.grid(alpha=0.3)
                    st.pyplot(fig_lc); plt.close(fig_lc)
                else:
                    model = xgb.XGBRegressor(n_estimators=n_est, learning_rate=lr_val,
                                             max_depth=max_d, subsample=sub,
                                             reg_alpha=reg_alpha, reg_lambda=reg_lambda,
                                             random_state=42, verbosity=0)
                    model.fit(X_tr, y_tr)
                    y_pred = model.predict(X_te)
                    c1, c2 = st.columns(2)
                    c1.metric("R² Score", f"{r2_score(y_te, y_pred):.4f}")
                    c2.metric("RMSE",     f"{np.sqrt(mean_squared_error(y_te, y_pred)):.4f}")
                    fig_p, ax_p = plt.subplots()
                    ax_p.scatter(y_te, y_pred, alpha=0.6, color="#00AEEF")
                    ax_p.plot([y_te.min(), y_te.max()], [y_te.min(), y_te.max()], "r--")
                    ax_p.set_xlabel("Actual"); ax_p.set_ylabel("Predicted")
                    st.pyplot(fig_p); plt.close(fig_p)

                st.subheader("🏆 Feature Importances")
                imp_df = pd.DataFrame({"Feature": feature_cols, "Importance": model.feature_importances_}).sort_values("Importance", ascending=False)
                fig_i, ax_i = plt.subplots(figsize=(8, max(3, len(feature_cols) * 0.4)))
                sns.barplot(data=imp_df, x="Importance", y="Feature", palette="YlOrRd_r", ax=ax_i)
                st.pyplot(fig_i); plt.close(fig_i)