import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import GradientBoostingClassifier, GradientBoostingRegressor
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, mean_squared_error, r2_score


def main():
    st.title("📈 Gradient Boosting")

    tab1, tab2 = st.tabs(["📚 Theory & Visualization", "🛠️ Practical Analysis"])

    # ==========================================
    # TAB 1: Theory — fully dynamic
    # ==========================================
    with tab1:
        st.header("How Gradient Boosting Works")
        st.markdown(r"""
        Gradient Boosting builds trees **sequentially**. Each new tree corrects the **residual errors** of the current ensemble.

        **Update rule:**  $F_m(x) = F_{m-1}(x) + \eta \cdot h_m(x)$

        where $\eta$ is the **learning rate** and $h_m$ is a shallow tree fitted to the residuals.
        """)

        st.divider()

        # ── Simulation 1: Staged accuracy ────────────────────────────────
        st.subheader("📉 Sim 1 — Staged Learning Curve")
        st.caption("Adjust parameters and watch how train/test accuracy evolves across boosting rounds.")
        col_ctrl1, col_plot1 = st.columns([1, 2])
        with col_ctrl1:
            n_est_1 = st.slider("n_estimators",   10, 300, 100, step=10,  key="gb_s1_n")
            lr_1    = st.slider("Learning Rate",  0.01, 1.0, 0.1, step=0.01, key="gb_s1_lr")
            depth_1 = st.slider("max_depth",      1, 8,  3,              key="gb_s1_d")
            n_samp  = st.slider("Samples",        100, 800, 400, step=50, key="gb_s1_s")
            st.info("Lower LR = smoother curve that often peaks later. High LR = fast but may overfit.")

        with col_plot1:
            X1, y1 = make_classification(n_samples=n_samp, n_features=10, random_state=42)
            X1_tr, X1_te, y1_tr, y1_te = train_test_split(X1, y1, test_size=0.25, random_state=42)
            gb1 = GradientBoostingClassifier(n_estimators=n_est_1, learning_rate=lr_1,
                                              max_depth=depth_1, random_state=42)
            gb1.fit(X1_tr, y1_tr)
            train_sc = [accuracy_score(y1_tr, p) for p in gb1.staged_predict(X1_tr)]
            test_sc  = [accuracy_score(y1_te, p) for p in gb1.staged_predict(X1_te)]
            best_idx = int(np.argmax(test_sc))

            fig1, ax1 = plt.subplots(figsize=(7, 3.5))
            ax1.plot(train_sc, label="Train", color="#00AEEF")
            ax1.plot(test_sc,  label="Test",  color="#FF6B6B")
            ax1.axvline(best_idx, color="green", linestyle="--", alpha=0.7,
                        label=f"Best stage: {best_idx+1} ({test_sc[best_idx]:.2%})")
            ax1.set_xlabel("Boosting Stage"); ax1.set_ylabel("Accuracy")
            ax1.set_title(f"Learning Curve  LR={lr_1}, depth={depth_1}")
            ax1.legend(fontsize=8); ax1.grid(alpha=0.3)
            plt.tight_layout()
            st.pyplot(fig1); plt.close(fig1)

        st.divider()

        # ── Simulation 2: Learning Rate comparison ───────────────────────
        st.subheader("📊 Sim 2 — Learning Rate Comparison")
        st.caption("Choose which learning rates to compare side-by-side.")
        col_ctrl2, col_plot2 = st.columns([1, 2])
        with col_ctrl2:
            n_est_2  = st.slider("n_estimators", 20, 300, 100, step=10, key="gb_s2_n")
            depth_2  = st.slider("max_depth",    1,  8,   3,            key="gb_s2_d")
            lr_options = [0.01, 0.05, 0.1, 0.2, 0.5, 1.0]
            selected_lrs = st.multiselect("Learning rates to compare", lr_options,
                                          default=[0.01, 0.1, 0.5, 1.0], key="gb_s2_lrs")
            st.info("High LR converges fast but overshoots. Low LR needs more stages.")

        with col_plot2:
            if selected_lrs:
                X2, y2 = make_classification(n_samples=400, n_features=10, random_state=42)
                X2_tr, X2_te, y2_tr, y2_te = train_test_split(X2, y2, test_size=0.25, random_state=42)
                fig2, ax2 = plt.subplots(figsize=(7, 3.5))
                for lr in sorted(selected_lrs):
                    gb2 = GradientBoostingClassifier(n_estimators=n_est_2, learning_rate=lr,
                                                      max_depth=depth_2, random_state=42)
                    gb2.fit(X2_tr, y2_tr)
                    scores = [accuracy_score(y2_te, p) for p in gb2.staged_predict(X2_te)]
                    ax2.plot(scores, label=f"LR={lr}")
                ax2.set_xlabel("Boosting Stage"); ax2.set_ylabel("Test Accuracy")
                ax2.set_title(f"Effect of Learning Rate  (depth={depth_2})")
                ax2.legend(fontsize=8); ax2.grid(alpha=0.3)
                plt.tight_layout()
                st.pyplot(fig2); plt.close(fig2)
            else:
                st.warning("Select at least one learning rate.")

    # ==========================================
    # TAB 2: Practical
    # ==========================================
    with tab2:
        st.header("Train Gradient Boosting on Your Data")
        uploaded_file = st.file_uploader("Upload CSV/Excel", type=["csv", "xlsx"], key="gb_upload")

        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith(".csv") else pd.read_excel(uploaded_file)
            df = df.fillna(df.median(numeric_only=True))
            st.write("**Data Preview:**", df.head())

            task = st.radio("Task Type", ["Classification", "Regression"], horizontal=True, key="gb_task")
            target_col = st.selectbox("Select Target Column", df.columns, key="gb_target")
            numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns.tolist()
            if target_col in numeric_cols:
                numeric_cols.remove(target_col)
            feature_cols = st.multiselect("Select Feature Columns", numeric_cols, key="gb_features")

            col_a, col_b, col_c = st.columns(3)
            n_est  = col_a.slider("n_estimators",  10, 500, 100, key="gb_n_est")
            lr_val = col_b.slider("Learning Rate", 0.01, 1.0, 0.1, key="gb_lr")
            max_d  = col_c.slider("max_depth",     1, 10, 3, key="gb_depth")

            if feature_cols and st.button("🚀 Train Gradient Boosting"):
                X = df[feature_cols].values
                y = df[target_col].values
                X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)

                if task == "Classification":
                    model = GradientBoostingClassifier(n_estimators=n_est, learning_rate=lr_val,
                                                       max_depth=max_d, random_state=42)
                    model.fit(X_tr, y_tr)
                    y_pred = model.predict(X_te)
                    st.success(f"✅ Accuracy: **{accuracy_score(y_te, y_pred):.2%}**")
                    with st.expander("📋 Classification Report"):
                        st.dataframe(pd.DataFrame(classification_report(y_te, y_pred, output_dict=True)).transpose().round(3))

                    st.subheader("📈 Learning Curve on Your Data")
                    staged = [accuracy_score(y_te, p) for p in model.staged_predict(X_te)]
                    fig_lc, ax_lc = plt.subplots()
                    ax_lc.plot(staged, color="#00AEEF")
                    ax_lc.set_xlabel("Boosting Stage"); ax_lc.set_ylabel("Test Accuracy")
                    ax_lc.grid(alpha=0.3)
                    st.pyplot(fig_lc); plt.close(fig_lc)
                else:
                    model = GradientBoostingRegressor(n_estimators=n_est, learning_rate=lr_val,
                                                      max_depth=max_d, random_state=42)
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
                sns.barplot(data=imp_df, x="Importance", y="Feature", palette="Oranges_r", ax=ax_i)
                st.pyplot(fig_i); plt.close(fig_i)