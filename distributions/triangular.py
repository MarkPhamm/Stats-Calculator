import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import triang


def main():
    # Function to calculate mean, standard deviation, and skewness for a triangular distribution
    def calculate_triangular_distribution_stats(a, b, c):
        mean = (a + b + c) / 3
        variance = (a**2 + b**2 + c**2 - a*b - a*c - b*c) / 18
        std_dev = np.sqrt(variance)
        skew = (np.sqrt(2) * (a + b - 2 * c) * (2 * a - b - c) * (a - 2 * b + c)) / (5 * variance**(3 / 2))
        return mean, std_dev, skew

    # Function to plot triangular distribution
    def plot_triangular_distribution(a, b, c, x):
        # Define the x-axis limits
        x_vals = np.linspace(a, b, 1000)

        # Create the triangular distribution
        scale = b - a
        c_relative = (c - a) / scale  # Relative mode (as proportion of scale)
        y_vals = triang.pdf(x_vals, c_relative, loc=a, scale=scale)

        # Create the plot
        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals, label="Triangular Distribution")

        # Highlight the area under the curve to the left of x
        ax.fill_between(x_vals, 0, y_vals, where=(x_vals <= x), color='blue', alpha=0.3, label=f"Area to the left of x = {x:.2f}")

        # Plot the vertical line at x
        ax.axvline(x=x, color='red', linestyle='--', label=f'x = {x:.2f}')

        # Set labels and title
        ax.set_title(f'Triangular Distribution (a={a}, b={b}, c={c})')
        ax.set_xlabel('Value')
        ax.set_ylabel('Probability Density')
        ax.legend()

        # Display the plot in Streamlit
        st.pyplot(fig)

    # Streamlit App
    st.title("Triangular Distribution Calculator")

    # User inputs for a, b, c (triangular distribution parameters)
    a = st.number_input("Enter the Lower Limit (a)", value=0.0, step=0.1)
    b = st.number_input("Enter the Upper Limit (b)", value=1.0, step=0.1)
    c = st.number_input("Enter the Mode (c)", value=0.5, step=0.1)

    # Check for invalid inputs and raise errors if conditions are violated
    if a > b:
        st.error("Lower limit 'a' must be less than or equal to upper limit 'b'.")
    elif a > c or c > b:
        st.error("The mode 'c' must lie between 'a' and 'b'.")
    else:
        # Set a dynamic default value for x based on the current values of a and b
        default_x = (a + b) / 2  # Default to the midpoint of a and b

        # User input for x
        x = st.number_input("Enter the value of x", value=default_x, step=0.1, min_value=a, max_value=b)

        # Calculate the triangular distribution stats
        mean, std_dev, skew = calculate_triangular_distribution_stats(a, b, c)

        # Calculate the height at x (f(x)) and cumulative probability P(X < x)
        f_x = triang.pdf(x, (c - a) / (b - a), loc=a, scale=b - a)  # PDF at x
        p_x = triang.cdf(x, (c - a) / (b - a), loc=a, scale=b - a)  # CDF at x

        # Display results
        st.write(f"Mean: {mean:.4f}")
        st.write(f"Standard Deviation: {std_dev:.4f}")
        st.write(f"Skewness: {skew:.4f}")
        st.write(f"Height at x (f(x)): {f_x:.4f}")
        st.write(f"Cumulative Probability P(X < x): {p_x:.4f}")
        st.write(f"Cumulative Probability P(X >= x): {1-p_x:.4f}")

        # Plot the triangular distribution with area to the left of x
        plot_triangular_distribution(a, b, c, x)

if __name__ == "__main__":
    main()