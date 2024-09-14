import streamlit as st
import math
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt


def main():
    # Create a radio button in the sidebar
    calculation_type = st.sidebar.radio("Choose calculation type:", ["Normal", "Inverse"])

    if calculation_type == "Normal":
        # Function to plot normal distribution with two vertical lines at x and y
        def plot_normal_distribution_with_x_and_y(mean, std_dev, x, y=None, sample_size=None, population=True):
            # Define the x-axis limits based on standard deviation, so it covers ~99.7% of the distribution (3 standard deviations)
            lower_bound = mean - 3 * std_dev
            upper_bound = mean + 3 * std_dev
            x_vals = np.linspace(lower_bound, upper_bound, 1000)

            # Calculate the normal distribution (mean=mean, std=std_dev)
            if population:
                y_vals = stats.norm.pdf(x_vals, loc=mean, scale=std_dev)
            else:
                std_error = std_dev / math.sqrt(sample_size)
                y_vals = stats.norm.pdf(x_vals, loc=mean, scale=std_error)

            # Create the plot
            fig, ax = plt.subplots()
            ax.plot(x_vals, y_vals, label="Normal Distribution")

            # Plot the vertical line at x
            ax.axvline(x=x, color='red', linestyle='--', label=f'x = {x:.2f}')
            if y is None:
            # Highlight the area to the left and right of x
                ax.fill_between(x_vals, 0, y_vals, where=(x_vals <= x), color='blue', alpha=0.3, label="Area to the left of x")
                ax.fill_between(x_vals, 0, y_vals, where=(x_vals > x), color='orange', alpha=0.3, label="Area to the right of x")

            # If y is provided, plot the vertical line at y and highlight the area between x and y
            if y is not None:
                ax.axvline(x=y, color='green', linestyle='--', label=f'y = {y:.2f}')
                ax.fill_between(x_vals, 0, y_vals, where=(x_vals <= x), color='blue', alpha=0.3, label="Area to the left of x")
                # Highlight the area between x and y
                ax.fill_between(x_vals, 0, y_vals, where=((x_vals >= x) & (x_vals <= y)), color='purple', alpha=0.3, label="Area between x and y")
                ax.fill_between(x_vals, 0, y_vals, where=(x_vals > y), color='orange', alpha=0.3, label="Area to the right of y")

            # Set labels and title
            ax.set_title(f'Normal Distribution (mean = {mean}, std_dev = {std_dev})')
            ax.set_xlabel('Value')
            ax.set_ylabel('Probability Density')
            ax.legend()

            # Display the plot in Streamlit
            st.pyplot(fig)

        # Streamlit App
        st.title("Normal Distribution Calculator")

        # LaTeX formula for Normal PDF
        st.latex(r"\text{PDF}(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}")

        # LaTeX formula for Normal CDF
        st.latex(r"\text{CDF}(x) = P(X \leq x) = \int_{-\infty}^{x} \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(t-\mu)^2}{2\sigma^2}} dt")

        # User inputs for mean and standard deviation
        mean = st.number_input("Enter the Mean (μ)", value=0.0, step=0.1)
        std_dev = st.number_input("Enter the Standard Deviation (σ)", value=1.0, step=0.1)

        # User inputs for x and optional y values
        x = st.number_input("Enter the value of x", value=0.0, step=0.1)
        y_input = st.text_input("Enter the value of y (optional)", value="", placeholder="Leave empty if not needed")

        # Convert y_input to a float if provided
        y = float(y_input) if y_input else None

        if y is None:
            # Calculate the areas to the left and right of x
            area_left = stats.norm.cdf(x, loc=mean, scale=std_dev)
            area_right = 1 - area_left

            # Display results
            st.success(f"Area to the left of x: {area_left:.4f} and Area to the right of x: {area_right:.4f}")
            
            # Plot the normal distribution and areas, based on whether y is provided or not
            plot_normal_distribution_with_x_and_y(mean, std_dev, x, y=y, sample_size=None, population=True)

        else:
            area_left_x = stats.norm.cdf(x, loc=mean, scale=std_dev)
            area_right_x = 1 - area_left_x

            area_left_y = stats.norm.cdf(y, loc=mean, scale=std_dev)
            area_right_y = 1 - area_left_y

            area_between = area_left_y - area_left_x

            # Display results
            st.success(f"Area to the between x and y: {area_between:.4f}")
            st.success(f"Area to the left of x: {area_left_x:.4f} and Area to the right of x: {area_right_x:.4f}")
            st.success(f"Area to the left of y: {area_left_y:.4f} and Area to the right of y: {area_right_y:.4f}")

            # Plot the normal distribution and areas, based on whether y is provided or not
            plot_normal_distribution_with_x_and_y(mean, std_dev, x, y=y, sample_size=None, population=True)

    elif calculation_type == "Inverse":
        # Function to plot normal distribution with vertical line at x
        def plot_normal_distribution_with_x(mean, std_dev, x):
            # Define the x-axis limits based on standard deviation, so it covers ~99.7% of the distribution (3 standard deviations)
            lower_bound = mean - 4 * std_dev
            upper_bound = mean + 4 * std_dev
            x_vals = np.linspace(lower_bound, upper_bound, 1000)

            # Calculate the normal distribution (mean=mean, std=std_dev)
            y = stats.norm.pdf(x_vals, loc=mean, scale=std_dev)

            # Create the plot
            fig, ax = plt.subplots()
            ax.plot(x_vals, y, label="Normal Distribution")

            # Highlight the area under the curve to the left of x
            ax.fill_between(x_vals, 0, y, where=(x_vals <= x), color='blue', alpha=0.3, label="Area to the left of x")

            # Plot the vertical line at x
            ax.axvline(x=x, color='red', linestyle='--', label=f'x = {x:.2f}')

            # Set labels and title
            ax.set_title(f'Normal Distribution (mean = {mean}, std_dev = {std_dev})')
            ax.set_xlabel('Value')
            ax.set_ylabel('Probability Density')
            ax.legend()

            # Display the plot in Streamlit
            st.pyplot(fig)

        # Streamlit App
        st.title("Inverse Normal Distribution")

        # LaTeX formula for Inverse Normal CDF
        st.latex(r"x = \text{CDF}^{-1}(p) = \mu + \sigma \cdot \Phi^{-1}(p)")

        # User inputs for mean and standard deviation
        mean = st.number_input("Enter the Mean (μ)", value=0.0, step=0.1)
        std_dev = st.number_input("Enter the Standard Deviation (σ)", value=1.0, step=0.1)

        # User inputs the percentage to the left
        area_left = st.slider("Enter the percentage of area to the left (as %)", min_value=0.01, max_value=99.99, value=50.0, step=0.01)

        # Convert the percentage to a proportion
        proportion_left = area_left / 100

        # Calculate the corresponding x value using the inverse cumulative distribution function (ppf)
        x = stats.norm.ppf(proportion_left, loc=mean, scale=std_dev)

        # Display the calculated x value
        st.success(f"The value of x such that {area_left:.2f}% of the distribution is to the left is: {x:.4f}")

        # Plot the normal distribution and highlight the area to the left of x
        plot_normal_distribution_with_x(mean, std_dev, x)

if __name__ == "__main__":
    main()
