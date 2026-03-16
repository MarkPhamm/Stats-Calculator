import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score, classification_report, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

try:
    from catboost import CatBoostClassifier, CatBoostRegressor
    CB_AVAILABLE = True
except ImportError:
    CB_AVAILABLE = False


def main():
    st.title("🐱 CatBoost (Categorical Boosting)")

    if not CB_AVAILABLE:
        st.error("CatBoost is not installed. Run `pip install catboost` and restart.")
        return

    tab1, tab2 = st.tabs(["📚 Theory & Visualization", "🛠️ Practical Analysis"])

    # ==========================================
    # TAB 1: Theory — fully dynamic
    # ==========================================
    with tab1:
        st.header("What Makes CatBoost Unique?")
        st.markdown(r"""
        CatBoost stands out for **native categorical handling** and **ordered boosting** to eliminate target leakage.

        | Feature | Description |
        |---------|-------------|
        | **Ordered Boosting** | Each sample scored using only preceding samples — no leakage |
        | **Native Categoricals** | Target Statistics encoding; no manual OHE needed |
        | **Symmetric Trees** | Balanced splits → fast prediction, good generalisation |
        | **Minimal Tuning** | Strong defaults, competitive out of the box |
        """)

        st.divider()

        # ── Simulation 1: Depth vs Accuracy ──────────────────────────────
        st.subheader("🌳 Sim 1 — Tree Depth vs Accuracy")
        st.caption("CatBoost uses symmetric (oblivious) trees — every node at the same depth shares the same split.")
        col_ctrl1, col_plot1 = st.columns([1, 2])
        with col_ctrl1:
            n_iter_1  = st.slider("iterations",    20, 300, 100, step=10, key="cb_s1_iter")
            lr_1      = st.slider("Learning Rate", 0.01, 0.5, 0.05, step=0.01, key="cb_s1_lr")
            n_samp_1  = st.slider("Samples",       200, 1000, 500, step=50,    key="cb_s1_s")
            max_depth_test = st.slider("Max depth to test", 2, 12, 10,         key="cb_s1_maxd")
            st.info("Default depth=6 is usually a sweet spot. Deeper trees can overfit with CatBoost's symmetric structure.")

        with col_plot1:
            X1, y1 = make_classification(n_samples=n_samp_1, n_features=12, random_state=42)
            X1_tr, X1_te, y1_tr, y1_te = train_test_split(X1, y1, test_size=0.2, random_state=42)
            depths = list(range(1, max_depth_test + 1))
            accs   = []
            for d in depths:
                m = CatBoostClassifier(depth=d, iterations=n_iter_1, learning_rate=lr_1,
                                       verbose=0, random_seed=42)
                m.fit(X1_tr, y1_tr)
                accs.append(accuracy_score(y1_te, m.predict(X1_te)))

            fig1, ax1 = plt.subplots(figsize=(7, 3.5))
            ax1.plot(depths, accs, marker="o", color="#E74C3C")
            ax1.set_xlabel("Tree Depth"); ax1.set_ylabel("Test Accuracy")
            ax1.set_title(f"CatBoost: Depth vs Accuracy  (iter={n_iter_1}, LR={lr_1})")
            ax1.grid(alpha=0.3)
            plt.tight_layout()
            st.pyplot(fig1); plt.close(fig1)

        st.divider()

        # ── Simulation 2: Learning Curve ──────────────────────────────────
        st.subheader("📉 Sim 2 — Learning Curve")
        st.caption("Train and test log-loss tracked across all iterations via get_evals_result().")
        col_ctrl2, col_plot2 = st.columns([1, 2])
        with col_ctrl2:
            n_iter_2  = st.slider("iterations",    20, 500, 200, step=10,    key="cb_s2_iter")
            lr_2      = st.slider("Learning Rate", 0.01, 0.5, 0.05, step=0.01, key="cb_s2_lr")
            depth_2   = st.slider("depth",         1, 10, 6,                 key="cb_s2_d")
            l2_leaf   = st.slider("l2_leaf_reg",   0.0, 10.0, 3.0, step=0.5, key="cb_s2_l2")
            st.info("l2_leaf_reg is CatBoost's L2 regularisation. Increase it to flatten the train curve and close the gap.")

        with col_plot2:
            X2, y2 = make_classification(n_samples=600, n_features=12, random_state=42)
            X2_tr, X2_te, y2_tr, y2_te = train_test_split(X2, y2, test_size=0.25, random_state=42)
            m2 = CatBoostClassifier(iterations=n_iter_2, learning_rate=lr_2,
                                    depth=depth_2, l2_leaf_reg=l2_leaf,
                                    verbose=0, random_seed=42)
            m2.fit(X2_tr, y2_tr, eval_set=(X2_te, y2_te), plot=False)
            evals      = m2.get_evals_result()
            train_loss = evals["learn"]["Logloss"]
            test_loss  = evals["validation"]["Logloss"]
            best_it    = int(np.argmin(test_loss))

            fig2, ax2 = plt.subplots(figsize=(7, 3.5))
            ax2.plot(train_loss, label="Train Loss", color="#E74C3C")
            ax2.plot(test_loss,  label="Test Loss",  color="#F39C12")
            ax2.axvline(best_it, color="green", linestyle="--", alpha=0.7,
                        label=f"Best iter: {best_it+1}")
            ax2.set_xlabel("Iteration"); ax2.set_ylabel("Log Loss")
            ax2.set_title(f"Learning Curve  depth={depth_2}, LR={lr_2}, L2={l2_leaf}")
            ax2.legend(fontsize=8); ax2.grid(alpha=0.3)
            plt.tight_layout()
            st.pyplot(fig2); plt.close(fig2)

    # ==========================================
    # TAB 2: Practical
    # ==========================================
    with tab2:
        st.header("Train CatBoost on Your Data")
        st.info("💡 CatBoost handles categorical columns natively — no encoding required!")

        uploaded_file = st.file_uploader("Upload CSV/Excel", type=["csv", "xlsx"], key="cb_upload")

        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith(".csv") else pd.read_excel(uploaded_file)
            df = df.fillna(df.median(numeric_only=True))
            st.write("**Data Preview:**", df.head())

            task = st.radio("Task Type", ["Classification", "Regression"], horizontal=True, key="cb_task")
            target_col = st.selectbox("Select Target Column", df.columns, key="cb_target")
            all_cols = [c for c in df.columns if c != target_col]
            feature_cols = st.multiselect("Select Feature Columns", all_cols, key="cb_features")

            if feature_cols:
                cat_candidates = df[feature_cols].select_dtypes(include=["object", "category"]).columns.tolist()
                cat_features   = st.multiselect("Categorical Columns (auto-detected)",
                                                cat_candidates, default=cat_candidates, key="cb_cat")

            col_a, col_b, col_c = st.columns(3)
            iterations = col_a.slider("iterations",    50, 1000, 200, key="cb_iter")
            lr_val     = col_b.slider("Learning Rate", 0.01, 0.5, 0.05, key="cb_lr")
            depth      = col_c.slider("depth",         2, 10, 6,   key="cb_depth")

            if feature_cols and st.button("🚀 Train CatBoost"):
                X = df[feature_cols].copy()
                y = df[target_col].values
                for col in X.select_dtypes(include="object").columns:
                    if col not in cat_features:
                        X[col] = LabelEncoder().fit_transform(X[col].astype(str))

                X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
                cat_idx = [X_tr.columns.tolist().index(c) for c in cat_features if c in X_tr.columns]

                if task == "Classification":
                    model = CatBoostClassifier(iterations=iterations, learning_rate=lr_val,
                                               depth=depth, cat_features=cat_idx,
                                               verbose=0, random_seed=42)
                    model.fit(X_tr, y_tr, eval_set=(X_te, y_te), plot=False)
                    y_pred = model.predict(X_te)
                    st.success(f"✅ Accuracy: **{accuracy_score(y_te, y_pred):.2%}**")
                    with st.expander("📋 Classification Report"):
                        st.dataframe(pd.DataFrame(classification_report(y_te, y_pred, output_dict=True)).transpose().round(3))
                else:
                    model = CatBoostRegressor(iterations=iterations, learning_rate=lr_val,
                                              depth=depth, cat_features=cat_idx,
                                              verbose=0, random_seed=42)
                    model.fit(X_tr, y_tr, eval_set=(X_te, y_te), plot=False)
                    y_pred = model.predict(X_te)
                    c1, c2 = st.columns(2)
                    c1.metric("R² Score", f"{r2_score(y_te, y_pred):.4f}")
                    c2.metric("RMSE",     f"{np.sqrt(mean_squared_error(y_te, y_pred)):.4f}")
                    fig_p, ax_p = plt.subplots()
                    ax_p.scatter(y_te, y_pred, alpha=0.6, color="#E74C3C")
                    ax_p.plot([y_te.min(), y_te.max()], [y_te.min(), y_te.max()], "b--")
                    ax_p.set_xlabel("Actual"); ax_p.set_ylabel("Predicted")
                    st.pyplot(fig_p); plt.close(fig_p)

                st.subheader("🏆 Feature Importances")
                imp_df = pd.DataFrame({"Feature": feature_cols, "Importance": model.get_feature_importance()}).sort_values("Importance", ascending=False)
                fig_i, ax_i = plt.subplots(figsize=(8, max(3, len(feature_cols) * 0.4)))
                sns.barplot(data=imp_df, x="Importance", y="Feature", palette="Reds_r", ax=ax_i)
                ax_i.set_title("Feature Importances (PredictionValuesChange)")
                st.pyplot(fig_i); plt.close(fig_i)