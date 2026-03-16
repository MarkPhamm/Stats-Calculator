import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, mean_squared_error, r2_score


def main():
    st.title("🌲 Random Forest")

    tab1, tab2 = st.tabs(["📚 Theory & Visualization", "🛠️ Practical Analysis"])

    # ==========================================
    # TAB 1: Theory — fully dynamic
    # ==========================================
    with tab1:
        st.header("How Random Forest Works")
        st.markdown("""
        Random Forest is an **ensemble** of many Decision Trees. It fights overfitting through two ideas:

        | Idea | Description |
        |------|-------------|
        | **Bagging** | Each tree trains on a random bootstrap sample of the data |
        | **Feature Randomness** | Each split considers only a random subset of features |

        Final prediction: **majority vote** (classification) or **average** (regression).
        """)

        st.divider()

        # ── Simulation 1: Error vs Number of Trees ───────────────────────
        st.subheader("📉 Sim 1 — Error vs. Number of Trees")
        st.caption("Adjust the sliders and the chart updates instantly.")
        col_ctrl1, col_plot1 = st.columns([1, 2])
        with col_ctrl1:
            n_samples_1  = st.slider("Samples",            100, 1000, 300, step=50, key="rf_s1_n")
            n_features_1 = st.slider("Features",           2,   20,   10,           key="rf_s1_f")
            max_trees    = st.slider("Max trees to test",  10,  200,  100, step=10,  key="rf_s1_t")
            max_d_1      = st.slider("max_depth",          1,   20,   10,            key="rf_s1_d")
            st.info("More trees → lower variance. Error stabilises after ~50 trees.")

        with col_plot1:
            X1, y1 = make_classification(n_samples=n_samples_1, n_features=n_features_1, random_state=42)
            X1_tr, X1_te, y1_tr, y1_te = train_test_split(X1, y1, test_size=0.2, random_state=42)
            est_range = range(1, max_trees + 1, max(1, max_trees // 20))
            train_errs, test_errs = [], []
            for n in est_range:
                rf = RandomForestClassifier(n_estimators=n, max_depth=max_d_1, random_state=42, n_jobs=-1)
                rf.fit(X1_tr, y1_tr)
                train_errs.append(1 - accuracy_score(y1_tr, rf.predict(X1_tr)))
                test_errs.append(1  - accuracy_score(y1_te, rf.predict(X1_te)))

            fig1, ax1 = plt.subplots(figsize=(7, 3.5))
            ax1.plot(list(est_range), train_errs, label="Train Error", color="#00AEEF")
            ax1.plot(list(est_range), test_errs,  label="Test Error",  color="#FF6B6B")
            ax1.set_xlabel("Number of Trees"); ax1.set_ylabel("Error Rate")
            ax1.set_title(f"Error vs. Trees  (depth={max_d_1}, {n_features_1} features)")
            ax1.legend(); ax1.grid(alpha=0.3)
            plt.tight_layout()
            st.pyplot(fig1)
            plt.close(fig1)

        st.divider()

        # ── Simulation 2: Feature Importance ─────────────────────────────
        st.subheader("📊 Sim 2 — Feature Importance Explorer")
        st.caption("Informative features should rank highest. Change signal vs. noise ratio below.")
        col_ctrl2, col_plot2 = st.columns([1, 2])
        with col_ctrl2:
            n_informative = st.slider("Informative features", 1, 10, 4, key="rf_s2_inf")
            n_total_feats = st.slider("Total features",  max(n_informative, 2), 15, max(8, n_informative), key="rf_s2_tot")
            n_trees_imp   = st.slider("n_estimators",    10, 200, 100, step=10, key="rf_s2_n")
            st.info("Blue bars = informative features. Grey = noise. Adjust ratio to see MDI shift.")

        with col_plot2:
            X2, y2 = make_classification(
                n_samples=400, n_features=n_total_feats,
                n_informative=min(n_informative, n_total_feats), random_state=42
            )
            feat_names = [f"F{i+1}" for i in range(n_total_feats)]
            rf2 = RandomForestClassifier(n_estimators=n_trees_imp, random_state=42, n_jobs=-1)
            rf2.fit(X2, y2)
            imp = pd.Series(rf2.feature_importances_, index=feat_names).sort_values(ascending=True)
            threshold = imp.nlargest(min(n_informative, n_total_feats)).min()
            colors = ["#00AEEF" if v >= threshold else "#4A5568" for v in imp]

            fig2, ax2 = plt.subplots(figsize=(7, max(3, n_total_feats * 0.38)))
            imp.plot(kind="barh", ax=ax2, color=colors)
            ax2.set_title(f"Feature Importances  ({n_informative} informative highlighted in blue)")
            ax2.set_xlabel("Importance")
            ax2.grid(axis="x", alpha=0.3)
            plt.tight_layout()
            st.pyplot(fig2)
            plt.close(fig2)

    # ==========================================
    # TAB 2: Practical
    # ==========================================
    with tab2:
        st.header("Train Random Forest on Your Data")
        uploaded_file = st.file_uploader("Upload CSV/Excel", type=["csv", "xlsx"], key="rf_upload")

        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith(".csv") else pd.read_excel(uploaded_file)
            df = df.fillna(df.median(numeric_only=True))
            st.write("**Data Preview:**", df.head())

            task = st.radio("Task Type", ["Classification", "Regression"], horizontal=True, key="rf_task")
            target_col = st.selectbox("Select Target Column", df.columns, key="rf_target")
            numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns.tolist()
            if target_col in numeric_cols:
                numeric_cols.remove(target_col)
            feature_cols = st.multiselect("Select Feature Columns", numeric_cols, key="rf_features")

            col_a, col_b, col_c = st.columns(3)
            n_est     = col_a.slider("n_estimators", 10, 300, 100, key="rf_n_est")
            max_d     = col_b.slider("max_depth",     1,  30,  10, key="rf_depth")
            test_size = col_c.slider("Test Size (%)", 10,  40,  20, key="rf_test") / 100

            if feature_cols and st.button("🚀 Train Random Forest"):
                X = df[feature_cols].values
                y = df[target_col].values
                X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=test_size, random_state=42)

                if task == "Classification":
                    model = RandomForestClassifier(n_estimators=n_est, max_depth=max_d, random_state=42, n_jobs=-1)
                    model.fit(X_tr, y_tr)
                    y_pred = model.predict(X_te)
                    st.success(f"✅ Accuracy: **{accuracy_score(y_te, y_pred):.2%}**")
                    with st.expander("📋 Classification Report"):
                        st.dataframe(pd.DataFrame(classification_report(y_te, y_pred, output_dict=True)).transpose().round(3))
                else:
                    model = RandomForestRegressor(n_estimators=n_est, max_depth=max_d, random_state=42, n_jobs=-1)
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
                sns.barplot(data=imp_df, x="Importance", y="Feature", palette="Blues_r", ax=ax_i)
                st.pyplot(fig_i); plt.close(fig_i)