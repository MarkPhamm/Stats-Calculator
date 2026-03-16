import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score


# ==========================================
# HELPER: K-Means Algorithm (For Tab 1)
# ==========================================
def k_means_algorithm(X, k, iterations=10):
    """
    Manual implementation of K-Means step-by-step for visualization.
    """
    # Initialize centroids randomly from existing points
    centroids = X[np.random.choice(X.shape[0], k, replace=False)]
    history = []
    
    for _ in range(iterations):
        # Calculate distances from points to centroids
        distances = np.linalg.norm(X[:, np.newaxis] - centroids, axis=2)
        # Assign labels based on closest centroid
        labels = np.argmin(distances, axis=1)
        
        # Store state
        history.append((centroids.copy(), labels.copy()))
        
        # Update centroids to the mean of their assigned points
        new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(k)])
        
        # Check for convergence
        if np.all(centroids == new_centroids):
            break
        centroids = new_centroids
        
    return history

# ==========================================
# MAIN APP MODULE
# ==========================================
def main():
    st.title("K-Means Clustering")

    tab1, tab2 = st.tabs(["📚 Theory & Visualization", "🛠️ Practical Analysis"])

    # ==========================================
    # TAB 1: Theory (Animation)
    # ==========================================
    with tab1:
        st.header("How K-Means Works")
        st.markdown("""
        K-Means is an iterative algorithm that partitions data into **K** distinct clusters. 
        It works by moving 'centroids' to the center of the data points assigned to them.
        """)

        col_control, col_anim = st.columns([1, 2])
        
        with col_control:
            st.subheader("Simulation Config")
            n_centers = st.slider("Number of True Clusters", 2, 5, 3)
            k_clusters = st.slider("K (Centroids to find)", 2, 5, 3)
            st.info("Click 'Run Animation' to see the centroids move.")

        with col_anim:
            # Generate synthetic blobs
            X, _ = make_blobs(n_samples=300, centers=n_centers, cluster_std=0.60, random_state=0)
            
            placeholder = st.empty()
            
            if st.button("Run Animation"):
                history = k_means_algorithm(X, k_clusters)
                
                # Animation Loop
                for i, (centroids, labels) in enumerate(history):
                    fig, ax = plt.subplots(figsize=(6, 4))
                    
                    # Plot data points colored by cluster
                    ax.scatter(X[:, 0], X[:, 1], c=labels, s=30, cmap='viridis', alpha=0.6)
                    
                    # Plot centroids
                    ax.scatter(centroids[:, 0], centroids[:, 1], c='red', s=200, marker='X', label='Centroids')
                    
                    ax.set_title(f"Iteration {i+1}")
                    ax.legend()
                    placeholder.pyplot(fig)
                    plt.close(fig) 
                
                st.success("Convergence Reached!")
            else:
                # Show initial data
                fig, ax = plt.subplots(figsize=(6, 4))
                ax.scatter(X[:, 0], X[:, 1], color='gray', alpha=0.5)
                ax.set_title("Raw Data (No Clusters)")
                placeholder.pyplot(fig)

    # ==========================================
    # TAB 2: Practical Analysis (Real Data)
    # ==========================================
    with tab2:
        st.header("Cluster Your Own Data")
        
        uploaded_file = st.file_uploader("Upload CSV File", type=["csv"], key="kmeans_upload")
        
        if uploaded_file is not None:
            # Load Data
            df = pd.read_csv(uploaded_file)
            
            # Keep only numeric columns
            df_numeric = df.select_dtypes(include=['float64', 'int64']).fillna(0)
            
            st.write("Data Preview (Numeric Columns Only):", df_numeric.head())
            
            st.subheader("1. Feature Selection")
            selected_features = st.multiselect("Select exactly 2 Features for Visualization", df_numeric.columns)
            
            if len(selected_features) == 2:
                X_real = df_numeric[selected_features].values
                
                # Elbow Method
                st.subheader("2. Determine Optimal K (Elbow Method)")
                st.write("The 'Elbow' of the graph represents the optimal number of clusters.")
                
                wcss = []
                range_k = range(1, 11)
                for k in range_k:
                    kmeans = KMeans(n_clusters=k, random_state=42)
                    kmeans.fit(X_real)
                    wcss.append(kmeans.inertia_)
                
                fig_elbow, ax_elbow = plt.subplots(figsize=(8, 3))
                ax_elbow.plot(range_k, wcss, marker='o', linestyle='--')
                ax_elbow.set_xlabel('Number of Clusters (K)')
                ax_elbow.set_ylabel('WCSS (Within-Cluster Sum of Square)')
                ax_elbow.set_title("Elbow Method Graph")
                st.pyplot(fig_elbow)
                
                # Final Clustering
                st.subheader("3. Apply Clustering")
                final_k = st.number_input("Choose K based on the graph above", min_value=2, max_value=10, value=3)
                
                if st.button("Run K-Means Clustering"):
                    # Train model
                    km_final = KMeans(n_clusters=final_k, random_state=42)
                    y_kmeans = km_final.fit_predict(X_real)
                    
                    # Metrics
                    sil_score = silhouette_score(X_real, y_kmeans)
                    st.metric("Silhouette Score", f"{sil_score:.4f}", help="Close to 1 is good, close to -1 is bad.")
                    
                    # Visualization
                    fig_res, ax_res = plt.subplots()
                    # Plot points
                    ax_res.scatter(X_real[:, 0], X_real[:, 1], c=y_kmeans, cmap='viridis', s=50, alpha=0.6)
                    # Plot centers
                    centers = km_final.cluster_centers_
                    ax_res.scatter(centers[:, 0], centers[:, 1], c='red', s=200, marker='X', label='Centroids')
                    
                    ax_res.set_xlabel(selected_features[0])
                    ax_res.set_ylabel(selected_features[1])
                    ax_res.set_title(f"K-Means Clustering (K={final_k})")
                    ax_res.legend()
                    st.pyplot(fig_res)
            else:
                st.warning("Please select exactly 2 features to proceed with 2D visualization.")