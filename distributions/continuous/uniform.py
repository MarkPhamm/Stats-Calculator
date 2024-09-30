import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform


def calculate_uniform_distribution_stats(a: float, b: float) -> tuple[float, float]:
    """
    Calculate mean and standard deviation for a uniform distribution.

    Args:
        a (float): Lower limit of the distribution.
        b (float): Upper limit of the distribution.

    Returns:
        tuple: Mean and standard deviation.
    """
    mean = (a + b) / 2
    std_dev = (b - a) / np.sqrt(12)
    return mean, std_dev


def plot_uniform_distribution(a: float, b: float, x: float) -> None:
    """
    Plot the uniform distribution and highlight the area to the left of x.

    Args:
        a (float): Lower limit of the distribution.
        b (float): Upper limit of the distribution.
        x (float): Point to highlight on the distribution.
    """
    x_vals = np.linspace(a - 0.1, b + 0.1, 1000)
    y_vals = uniform.pdf(x_vals, loc=a, scale=b - a)

    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, label="Uniform Distribution")
    ax.fill_between(x_vals, 0, y_vals, where=(x_vals <= x), color='blue', alpha=0.3, label=f"Area to the left of x = {x:.2f}")
    ax.axvline(x=x, color='red', linestyle='--', label=f'x = {x:.2f}')

    ax.set_title(f'Uniform Distribution (a={a}, b={b})')
    ax.set_xlabel('Value')
    ax.set_ylabel('Probability Density')
    ax.legend()

    st.pyplot(fig)


def main():
    st.title("Uniform Distribution Calculator")

    st.latex(r"\text{Mean: } \mu = \frac{a + b}{2}")
    st.latex(r"\text{Variance: } \sigma^2 = \frac{(b - a)^2}{12}")
    st.latex(r"P(a \leq X \leq b) = \int_{a}^{b} \frac{1}{b-a} \, dx = \frac{b - a}{b - a} = 1")
    st.latex(r"P(x \leq X \leq y) = \int_{x}^{y} \frac{1}{b-a} \, dt = \frac{y - x}{b - a}")

    a = st.number_input("Enter the Lower Limit (a)", value=0.0, step=0.1)
    b = st.number_input("Enter the Upper Limit (b)", value=1.0, step=0.1)

    if a > b:
        st.error("Lower limit 'a' must be less than or equal to upper limit 'b'.")
        return

    default_x = (a + b) / 2
    x = st.number_input("Enter the value of x", value=default_x, step=0.1, min_value=a, max_value=b)

    mean, std_dev = calculate_uniform_distribution_stats(a, b)

    p_less_than_x = uniform.cdf(x, loc=a, scale=b - a)
    p_greater_equal_x = 1 - p_less_than_x

    st.write(f"Mean: {mean:.4f}")
    st.write(f"Standard Deviation: {std_dev:.4f}")
    st.write(f"Cumulative Probability P(X < x): {p_less_than_x:.4f}")
    st.write(f"Cumulative Probability P(X >= x): {p_greater_equal_x:.4f}")

    plot_uniform_distribution(a, b, x)


if __name__ == "__main__":
    main()
