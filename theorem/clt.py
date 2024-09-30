import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plot_distribution(ax, data, title, color='blue'):
    sns.histplot(data, kde=True, color=color, ax=ax, bins=30)
    ax.set_title(title)
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')

def generate_data(distribution, size, **kwargs):
    if distribution == "Normal":
        return np.random.normal(loc=kwargs.get('mean', 0), scale=kwargs.get('std_dev', 1), size=size)
    elif distribution == "Uniform":
        return np.random.uniform(low=kwargs.get('low', 0), high=kwargs.get('high', 1), size=size)
    elif distribution == "Exponential":
        return np.random.exponential(scale=kwargs.get('scale', 1), size=size)
    elif distribution == "Triangular":
        return np.random.triangular(left=kwargs.get('left', 0), mode=kwargs.get('mode', 0.5), right=kwargs.get('right', 1), size=size)
    else:
        raise ValueError("Unsupported distribution")

def calculate_statistics(data):
    mean = np.mean(data)
    std_dev = np.std(data, ddof=1)
    std_error = std_dev / np.sqrt(len(data))
    return mean, std_dev, std_error

def main():
    st.title("Central Limit Theorem Demonstration")

    st.markdown('''
    <style>
    .katex-html {
        text-align: left;
    }
    </style>''',
    unsafe_allow_html=True
    )

    # Explanation of the Central Limit Theorem
    st.header("Central Limit Theorem (CLT)")
    st.write("""
    The Central Limit Theorem states that for a sufficiently large sample size, 
    the sampling distribution of the sample mean will be approximately normally distributed, 
    regardless of the original distribution of the data.
    """)

    st.latex(r"""
    \text{Given: } X_1, X_2, \ldots, X_n \text{ are independent and identically distributed random variables}
    """)
    
    st.latex(r"""
    \text{with population mean } \mu \text{ and population variance } \sigma^2
    """)

    st.latex(r"""
    \text{Then, for large } n\text{:}
    """)

    st.latex(r"""
    \bar{X} \sim N \left( \mu, \frac{\sigma^2}{n} \right)
    """)

    st.write("""
    Where:
    - $\overline{X}$ is the sample mean
    - $\mu$ is the population mean
    - $\sigma^2$ is the population variance
    - $n$ is the sample size
    """)

    # Distribution selection
    distribution = st.selectbox("Select Original Distribution:", ["Normal", "Uniform", "Exponential", "Triangular"])

    # Set distribution parameters
    params = {}
    if distribution == "Normal":
        params['mean'] = st.slider("Mean", -10.0, 10.0, 0.0, 0.1)
        params['std_dev'] = st.slider("Standard Deviation", 0.1, 10.0, 1.0, 0.1)
    elif distribution == "Uniform":
        params['low'] = st.slider("Lower Bound", -10.0, 0.0, 0.0, 0.1)
        params['high'] = st.slider("Upper Bound", 0.0, 10.0, 1.0, 0.1)
    elif distribution == "Exponential":
        params['scale'] = st.slider("Scale", 0.1, 10.0, 1.0, 0.1)
    elif distribution == "Triangular":
        params['left'] = st.slider("Left", -10.0, 0.0, 0.0, 0.1)
        params['mode'] = st.slider("Mode", -10.0, 10.0, 0.5, 0.1)
        params['right'] = st.slider("Right", 0.0, 20.0, 1.0, 0.1)

    # Simulation parameters
    num_samples = st.slider("Number of Samples", 10, 1000, 100)
    sample_size = st.slider("Sample Size", 1, 100, 30)

    # Generate data
    original_data = generate_data(distribution, size=num_samples, **params)
    sample_means = [np.mean(generate_data(distribution, size=sample_size, **params)) for _ in range(num_samples)]

    # Calculate statistics
    pop_mean, pop_std, pop_std_error = calculate_statistics(original_data)
    sample_mean, sample_std, sample_std_error = calculate_statistics(sample_means)

    # Plot distributions
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    plot_distribution(ax1, original_data, 'Original Distribution', color='blue')
    plot_distribution(ax2, sample_means, 'Sampling Distribution of Sample Means', color='green')
    st.pyplot(fig)

    # Display statistics
    st.subheader("Statistics:")
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("Original Distribution:")
        st.write(f"Mean: {pop_mean:.4f}")
        st.write(f"Standard Deviation: {pop_std:.4f}")
        st.write(f"Standard Error: {pop_std_error:.4f}")
    
    with col2:
        st.write("Sampling Distribution:")
        st.write(f"Mean: {sample_mean:.4f}")
        st.write(f"Standard Deviation: {sample_std:.4f}")
        st.write(f"Standard Error: {sample_std_error:.4f}")

if __name__ == "__main__":
    main()
