import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


def main():
    st.title("Principal Component Analysis (PCA)")

    tab1, tab2 = st.tabs(["📚 Theory & Visualization", "🛠️ Practical Analysis"])

    # ==========================================
    # TAB 1: Theory (Variance & Projection)
    # ==========================================
    with tab1:
        st.header("Dimensionality Reduction Concept")
        st.markdown("""
        PCA simplifies complex data by finding the "Principal Components" (directions) where the data varies the most. 
        It's like finding the best angle to take a photo of a 3D object so you lose the least amount of detail.
        """)

        # Generate correlated data
        np.random.seed(1)
        mean = [0, 0]
        cov = [[1, 0.8], [0.8, 1]]  # Strong correlation
        X_vis = np.random.multivariate_normal(mean, cov, 100)

        # Fit PCA
        pca = PCA(n_components=2)
        pca.fit(X_vis)
        
        # Plot
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.scatter(X_vis[:, 0], X_vis[:, 1], alpha=0.5)
        
        # Draw vectors
        for length, vector in zip(pca.explained_variance_, pca.components_):
            v = vector * 3 * np.sqrt(length)
            ax.arrow(pca.mean_[0], pca.mean_[1], v[0], v[1], 
                     head_width=0.1, head_length=0.1, linewidth=2, color='red')
            
        ax.axis('equal')
        ax.set_title("Data with Principal Components (Red Arrows)")
        st.pyplot(fig)
        
        st.caption("The long red arrow is the First Principal Component (PC1) - it captures the most information.")

    # ==========================================
    # TAB 2: Practical Analysis
    # ==========================================
    with tab2:
        st.header("Visualize High-Dimensional Data")
        
        uploaded_file = st.file_uploader("Upload CSV/Excel", type=["csv", "xlsx"], key="pca_upload")

        if uploaded_file is not None:
            if uploaded_file.name.endswith(".csv"):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
            
            df = df.fillna(df.median(numeric_only=True))
            
            # Feature Selection
            numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
            features = st.multiselect("Select Features to Analyze (Choose > 2)", numeric_cols)
            
            # Optional: Select a column for coloring points
            color_col = st.selectbox("Select Label for Coloring (Optional)", ["None"] + list(df.columns))

            if len(features) >= 2 and st.button("Run PCA"):
                X = df[features]
                
                # Standardize Data (Critical for PCA)
                scaler = StandardScaler()
                X_scaled = scaler.fit_transform(X)

                # Run PCA
                pca = PCA(n_components=2)
                components = pca.fit_transform(X_scaled)
                
                # Explained Variance
                var_ratio = pca.explained_variance_ratio_
                st.info(f"Explained Variance: PC1 ({var_ratio[0]:.2%}) + PC2 ({var_ratio[1]:.2%}) = Total {(sum(var_ratio)):.2%}")

                # Plotting
                pca_df = pd.DataFrame(data=components, columns=['PC1', 'PC2'])
                
                if color_col != "None":
                    pca_df['Label'] = df[color_col].astype(str).values
                
                fig, ax = plt.subplots(figsize=(8, 6))
                if color_col != "None":
                    sns.scatterplot(data=pca_df, x='PC1', y='PC2', hue='Label', alpha=0.7, ax=ax)
                else:
                    sns.scatterplot(data=pca_df, x='PC1', y='PC2', alpha=0.7, ax=ax)
                
                ax.set_title("PCA Projection (2D)")
                st.pyplot(fig)
                
                # Loadings (What makes up PC1/PC2?)
                st.subheader("Component Loadings (Influence of original features)")
                loadings = pd.DataFrame(pca.components_.T, columns=['PC1', 'PC2'], index=features)
                st.dataframe(loadings)