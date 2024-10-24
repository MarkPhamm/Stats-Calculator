import streamlit as st
import math
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

def main():
    def calculate_z_statistic(sample_mean, population_mean, std_dev, sample_size):
        """Calculate Z-statistic for hypothesis test on mean (known population standard deviation)."""
        return (sample_mean - population_mean) / (std_dev / math.sqrt(sample_size))

    def calculate_t_statistic(sample_mean, population_mean, sample_std_dev, sample_size):
        """Calculate t-statistic for hypothesis test on mean (unknown population standard deviation)."""
        return (sample_mean - population_mean) / (sample_std_dev / math.sqrt(sample_size))

    def calculate_z_statistic_proportion(sample_prop, population_prop, sample_size):
        """Calculate Z-statistic for hypothesis test on proportion."""
        return (sample_prop - population_prop) / math.sqrt((population_prop * (1 - population_prop)) / sample_size)

    def plot_distribution(distribution, test_statistic, critical_value, hypothesis_type, df=None):
        """Plot the distribution with critical regions and test statistic."""
        fig, ax = plt.subplots(figsize=(10, 6))
        x = np.linspace(distribution.ppf(0.001, df) if df is not None else distribution.ppf(0.001), 
                        distribution.ppf(0.999, df) if df is not None else distribution.ppf(0.999), 1000)
        y = distribution.pdf(x, df) if df is not None else distribution.pdf(x)
        
        ax.plot(x, y, 'b-', lw=2, label='Distribution')
        
        # Shade critical region(s)
        if hypothesis_type == "Two-Tailed":
            ax.fill_between(x, y, where=(x >= critical_value) | (x <= -critical_value), color='red', alpha=0.3, label='Critical Region')
        elif hypothesis_type == "Left-Tailed":
            ax.fill_between(x, y, where=(x <= -critical_value), color='red', alpha=0.3, label='Critical Region')
        else:  # Right-Tailed
            ax.fill_between(x, y, where=(x >= critical_value), color='red', alpha=0.3, label='Critical Region')
        
        # Plot test statistic and critical value(s)
        ax.axvline(test_statistic, color='green', linestyle='--', label='Test Statistic')
        ax.axvline(critical_value, color='red', linestyle='--', label='Critical Value')
        if hypothesis_type == "Two-Tailed":
            ax.axvline(-critical_value, color='red', linestyle='--')
        
        ax.set_title('Hypothesis Test Visualization')
        ax.set_xlabel('Test Statistic')
        ax.set_ylabel('Probability Density')
        ax.legend()
        st.pyplot(fig)

    st.title("Hypothesis Testing Calculator")

    st.latex(r"\text{Z-statistic} = \frac{\bar{x} - \mu_0}{\sigma / \sqrt{n}}")
    st.latex(r"\text{t-statistic} = \frac{\bar{x} - \mu_0}{s / \sqrt{n}}")
    st.latex(r"\text{Z-statistic (Proportion)} = \frac{\hat{p} - p_0}{\sqrt{p_0(1 - p_0) / n}}")

    test_type = st.sidebar.radio("Select Test Type:", ["Mean", "Proportion"])
    
    if test_type == "Mean":
        test_option = st.selectbox("Select Test Option:", ["Sigma Known (Z-test)", "Sigma Unknown (t-test)"])
    else:
        test_option = "Proportion Test"

    hypothesis_type = st.selectbox("Select Hypothesis Type:", ["Two-Tailed", "Left-Tailed", "Right-Tailed"])

    sample_size = st.number_input("Enter Sample Size (n)", min_value=1, value=30, step=1)
    significance_level = st.slider("Select Significance Level (α)", min_value=0.01, max_value=0.10, value=0.05, step=0.01)

    if test_type == "Mean":
        population_mean = st.number_input("Enter Hypothesized Population Mean (μ₀)", value=0.0, step=0.1)
        sample_mean = st.number_input("Enter Sample Mean (x̄)", value=0.0, step=0.1)

        if test_option == "Sigma Known (Z-test)":
            std_dev = st.number_input("Enter Population Standard Deviation (σ)", value=1.0, step=0.1)
            test_statistic = calculate_z_statistic(sample_mean, population_mean, std_dev, sample_size)
            distribution = stats.norm
            df = None
        else:  # Sigma Unknown (t-test)
            sample_std_dev = st.number_input("Enter Sample Standard Deviation (s)", value=1.0, step=0.1)
            test_statistic = calculate_t_statistic(sample_mean, population_mean, sample_std_dev, sample_size)
            distribution = stats.t
            df = sample_size - 1
        
        st.subheader("Hypotheses:")
        st.write(f"Null Hypothesis (H₀): μ = {population_mean}")
        if hypothesis_type == "Two-Tailed":
            st.write(f"Alternative Hypothesis (H₁): μ ≠ {population_mean}")
        elif hypothesis_type == "Left-Tailed":
            st.write(f"Alternative Hypothesis (H₁): μ < {population_mean}")
        else:  # Right-Tailed
            st.write(f"Alternative Hypothesis (H₁): μ > {population_mean}")

    else:  # Proportion
        population_prop = st.number_input("Enter Hypothesized Population Proportion (p₀)", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        sample_prop = st.number_input("Enter Sample Proportion (p̂)", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        test_statistic = calculate_z_statistic_proportion(sample_prop, population_prop, sample_size)
        distribution = stats.norm
        df = None

        st.subheader("Hypotheses:")
        st.write(f"Null Hypothesis (H₀): p = {population_prop}")
        if hypothesis_type == "Two-Tailed":
            st.write(f"Alternative Hypothesis (H₁): p ≠ {population_prop}")
        elif hypothesis_type == "Left-Tailed":
            st.write(f"Alternative Hypothesis (H₁): p < {population_prop}")
        else:  # Right-Tailed
            st.write(f"Alternative Hypothesis (H₁): p > {population_prop}")

    # Calculate critical value and p-value
    if hypothesis_type == "Two-Tailed":
        critical_value = distribution.ppf(1 - significance_level / 2, df) if df is not None else distribution.ppf(1 - significance_level / 2)
        p_value = 2 * (1 - distribution.cdf(abs(test_statistic), df)) if df is not None else 2 * (1 - distribution.cdf(abs(test_statistic)))
    elif hypothesis_type == "Left-Tailed":
        critical_value = distribution.ppf(significance_level, df) if df is not None else distribution.ppf(significance_level)
        p_value = distribution.cdf(test_statistic, df) if df is not None else distribution.cdf(test_statistic)
    else:  # Right-Tailed
        critical_value = distribution.ppf(1 - significance_level, df) if df is not None else distribution.ppf(1 - significance_level)
        p_value = 1 - distribution.cdf(test_statistic, df) if df is not None else 1 - distribution.cdf(test_statistic)

    st.subheader("Results:")
    st.success(f"Test Statistic: {test_statistic:.4f}")
    st.success(f"Critical Value: {critical_value:.4f}")
    st.success(f"p-value: {p_value:.4f}")

    plot_distribution(distribution, test_statistic, critical_value, hypothesis_type, df)

    st.subheader("Conclusion:")
    if p_value < significance_level:
        st.success(f"Reject the null hypothesis (p-value {p_value:.4f} < α {significance_level}). There is sufficient evidence to support the alternative hypothesis.")
    else:
        st.error(f"Fail to reject the null hypothesis (p-value {p_value:.4f} ≥ α {significance_level}). There is not sufficient evidence to support the alternative hypothesis.")

if __name__ == "__main__":
    main()
