import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
from sklearn.datasets import make_moons
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree


def main():
    st.title("Decision Tree Classifier")

    tab1, tab2 = st.tabs(["📚 Theory & Visualization", "🛠️ Practical Analysis"])

    # ==========================================
    # TAB 1: Theory (Visualizing Decision Boundaries)
    # ==========================================
    with tab1:
        st.header("How Decision Trees Work")
        st.markdown("""
        A Decision Tree splits data into smaller groups based on rules (e.g., "If X > 5, go left"). 
        It keeps splitting until it creates a "leaf" node with a prediction.
        """)

        col_control, col_viz = st.columns([1, 2])

        with col_control:
            st.subheader("Tree Config")
            depth = st.slider("Max Depth (Complexity)", 1, 10, 3)
            noise_lvl = st.slider("Noise Level", 0.0, 0.5, 0.2)
            st.info("Higher depth captures more details but may lead to overfitting.")

        with col_viz:
            # Generate non-linear data (Moons)
            X, y = make_moons(n_samples=200, noise=noise_lvl, random_state=42)

            # Train Tree
            tree_clf = DecisionTreeClassifier(max_depth=depth, random_state=42)
            tree_clf.fit(X, y)

            # Plot Decision Boundary
            fig, ax = plt.subplots()

            # Create meshgrid
            x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
            y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
            xx, yy = np.meshgrid(
                np.arange(x_min, x_max, 0.02), np.arange(y_min, y_max, 0.02)
            )

            Z = tree_clf.predict(np.c_[xx.ravel(), yy.ravel()])
            Z = Z.reshape(xx.shape)

            ax.contourf(xx, yy, Z, alpha=0.3, cmap="coolwarm")
            ax.scatter(X[:, 0], X[:, 1], c=y, cmap="coolwarm", edgecolors="k")
            ax.set_title(f"Decision Boundary (Depth={depth})")
            st.pyplot(fig)

            # Plot the actual Tree structure
            st.subheader("Tree Structure Visualization")
            fig_tree, ax_tree = plt.subplots(figsize=(12, 6))
            plot_tree(
                tree_clf,
                filled=True,
                feature_names=["X1", "X2"],
                class_names=["Class 0", "Class 1"],
                ax=ax_tree,
            )
            st.pyplot(fig_tree)

    # ==========================================
    # TAB 2: Practical Analysis
    # ==========================================
    with tab2:
        st.header("Train Decision Tree on Data")

        uploaded_file = st.file_uploader(
            "Upload CSV/Excel", type=["csv", "xlsx"], key="dt_upload"
        )

        if uploaded_file is not None:
            if uploaded_file.name.endswith(".csv"):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)

            df = df.fillna(df.median(numeric_only=True))
            st.write("Data Preview:", df.head())

            # Select Target and Features
            target_col = st.selectbox(
                "Select Target (Label)", df.columns, key="dt_target"
            )

            numeric_cols = df.select_dtypes(
                include=["float64", "int64"]
            ).columns.tolist()
            if target_col in numeric_cols:
                numeric_cols.remove(target_col)

            feature_cols = st.multiselect(
                "Select Features (Input)", numeric_cols, key="dt_features"
            )

            # Hyperparameter tuning for user
            user_depth = st.slider("Max Tree Depth", 1, 20, 5, key="dt_depth_real")

            if feature_cols and st.button("Train Decision Tree"):
                X = df[feature_cols]
                y = df[target_col]

                X_train, X_test, y_train, y_test = train_test_split(
                    X, y, test_size=0.2, random_state=42
                )

                model = DecisionTreeClassifier(max_depth=user_depth, random_state=42)
                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)

                # Metrics
                acc = accuracy_score(y_test, y_pred)
                st.success(f"Model Accuracy: {acc:.2%}")

                # Feature Importance
                st.subheader("Feature Importance")
                imp_df = pd.DataFrame(
                    {"Feature": feature_cols, "Importance": model.feature_importances_}
                ).sort_values(by="Importance", ascending=False)

                fig_imp, ax_imp = plt.subplots()
                sns.barplot(
                    data=imp_df,
                    x="Importance",
                    y="Feature",
                    ax=ax_imp,
                    palette="viridis",
                )
                st.pyplot(fig_imp)

                # Show Tree Rules (Text)
                with st.expander("See Text Representation of Rules"):
                    from sklearn.tree import export_text

                    st.text(export_text(model, feature_names=feature_cols))
