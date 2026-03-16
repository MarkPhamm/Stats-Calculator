import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import AdaBoostClassifier, AdaBoostRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_classification, make_moons
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, mean_squared_error, r2_score


def main():
    st.title("🔁 AdaBoost (Adaptive Boosting)")

    tab1, tab2 = st.tabs(["📚 Theory & Visualization", "🛠️ Practical Analysis"])

    # ==========================================
    # TAB 1: Theory — fully dynamic
    # ==========================================
    with tab1:
        st.header("How AdaBoost Works")
        st.markdown(r"""
        AdaBoost trains weak learners (stumps) sequentially, **re-weighting** misclassified samples each round.

        **Key formula:** learner weight $\alpha_m = \frac{1}{2}\ln\!\left(\frac{1-\varepsilon_m}{\varepsilon_m}\right)$

        Final prediction: $H(x) = \text{sign}\!\left(\sum_m \alpha_m h_m(x)\right)$
        """)

        st.divider()

        # ── Simulation 1: Decision Boundary vs n_estimators ──────────────
        st.subheader("🗺️ Sim 1 — Decision Boundary Evolution")
        st.caption("Increase estimators to see AdaBoost refine its boundary on the moons dataset.")
        col_ctrl1, col_plot1 = st.columns([1, 2])
        with col_ctrl1:
            n_est_1  = st.slider("n_estimators",  1, 300, 50,  step=5,    key="ada_s1_n")
            noise_1  = st.slider("Noise level",   0.0, 0.4, 0.25, step=0.05, key="ada_s1_noise")
            lr_1     = st.slider("Learning Rate", 0.1, 2.0, 1.0, step=0.1,   key="ada_s1_lr")
            n_samp_1 = st.slider("Samples",       100, 600, 300, step=50,    key="ada_s1_s")
            st.info("Too many estimators on noisy data → overfitting. Watch the boundary become jagged.")

        with col_plot1:
            X1, y1 = make_moons(n_samples=n_samp_1, noise=noise_1, random_state=42)
            model1  = AdaBoostClassifier(n_estimators=n_est_1, learning_rate=lr_1,
                                         random_state=42, algorithm="SAMME")
            model1.fit(X1, y1)
            xx, yy = np.meshgrid(
                np.linspace(X1[:, 0].min() - 0.5, X1[:, 0].max() + 0.5, 200),
                np.linspace(X1[:, 1].min() - 0.5, X1[:, 1].max() + 0.5, 200)
            )
            Z = model1.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
            acc1 = accuracy_score(y1, model1.predict(X1))

            fig1, ax1 = plt.subplots(figsize=(7, 4))
            ax1.contourf(xx, yy, Z, alpha=0.3, cmap="coolwarm")
            ax1.scatter(X1[:, 0], X1[:, 1], c=y1, cmap="coolwarm", edgecolors="k", s=25)
            ax1.set_title(f"Decision Boundary  (n={n_est_1}, LR={lr_1}, acc={acc1:.2%})")
            plt.tight_layout()
            st.pyplot(fig1); plt.close(fig1)

        st.divider()

        # ── Simulation 2: Sample weight evolution ────────────────────────
        st.subheader("⚖️ Sim 2 — Sample Weight Evolution")
        st.caption("Watch how misclassified samples gain weight forcing the next learner to focus on them.")
        col_ctrl2, col_plot2 = st.columns([1, 2])
        with col_ctrl2:
            n_rounds  = st.slider("Rounds to show", 2, 8, 5,   key="ada_s2_r")
            n_pts     = st.slider("Data points",    10, 40, 20, key="ada_s2_n")
            seed_val  = st.slider("Random seed",    0, 99, 42,  key="ada_s2_seed")
            st.info("Misclassified samples (tall bars) get boosted weight so the next stump must focus on them.")

        with col_plot2:
            rng = np.random.RandomState(seed_val)
            n   = n_pts
            Xw  = rng.randn(n, 2)
            yw  = (Xw[:, 0] + Xw[:, 1] > 0).astype(int)
            weights = np.ones(n) / n
            weight_history = [weights.copy()]

            for _ in range(n_rounds - 1):
                stump = DecisionTreeClassifier(max_depth=1)
                stump.fit(Xw, yw, sample_weight=weights)
                pred  = stump.predict(Xw)
                wrong = (pred != yw)
                err   = np.clip(np.dot(weights, wrong) / weights.sum(), 1e-10, 1 - 1e-10)
                alpha = 0.5 * np.log((1 - err) / err)
                weights *= np.exp(alpha * (2 * wrong.astype(float) - 1))
                weights /= weights.sum()
                weight_history.append(weights.copy())

            fig2, axes = plt.subplots(1, n_rounds, figsize=(min(14, n_rounds * 2.5), 3), sharey=True)
            if n_rounds == 1:
                axes = [axes]
            for i, (w, ax) in enumerate(zip(weight_history, axes)):
                colors = ["#FF6B6B" if yi == 1 else "#00AEEF" for yi in yw]
                ax.bar(range(n), w, color=colors, edgecolor="grey", linewidth=0.3)
                ax.set_title(f"Round {i+1}", fontsize=9)
                ax.set_xticks([])
            axes[0].set_ylabel("Weight")
            fig2.suptitle("Weight Evolution  (Red=Class 1, Blue=Class 0)", fontsize=9)
            plt.tight_layout()
            st.pyplot(fig2); plt.close(fig2)

    # ==========================================
    # TAB 2: Practical
    # ==========================================
    with tab2:
        st.header("Train AdaBoost on Your Data")
        uploaded_file = st.file_uploader("Upload CSV/Excel", type=["csv", "xlsx"], key="ada_upload")

        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith(".csv") else pd.read_excel(uploaded_file)
            df = df.fillna(df.median(numeric_only=True))
            st.write("**Data Preview:**", df.head())

            task = st.radio("Task Type", ["Classification", "Regression"], horizontal=True, key="ada_task")
            target_col = st.selectbox("Select Target Column", df.columns, key="ada_target")
            numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns.tolist()
            if target_col in numeric_cols:
                numeric_cols.remove(target_col)
            feature_cols = st.multiselect("Select Feature Columns", numeric_cols, key="ada_features")

            col_a, col_b = st.columns(2)
            n_est  = col_a.slider("n_estimators",  10, 500, 100, key="ada_n_est")
            lr_val = col_b.slider("Learning Rate", 0.01, 2.0, 1.0, key="ada_lr")

            if feature_cols and st.button("🚀 Train AdaBoost"):
                X = df[feature_cols].values
                y = df[target_col].values
                X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)

                if task == "Classification":
                    model = AdaBoostClassifier(n_estimators=n_est, learning_rate=lr_val,
                                               random_state=42, algorithm="SAMME")
                    model.fit(X_tr, y_tr)
                    y_pred = model.predict(X_te)
                    st.success(f"✅ Accuracy: **{accuracy_score(y_te, y_pred):.2%}**")
                    with st.expander("📋 Classification Report"):
                        st.dataframe(pd.DataFrame(classification_report(y_te, y_pred, output_dict=True)).transpose().round(3))

                    st.subheader("📊 Estimator Weights (α values)")
                    fig_w, ax_w = plt.subplots(figsize=(8, 3))
                    ax_w.bar(range(len(model.estimator_weights_)), model.estimator_weights_,
                             color="#9B59B6", alpha=0.8)
                    ax_w.set_xlabel("Estimator Index"); ax_w.set_ylabel("Weight (α)")
                    ax_w.set_title("Weight per Weak Learner")
                    ax_w.grid(axis="y", alpha=0.3)
                    st.pyplot(fig_w); plt.close(fig_w)
                else:
                    model = AdaBoostRegressor(n_estimators=n_est, learning_rate=lr_val, random_state=42)
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