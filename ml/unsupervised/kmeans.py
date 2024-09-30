import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score

# K-Means Algorithm with centroid tracking
def k_means(X, k, iterations=100):
    # Randomly initialize centroids further away from the data points for slower convergence
    centroids = np.random.uniform(low=X.min() - 10, high=X.max() + 10, size=(k, X.shape[1]))
    history = []
    silhouette_history = []

    for _ in range(iterations):
        # Assign each point to the nearest centroid
        distances = np.sqrt(((X - centroids[:, np.newaxis])**2).sum(axis=2))
        labels = np.argmin(distances, axis=0)
        
        # Recompute centroids
        new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(k)])
        
        # Save history for plotting
        history.append((centroids.copy(), labels.copy()))
        
        # Calculate silhouette score
        if len(np.unique(labels)) > 1:
            silhouette_avg = silhouette_score(X, labels)
            silhouette_history.append(silhouette_avg)
        
        # Update centroids with a smaller adjustment step for slower convergence
        centroids = centroids + 0.4 * (new_centroids - centroids)  # Smaller step size for centroid movement

    return history, silhouette_history

def main():
    st.title("K-Means Clustering with Centroid Movement Visualization")

    # Add LaTeX formulas to explain the process of K-Means clustering
    st.subheader("K-Means Clustering Formulas")

    # Distance formula for K-means
    st.latex(r"d(x_i, c_j) = \sqrt{\sum_{k=1}^{n} (x_{ik} - c_{jk})^2}")
    
    # Update rule for centroids
    st.latex(r"c_j = \frac{1}{|S_j|} \sum_{x_i \in S_j} x_i")
    
    # Silhouette score formula
    st.latex(r"silhouette = \frac{b - a}{\max(a, b)}")

    # Randomly generate a synthetic dataset
    np.random.seed(42)
    n_samples = st.slider("Number of points", min_value=100, max_value=500, step=50, value=300)
    n_clusters = st.slider("Number of clusters (K)", min_value=2, max_value=5, step=1, value=3)
    iterations = st.slider("Number of iterations", min_value=1, max_value=20, value=10, step=1)

    # Generate highly scattered data
    X, _ = make_blobs(n_samples=n_samples, centers=n_clusters, cluster_std=3.5, random_state=42)

    # Plot the random points
    st.subheader("Randomly Generated Data Points")

    # Initial figure and axis
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Scatter plot of the data points
    scatter = ax1.scatter(X[:, 0], X[:, 1], c='gray')
    centroid_scatter = ax1.scatter([], [], c='red', marker='x', s=100, label="Centroids")
    ax1.set_title("K-Means Clustering with Centroid Movement")
    ax1.set_xlabel("X1")
    ax1.set_ylabel("X2")
    ax1.legend()

    # Plot for silhouette score
    ax2.set_title("Silhouette Score over Iterations")
    ax2.set_xlabel("Iterations")
    ax2.set_ylabel("Silhouette Score")
    silhouette_plot, = ax2.plot([], [], color='green')

    # Initialize the plot in Streamlit (create a single placeholder for the plot)
    plot_placeholder = st.pyplot(fig)

    if st.button("Run K-Means"):
        # Run K-Means algorithm
        history, silhouette_history = k_means(X, n_clusters, iterations)

        # Loop through the K-Means history to update centroids, labels, and silhouette score
        for i in range(len(history)):
            centroids, labels = history[i]
            scatter.set_offsets(X)
            scatter.set_array(labels)

            # Update centroid positions
            centroid_scatter.set_offsets(centroids)

            # Update silhouette score plot
            if i < len(silhouette_history):
                silhouette_plot.set_data(range(i+1), silhouette_history[:i+1])

            # Set axis limits dynamically
            ax2.set_xlim(0, len(silhouette_history))
            ax2.set_ylim(0, 1)

            # Redraw the plot (single plot update)
            plot_placeholder.pyplot(fig)

        # Display final silhouette score
        final_silhouette = silhouette_history[-1] if silhouette_history else 0
        st.success(f"Final Silhouette Score: {final_silhouette:.4f}")

    st.markdown("""
    - **d(x_i, c_j)**: Distance between data point \(x_i\) and centroid \(c_j\).
    - **c_j**: Centroid of the \(j\)-th cluster, calculated as the mean of points assigned to it.
    - **Silhouette score**: A measure of how similar an object is to its own cluster compared to other clusters, ranging from -1 to 1.
    """)

if __name__ == "__main__":
    main()
