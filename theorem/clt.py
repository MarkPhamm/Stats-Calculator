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

    # Display the formula for the Central Limit Theorem using st.latex
    st.latex(r"""
        \text{The Central Limit Theorem (CLT) states that, for a sufficiently large sample size } n, \\
        \text{the sampling distribution of the sample mean } \bar{X} \text{ will be approximately normally} \\
        \text{distributed regardless of the original distribution of the data.} \\
             
        \newline
             
        \text{If } X_1, X_2, \ldots, X_n \text{ are independent and identically distributed random variables} \\
        \text{with population mean } \mu \text{ and population variance } \sigma^2 \text{, then:}
    """)



    st.latex(r"""
    \bar{X} \sim N \left( \mu, \frac{\sigma^2}{n} \right)
    """)

    st.latex(r"""
    \begin{align*}
    \bar{X} & \text{ is the sample mean} \\
    \mu & \text{ is the population mean} \\
    \sigma^2 & \text{ is the population variance} \\
    n & \text{ is the sample size}
    \end{align*}
    """)

    # Choose the original distribution
    distribution = st.selectbox("Select Original Distribution:", ["Normal", "Uniform", "Exponential", "Triangular"])

    # Set parameters for the chosen distribution
    if distribution == "Normal":
        mean = st.slider("Mean (for Normal Distribution)", -10.0, 10.0, 0.0, 0.1)
        std_dev = st.slider("Standard Deviation (for Normal Distribution)", 0.1, 10.0, 1.0, 0.1)
        params = {'mean': mean, 'std_dev': std_dev}
    elif distribution == "Uniform":
        low = st.slider("Low (for Uniform Distribution)", -10.0, 0.0, 0.0, 0.1)
        high = st.slider("High (for Uniform Distribution)", 0.0, 10.0, 1.0, 0.1)
        params = {'low': low, 'high': high}
    elif distribution == "Exponential":
        scale = st.slider("Scale (for Exponential Distribution)", 0.1, 10.0, 1.0, 0.1)
        params = {'scale': scale}
    elif distribution == "Triangular":
        left = st.slider("Left (for Triangular Distribution)", -10.0, 0.0, 0.0, 0.1)
        mode = st.slider("Mode (for Triangular Distribution)", -10.0, 10.0, 0.5, 0.1)
        right = st.slider("Right (for Triangular Distribution)", 0.0, 20.0, 1.0, 0.1)
        params = {'left': left, 'mode': mode, 'right': right}

    # Number of samples and sample size
    num_samples = st.slider("Number of Samples (N)", 10, 1000, 100)
    sample_size = st.slider("Sample Size", 1, 100, 30)

    # Generate the original data
    original_data = generate_data(distribution, size=num_samples, **params)

    # Generate sample means
    sample_means = [np.mean(generate_data(distribution, size=sample_size, **params)) for _ in range(num_samples)]

    # Calculate statistics
    pop_mean, pop_std, pop_std_error = calculate_statistics(original_data)
    sample_mean, sample_std, sample_std_error = calculate_statistics(sample_means)

    # Plot the distributions
    fig, axs = plt.subplots(1, 2, figsize=(14, 6))
    plot_distribution(axs[0], original_data, 'Original Distribution', color='blue')
    plot_distribution(axs[1], sample_means, 'Sampling Distribution of Sample Means', color='green')
    st.pyplot(fig)

    # Display statistics in two columns
    st.subheader("Statistics:")
    col1, col2 = st.columns(2)
    
    with col1:
        st.text(f"Population Mean: {pop_mean:.4f}")
        st.text(f"Population Standard Deviation: {pop_std:.4f}")
        st.text(f"Population Standard Error: {pop_std_error:.4f}")
    
    with col2:
        st.text(f"Sample Mean: {sample_mean:.4f}")
        st.text(f"Sample Standard Deviation: {sample_std:.4f}")
        st.text(f"Sample Standard Error: {sample_std_error:.4f}")

if __name__ == "__main__":
    main()
