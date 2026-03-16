import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
from sklearn.datasets import make_classification
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    mean_squared_error,
    r2_score,
)
from sklearn.model_selection import train_test_split

try:
    import lightgbm as lgb

    LGB_AVAILABLE = True
except ImportError:
    LGB_AVAILABLE = False


def main():
    st.title("🌿 LightGBM (Light Gradient Boosting Machine)")

    if not LGB_AVAILABLE:
        st.error("LightGBM is not installed. Run `pip install lightgbm` and restart.")
        return

    tab1, tab2 = st.tabs(["📚 Theory & Visualization", "🛠️ Practical Analysis"])

    # ==========================================
    # TAB 1: Theory — fully dynamic
    # ==========================================
    with tab1:
        st.header("What Makes LightGBM Fast?")
        st.markdown("""
        LightGBM optimises for **speed** and **memory** with two core innovations:

        | Technique | What it does |
        |-----------|-------------|
        | **GOSS** | Keeps high-gradient samples; randomly drops easy ones |
        | **EFB**  | Bundles mutually exclusive sparse features |

        It grows trees **leaf-wise** (best-first) instead of level-wise, achieving lower loss with fewer splits.
        """)

        st.divider()

        # ── Simulation 1: num_leaves vs Accuracy ─────────────────────────
        st.subheader("🍃 Sim 1 — num_leaves vs Accuracy")
        st.caption(
            "num_leaves controls model complexity in LightGBM's leaf-wise growth."
        )
        col_ctrl1, col_plot1 = st.columns([1, 2])
        with col_ctrl1:
            n_est_1 = st.slider("n_estimators", 10, 300, 100, step=10, key="lgb_s1_n")
            lr_1 = st.slider(
                "Learning Rate", 0.01, 0.5, 0.05, step=0.01, key="lgb_s1_lr"
            )
            n_samp_1 = st.slider("Samples", 200, 1000, 500, step=50, key="lgb_s1_s")
            max_leaves = st.slider(
                "Max num_leaves to test", 4, 256, 128, step=4, key="lgb_s1_max"
            )
            st.info(
                "Beyond a sweet spot, more leaves overfit. Rule: num_leaves < 2^max_depth."
            )

        with col_plot1:
            X1, y1 = make_classification(
                n_samples=n_samp_1, n_features=10, random_state=42
            )
            X1_tr, X1_te, y1_tr, y1_te = train_test_split(
                X1, y1, test_size=0.2, random_state=42
            )
            leaf_range = list(range(4, max_leaves + 1, max(1, max_leaves // 16)))
            accs = []
            for nl in leaf_range:
                m = lgb.LGBMClassifier(
                    n_estimators=n_est_1,
                    num_leaves=nl,
                    learning_rate=lr_1,
                    verbose=-1,
                    random_state=42,
                )
                m.fit(X1_tr, y1_tr)
                accs.append(accuracy_score(y1_te, m.predict(X1_te)))

            fig1, ax1 = plt.subplots(figsize=(7, 3.5))
            ax1.plot(leaf_range, accs, marker="o", color="#2ECC71")
            ax1.set_xlabel("num_leaves")
            ax1.set_ylabel("Test Accuracy")
            ax1.set_title(f"Accuracy vs num_leaves  (LR={lr_1}, n_est={n_est_1})")
            ax1.grid(alpha=0.3)
            plt.tight_layout()
            st.pyplot(fig1)
            plt.close(fig1)

        st.divider()

        # ── Simulation 2: Learning Curves with early stopping ────────────
        st.subheader("📉 Sim 2 — Learning Curve with Early Stopping")
        st.caption(
            "See where the test loss bottoms out — that's where early stopping would fire."
        )
        col_ctrl2, col_plot2 = st.columns([1, 2])
        with col_ctrl2:
            n_est_2 = st.slider("n_estimators", 20, 500, 200, step=10, key="lgb_s2_n")
            lr_2 = st.slider(
                "Learning Rate", 0.01, 0.3, 0.05, step=0.01, key="lgb_s2_lr"
            )
            num_leaves_2 = st.slider("num_leaves", 4, 128, 31, key="lgb_s2_leaves")
            min_child_2 = st.slider("min_child_samples", 5, 100, 20, key="lgb_s2_child")
            st.info(
                "The gap between train and test loss reveals overfitting. Raise min_child_samples to reduce it."
            )

        with col_plot2:
            X2, y2 = make_classification(n_samples=600, n_features=12, random_state=42)
            X2_tr, X2_te, y2_tr, y2_te = train_test_split(
                X2, y2, test_size=0.25, random_state=42
            )
            callbacks = [
                lgb.early_stopping(30, verbose=False),
                lgb.log_evaluation(period=-1),
            ]
            m2 = lgb.LGBMClassifier(
                n_estimators=n_est_2,
                learning_rate=lr_2,
                num_leaves=num_leaves_2,
                min_child_samples=min_child_2,
                verbose=-1,
                random_state=42,
            )
            m2.fit(
                X2_tr,
                y2_tr,
                eval_set=[(X2_tr, y2_tr), (X2_te, y2_te)],
                callbacks=callbacks,
            )
            evals = m2.evals_result_
            train_loss = evals["training"]["binary_logloss"]
            test_loss = evals["valid_1"]["binary_logloss"]
            best_it = m2.best_iteration_

            fig2, ax2 = plt.subplots(figsize=(7, 3.5))
            ax2.plot(train_loss, label="Train Loss", color="#2ECC71")
            ax2.plot(test_loss, label="Test Loss", color="#E74C3C")
            if best_it and best_it > 0:
                ax2.axvline(
                    best_it - 1,
                    color="orange",
                    linestyle="--",
                    alpha=0.8,
                    label=f"Early stop: {best_it}",
                )
            ax2.set_xlabel("Round")
            ax2.set_ylabel("Log Loss")
            ax2.set_title(f"Learning Curve  leaves={num_leaves_2}, LR={lr_2}")
            ax2.legend(fontsize=8)
            ax2.grid(alpha=0.3)
            plt.tight_layout()
            st.pyplot(fig2)
            plt.close(fig2)

    # ==========================================
    # TAB 2: Practical
    # ==========================================
    with tab2:
        st.header("Train LightGBM on Your Data")
        uploaded_file = st.file_uploader(
            "Upload CSV/Excel", type=["csv", "xlsx"], key="lgb_upload"
        )

        if uploaded_file is not None:
            df = (
                pd.read_csv(uploaded_file)
                if uploaded_file.name.endswith(".csv")
                else pd.read_excel(uploaded_file)
            )
            df = df.fillna(df.median(numeric_only=True))
            st.write("**Data Preview:**", df.head())

            task = st.radio(
                "Task Type",
                ["Classification", "Regression"],
                horizontal=True,
                key="lgb_task",
            )
            target_col = st.selectbox(
                "Select Target Column", df.columns, key="lgb_target"
            )
            numeric_cols = df.select_dtypes(
                include=["float64", "int64"]
            ).columns.tolist()
            if target_col in numeric_cols:
                numeric_cols.remove(target_col)
            feature_cols = st.multiselect(
                "Select Feature Columns", numeric_cols, key="lgb_features"
            )

            col_a, col_b, col_c, col_d = st.columns(4)
            n_est = col_a.slider("n_estimators", 10, 500, 100, key="lgb_n")
            lr_val = col_b.slider("Learning Rate", 0.01, 0.5, 0.05, key="lgb_lr")
            num_leaves = col_c.slider("num_leaves", 10, 200, 31, key="lgb_leaves")
            min_child = col_d.slider("min_child_samples", 5, 100, 20, key="lgb_child")

            if feature_cols and st.button("🚀 Train LightGBM"):
                X = df[feature_cols].values
                y = df[target_col].values
                X_tr, X_te, y_tr, y_te = train_test_split(
                    X, y, test_size=0.2, random_state=42
                )
                callbacks = [
                    lgb.early_stopping(50, verbose=False),
                    lgb.log_evaluation(period=-1),
                ]

                if task == "Classification":
                    model = lgb.LGBMClassifier(
                        n_estimators=n_est,
                        learning_rate=lr_val,
                        num_leaves=num_leaves,
                        min_child_samples=min_child,
                        random_state=42,
                        verbose=-1,
                    )
                    model.fit(X_tr, y_tr, eval_set=[(X_te, y_te)], callbacks=callbacks)
                    y_pred = model.predict(X_te)
                    st.success(
                        f"✅ Accuracy: **{accuracy_score(y_te, y_pred):.2%}**  (best iter: {model.best_iteration_})"
                    )
                    with st.expander("📋 Classification Report"):
                        st.dataframe(
                            pd.DataFrame(
                                classification_report(y_te, y_pred, output_dict=True)
                            )
                            .transpose()
                            .round(3)
                        )
                else:
                    model = lgb.LGBMRegressor(
                        n_estimators=n_est,
                        learning_rate=lr_val,
                        num_leaves=num_leaves,
                        min_child_samples=min_child,
                        random_state=42,
                        verbose=-1,
                    )
                    model.fit(X_tr, y_tr, eval_set=[(X_te, y_te)], callbacks=callbacks)
                    y_pred = model.predict(X_te)
                    c1, c2 = st.columns(2)
                    c1.metric("R² Score", f"{r2_score(y_te, y_pred):.4f}")
                    c2.metric(
                        "RMSE", f"{np.sqrt(mean_squared_error(y_te, y_pred)):.4f}"
                    )
                    fig_p, ax_p = plt.subplots()
                    ax_p.scatter(y_te, y_pred, alpha=0.6, color="#2ECC71")
                    ax_p.plot([y_te.min(), y_te.max()], [y_te.min(), y_te.max()], "r--")
                    ax_p.set_xlabel("Actual")
                    ax_p.set_ylabel("Predicted")
                    st.pyplot(fig_p)
                    plt.close(fig_p)

                st.subheader("🏆 Feature Importances")
                imp_df = pd.DataFrame(
                    {"Feature": feature_cols, "Importance": model.feature_importances_}
                ).sort_values("Importance", ascending=False)
                fig_i, ax_i = plt.subplots(figsize=(8, max(3, len(feature_cols) * 0.4)))
                sns.barplot(
                    data=imp_df,
                    x="Importance",
                    y="Feature",
                    palette="Greens_r",
                    ax=ax_i,
                )
                ax_i.set_title("Feature Importances (Split Gain)")
                st.pyplot(fig_i)
                plt.close(fig_i)
