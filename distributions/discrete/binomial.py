import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

def calculate_binomial_distribution_stats(n: int, p: float) -> tuple[float, float]:
    """
    Calculate mean and standard deviation for a binomial distribution.

    Args:
        n (int): Number of trials.
        p (float): Probability of success.

    Returns:
        tuple: Mean and standard deviation.
    """
    mean = n * p
    variance = n * p * (1 - p)
    std_dev = np.sqrt(variance)
    return mean, std_dev

def plot_binomial_distribution(n: int, p: float, s_min: int, s_max: int) -> None:
    """
    Plot the binomial distribution with highlighted range.

    Args:
        n (int): Number of trials.
        p (float): Probability of success.
        s_min (int): Minimum number of successes.
        s_max (int): Maximum number of successes.
    """
    x_vals = np.arange(0, n + 1)
    y_vals = binom.pmf(x_vals, n, p)
    
    fig, ax = plt.subplots()
    ax.bar(x_vals, y_vals, label="Binomial Distribution", alpha=0.7)
    
    mask = (x_vals >= s_min) & (x_vals <= s_max)
    ax.bar(x_vals[mask], y_vals[mask], color='blue', alpha=0.5, label=f"P({s_min} <= X <= {s_max})")
    
    ax.axvline(x=s_min, color='red', linestyle='--', label=f's_min = {s_min}')
    ax.axvline(x=s_max, color='green', linestyle='--', label=f's_max = {s_max}')
    
    ax.set_title(f'Binomial Distribution (n={n}, p={p})')
    ax.set_xlabel('Number of Successes')
    ax.set_ylabel('Probability Mass')
    ax.legend()
    
    st.pyplot(fig)

def main():
    st.title("Binomial Distribution Calculator")

    st.latex(r"""
    P(X = k) = \binom{n}{k} p^k (1 - p)^{n - k}
    """)

    n = st.number_input("Enter the Number of Trials (n)", value=10, step=1, min_value=1)
    p = st.number_input("Enter the Probability of Success (p)", value=0.5, step=0.01, min_value=0.0, max_value=1.0)

    s_min = st.number_input("Enter the Minimum Number of Successes (s_min)", value=0, step=1, min_value=0, max_value=n)
    s_max = st.number_input("Enter the Maximum Number of Successes (s_max)", value=n, step=1, min_value=s_min, max_value=n)

    mean, std_dev = calculate_binomial_distribution_stats(n, p)

    p_range = binom.cdf(s_max, n, p) - binom.cdf(s_min - 1, n, p)
    p_less_than_equal_s_max = binom.cdf(s_max, n, p)
    p_less_than_equal_s_min = binom.cdf(s_min, n, p)

    st.write(f"Mean: {mean:.4f}")
    st.write(f"Standard Deviation: {std_dev:.4f}")
    st.success(f"Cumulative Probability P(X <= {s_min}): {p_less_than_equal_s_min:.4f}")
    st.success(f"Cumulative Probability P(X <= {s_max}): {p_less_than_equal_s_max:.4f}")

    st.success(f"Probability P({s_min} <= X <= {s_max}): {p_range:.4f}")

    st.header("Calculate P(X = x) for specific values")
    x_values_input = st.text_input("Enter values of x (separated by commas)", value="0, 1, 2")
    
    try:
        x_values = [int(x.strip()) for x in x_values_input.split(",")]
        valid_x_values = [x for x in x_values if 0 <= x <= n]
        
        if valid_x_values:
            for x in valid_x_values:
                prob = binom.pmf(x, n, p)
                st.success(f"P(X = {x}): {prob:.4f}")
        else:
            st.warning("Please enter valid x values between 0 and n.")
    except ValueError:
        st.error("Invalid input for x values. Please enter integers separated by commas.")
    
    plot_binomial_distribution(n, p, s_min, s_max)

if __name__ == "__main__":
    main()
