import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

def calculate_poisson_distribution_stats(lam: float) -> tuple[float, float]:
    """
    Calculate mean and standard deviation for a Poisson distribution.

    Args:
        lam (float): Rate (lambda) of the Poisson distribution.

    Returns:
        tuple: Mean and standard deviation.
    """
    mean = lam
    std_dev = np.sqrt(lam)
    return mean, std_dev

def plot_poisson_distribution(lam: float, x_min: int, x_max: int) -> None:
    """
    Plot the Poisson distribution with highlighted range.

    Args:
        lam (float): Rate (lambda) of the Poisson distribution.
        x_min (int): Minimum number of occurrences.
        x_max (int): Maximum number of occurrences.
    """
    x_vals = np.arange(0, x_max + 0.5*x_max)  # Adjusted to extend the range to x_max + 1
    y_vals = poisson.pmf(x_vals, lam)
    
    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, marker='o', label="Poisson Distribution", alpha=0.7)  # Changed to line plot with markers
    
    mask = (x_vals >= x_min) & (x_vals <= x_max)
    ax.fill_between(x_vals[mask], y_vals[mask], color='blue', alpha=0.5, label=f"P({x_min} <= X <= {x_max})")  # Highlighted area
    
    ax.axvline(x=x_min, color='red', linestyle='--', label=f'x_min = {x_min}')
    ax.axvline(x=x_max, color='green', linestyle='--', label=f'x_max = {x_max}')
    
    ax.set_title(f'Poisson Distribution (λ={lam})')
    ax.set_xlabel('Number of Occurrences')
    ax.set_ylabel('Probability Mass')
    ax.legend()
    
    st.pyplot(fig)

def main():
    st.title("Poisson Distribution Calculator")

    st.latex(r"""
    P(X = k) = \frac{e^{-\lambda} \lambda^k}{k!}
    """)

    lam = st.number_input("Enter the Rate (λ)", value=.0, step=0.1, min_value=0.0)
    x_min = st.number_input("Enter the Minimum Number of Occurrences (x_min)", value=0, step=1, min_value=0)
    x_max = st.number_input("Enter the Maximum Number of Occurrences (x_max)", value=10, step=1, min_value=x_min)

    mean, std_dev = calculate_poisson_distribution_stats(lam)

    st.write(f"Mean: {mean:.4f}")
    st.write(f"Standard Deviation: {std_dev:.4f}")

    st.header("Calculate P(X = x) for specific values")
    x_values_input = st.text_input("Enter values of x (separated by commas)", value="0, 1, 2")
    
    try:
        x_values = [int(x.strip()) for x in x_values_input.split(",")]
        valid_x_values = [x for x in x_values if x >= 0]
        
        if valid_x_values:
            for x in valid_x_values:
                prob = poisson.pmf(x, lam)
                st.write(f"P(X = {x}): {prob:.4f}")
        else:
            st.warning("Please enter valid x values.")
    except ValueError:
        st.error("Invalid input for x values. Please enter integers separated by commas.")
    
    plot_poisson_distribution(lam, x_min, x_max)

if __name__ == "__main__":
    main()
