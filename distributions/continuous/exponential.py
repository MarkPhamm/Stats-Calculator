import streamlit as st
import math
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

def plot_exponential_distribution(rate, x, y=None):
    lower_bound = 0
    upper_bound = max(5 / rate, x + 1)  # Ensure the plot covers a reasonable range
    x_vals = np.linspace(lower_bound, upper_bound, 1000)
    y_vals = stats.expon.pdf(x_vals, scale=1/rate)

    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, label="Exponential Distribution")
    ax.axvline(x=x, color='red', linestyle='--', label=f'x = {x:.2f}')

    if y is None:
        ax.fill_between(x_vals, 0, y_vals, where=(x_vals <= x), color='blue', alpha=0.3, label="Area to the left of x")
        ax.fill_between(x_vals, 0, y_vals, where=(x_vals > x), color='orange', alpha=0.3, label="Area to the right of x")
    else:
        ax.axvline(x=y, color='green', linestyle='--', label=f'y = {y:.2f}')
        ax.fill_between(x_vals, 0, y_vals, where=(x_vals <= x), color='blue', alpha=0.3, label="Area to the left of x")
        ax.fill_between(x_vals, 0, y_vals, where=((x_vals >= x) & (x_vals <= y)), color='purple', alpha=0.3, label="Area between x and y")
        ax.fill_between(x_vals, 0, y_vals, where=(x_vals > y), color='orange', alpha=0.3, label="Area to the right of y")

    ax.set_title(f'Exponential Distribution (rate = {rate})')
    ax.set_xlabel('Value')
    ax.set_ylabel('Probability Density')
    ax.legend()

    st.pyplot(fig)

def exponential_distribution():
    st.title("Exponential Distribution Calculator")
    st.latex(r"\text{PDF}(x) = \lambda e^{-\lambda x}")
    st.latex(r"\text{CDF}(x) = 1 - e^{-\lambda x}")
    st.latex(r"\lambda = \frac{1}{\mu}")

    rate = st.number_input("Enter the Rate (λ)", value=1.0, step=0.1, min_value=0.1)
    x = st.number_input("Enter the value of x", value=1.0, step=0.1, min_value=0.0)
    y_input = st.text_input("Enter the value of y (optional)", value="", placeholder="Leave empty if not needed")

    y = float(y_input) if y_input else None

    if y is None:
        area_left = stats.expon.cdf(x, scale=1/rate)
        area_right = 1 - area_left
        st.success(f"Area to the left of x: {area_left:.4f} and Area to the right of x: {area_right:.4f}")
    else:
        area_left_x = stats.expon.cdf(x, scale=1/rate)
        area_right_x = 1 - area_left_x
        area_left_y = stats.expon.cdf(y, scale=1/rate)
        area_right_y = 1 - area_left_y
        area_between = area_left_y - area_left_x
        st.success(f"Area between x and y: {area_between:.4f}")
        st.success(f"Area to the left of x: {area_left_x:.4f} and Area to the right of x: {area_right_x:.4f}")
        st.success(f"Area to the left of y: {area_left_y:.4f} and Area to the right of y: {area_right_y:.4f}")

    plot_exponential_distribution(rate, x, y=y)

def inverse_exponential_distribution():
    st.title("Inverse Exponential Distribution")
    st.latex(r"x = \text{CDF}^{-1}(p) = -\frac{\ln(1-p)}{\lambda}")
    st.latex(r"\lambda = \frac{1}{\mu}")

    rate = st.number_input("Enter the Rate (λ)", value=1.0, step=0.1, min_value=0.1)
    area_left = st.slider("Enter the percentage of area to the left (as %)", min_value=0.01, max_value=99.99, value=50.0, step=0.01)

    proportion_left = area_left / 100
    x = stats.expon.ppf(proportion_left, scale=1/rate)

    st.success(f"The value of x such that {area_left:.2f}% of the distribution is to the left is: {x:.4f}")
    plot_exponential_distribution(rate, x)

def main():
    calculation_type = st.sidebar.radio("Choose calculation type:", ["Exponential", "Inverse Exponential"])

    if calculation_type == "Exponential":
        exponential_distribution()
    elif calculation_type == "Inverse Exponential":
        inverse_exponential_distribution()

if __name__ == "__main__":
    main()
