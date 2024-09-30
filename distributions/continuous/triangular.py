import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import triang


def calculate_triangular_distribution_stats(a: float, b: float, c: float) -> tuple[float, float, float]:
    """
    Calculate mean, standard deviation, and skewness for a triangular distribution.

    Args:
        a (float): Lower limit of the distribution.
        b (float): Upper limit of the distribution.
        c (float): Mode of the distribution.

    Returns:
        tuple: Mean, standard deviation, and skewness.
    """
    mean = (a + b + c) / 3
    variance = (a**2 + b**2 + c**2 - a*b - a*c - b*c) / 18
    std_dev = np.sqrt(variance)
    skew = (np.sqrt(2) * (a + b - 2*c) * (2*a - b - c) * (a - 2*b + c)) / (5 * variance**(3/2))
    return mean, std_dev, skew


def plot_triangular_distribution(a: float, b: float, c: float, x: float) -> None:
    """
    Plot the triangular distribution and highlight the area to the left of x.

    Args:
        a (float): Lower limit of the distribution.
        b (float): Upper limit of the distribution.
        c (float): Mode of the distribution.
        x (float): Point to highlight on the distribution.
    """
    x_vals = np.linspace(a, b, 1000)
    scale = b - a
    c_relative = (c - a) / scale
    y_vals = triang.pdf(x_vals, c_relative, loc=a, scale=scale)

    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, label="Triangular Distribution")
    ax.fill_between(x_vals, 0, y_vals, where=(x_vals <= x), color='blue', alpha=0.3, label=f"Area to the left of x = {x:.2f}")
    ax.axvline(x=x, color='red', linestyle='--', label=f'x = {x:.2f}')

    ax.set_title(f'Triangular Distribution (a={a}, b={b}, c={c})')
    ax.set_xlabel('Value')
    ax.set_ylabel('Probability Density')
    ax.legend()

    st.pyplot(fig)


def main():
    st.title("Triangular Distribution Calculator")

    st.latex(r"\text{Mean} = \frac{a + b + c}{3}")
    st.latex(r"\text{Variance} = \frac{a^2 + b^2 + c^2 - ab - ac - bc}{18}")
    st.latex(r"""
    P(x \leq X \leq y) = 
    \begin{cases}
    \int_{x}^{y} \frac{2(t-a)}{(b-a)(c-a)} \, dt & \text{for } x \leq c \leq y \\
    \int_{x}^{y} \frac{2(b-t)}{(b-a)(b-c)} \, dt & \text{for } c < x \leq y
    \end{cases}
    """)

    a = st.number_input("Enter the Lower Limit (a)", value=0.0, step=0.1)
    b = st.number_input("Enter the Upper Limit (b)", value=1.0, step=0.1)
    c = st.number_input("Enter the Mode (c)", value=0.5, step=0.1)

    if a > b:
        st.error("Lower limit 'a' must be less than or equal to upper limit 'b'.")
        return

    if a > c or c > b:
        st.error("The mode 'c' must lie between 'a' and 'b'.")
        return

    default_x = (a + b) / 2
    x = st.number_input("Enter the value of x", value=default_x, step=0.1, min_value=a, max_value=b)

    mean, std_dev, skew = calculate_triangular_distribution_stats(a, b, c)

    f_x = triang.pdf(x, (c - a) / (b - a), loc=a, scale=b - a)
    p_x = triang.cdf(x, (c - a) / (b - a), loc=a, scale=b - a)

    st.write(f"Mean: {mean:.4f}")
    st.write(f"Standard Deviation: {std_dev:.4f}")
    st.write(f"Skewness: {skew:.4f}")
    st.write(f"Height at x (f(x)): {f_x:.4f}")
    st.write(f"Cumulative Probability P(X < x): {p_x:.4f}")
    st.write(f"Cumulative Probability P(X >= x): {1-p_x:.4f}")

    plot_triangular_distribution(a, b, c, x)


if __name__ == "__main__":
    main()