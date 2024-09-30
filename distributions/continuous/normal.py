import streamlit as st
import math
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt


def plot_normal_distribution(mean, std_dev, x, y=None, sample_size=None, population=True):
    lower_bound = mean - 3 * std_dev
    upper_bound = mean + 3 * std_dev
    x_vals = np.linspace(lower_bound, upper_bound, 1000)

    if population:
        y_vals = stats.norm.pdf(x_vals, loc=mean, scale=std_dev)
    else:
        std_error = std_dev / math.sqrt(sample_size)
        y_vals = stats.norm.pdf(x_vals, loc=mean, scale=std_error)

    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, label="Normal Distribution")
    ax.axvline(x=x, color='red', linestyle='--', label=f'x = {x:.2f}')

    if y is None:
        ax.fill_between(x_vals, 0, y_vals, where=(x_vals <= x), color='blue', alpha=0.3, label="Area to the left of x")
        ax.fill_between(x_vals, 0, y_vals, where=(x_vals > x), color='orange', alpha=0.3, label="Area to the right of x")
    else:
        ax.axvline(x=y, color='green', linestyle='--', label=f'y = {y:.2f}')
        ax.fill_between(x_vals, 0, y_vals, where=(x_vals <= x), color='blue', alpha=0.3, label="Area to the left of x")
        ax.fill_between(x_vals, 0, y_vals, where=((x_vals >= x) & (x_vals <= y)), color='purple', alpha=0.3, label="Area between x and y")
        ax.fill_between(x_vals, 0, y_vals, where=(x_vals > y), color='orange', alpha=0.3, label="Area to the right of y")

    ax.set_title(f'Normal Distribution (mean = {mean}, std_dev = {std_dev})')
    ax.set_xlabel('Value')
    ax.set_ylabel('Probability Density')
    ax.legend()

    st.pyplot(fig)


def normal_distribution():
    st.title("Normal Distribution Calculator")
    st.latex(r"\text{PDF}(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}")
    st.latex(r"\text{CDF}(x) = P(X \leq x) = \int_{-\infty}^{x} \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(t-\mu)^2}{2\sigma^2}} dt")

    mean = st.number_input("Enter the Mean (μ)", value=0.0, step=0.1)
    std_dev = st.number_input("Enter the Standard Deviation (σ)", value=1.0, step=0.1)
    x = st.number_input("Enter the value of x", value=0.0, step=0.1)
    y_input = st.text_input("Enter the value of y (optional)", value="", placeholder="Leave empty if not needed")

    y = float(y_input) if y_input else None

    if y is None:
        area_left = stats.norm.cdf(x, loc=mean, scale=std_dev)
        area_right = 1 - area_left
        st.success(f"Area to the left of x: {area_left:.4f} and Area to the right of x: {area_right:.4f}")
    else:
        area_left_x = stats.norm.cdf(x, loc=mean, scale=std_dev)
        area_right_x = 1 - area_left_x
        area_left_y = stats.norm.cdf(y, loc=mean, scale=std_dev)
        area_right_y = 1 - area_left_y
        area_between = area_left_y - area_left_x
        st.success(f"Area between x and y: {area_between:.4f}")
        st.success(f"Area to the left of x: {area_left_x:.4f} and Area to the right of x: {area_right_x:.4f}")
        st.success(f"Area to the left of y: {area_left_y:.4f} and Area to the right of y: {area_right_y:.4f}")

    plot_normal_distribution(mean, std_dev, x, y=y, sample_size=None, population=True)


def inverse_normal_distribution():
    st.title("Inverse Normal Distribution")
    st.latex(r"x = \text{CDF}^{-1}(p) = \mu + \sigma \cdot \Phi^{-1}(p)")

    mean = st.number_input("Enter the Mean (μ)", value=0.0, step=0.1)
    std_dev = st.number_input("Enter the Standard Deviation (σ)", value=1.0, step=0.1)
    area_left = st.slider("Enter the percentage of area to the left (as %)", min_value=0.01, max_value=99.99, value=50.0, step=0.01)

    proportion_left = area_left / 100
    x = stats.norm.ppf(proportion_left, loc=mean, scale=std_dev)

    st.success(f"The value of x such that {area_left:.2f}% of the distribution is to the left is: {x:.4f}")
    plot_normal_distribution(mean, std_dev, x)


def main():
    calculation_type = st.sidebar.radio("Choose calculation type:", ["Normal", "Inverse"])

    if calculation_type == "Normal":
        normal_distribution()
    elif calculation_type == "Inverse":
        inverse_normal_distribution()


if __name__ == "__main__":
    main()
