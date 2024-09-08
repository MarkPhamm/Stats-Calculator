import streamlit as st
import math
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

def main():
    # Create a radio button in the sidebar
    calculation_type = st.sidebar.radio("Choose calculation type:", ["Normal", "Inverse"])

    # Example branching based on the selected radio button
    if calculation_type == "Normal":
        # Function to plot normal distribution with vertical line at x
        def plot_normal_distribution_with_x(mean, std_dev, x, sample_size, population=True):
            # Define the x-axis limits based on standard deviation, so it covers ~99.7% of the distribution (3 standard deviations)
            lower_bound = mean - 4 * std_dev
            upper_bound = mean + 4 * std_dev
            x_vals = np.linspace(lower_bound, upper_bound, 1000)

            # Calculate the normal distribution (mean=mean, std=std_dev)
            if population:
                y = stats.norm.pdf(x_vals, loc=mean, scale=std_dev)
            else:
                std_error = std_dev / math.sqrt(sample_size)
                y = stats.norm.pdf(x_vals, loc=mean, scale=std_error)

            # Create the plot
            fig, ax = plt.subplots()
            ax.plot(x_vals, y, label="Normal Distribution")

            # Highlight the area under the curve to the left of x
            ax.fill_between(x_vals, 0, y, where=(x_vals <= x), color='blue', alpha=0.3, label="Area to the left of x")
            
            # Highlight the area under the curve to the right of x
            ax.fill_between(x_vals, 0, y, where=(x_vals > x), color='orange', alpha=0.3, label="Area to the right of x")

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
        st.title("Normal Distribution")
        st.header("Calculate area to the left and right of x")

        # LaTeX formula for Normal CDF
        st.latex(r"\text{CDF}(x) = P(X \leq x) = \int_{-\infty}^{x} \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(t-\mu)^2}{2\sigma^2}} dt")

        # User inputs for mean and standard deviation
        mean = st.number_input("Enter the Mean (μ)", value=0.0, step=0.1)
        std_dev = st.number_input("Enter the Standard Deviation (σ)", value=1.0, step=0.1)

        # User inputs x value
        x = st.number_input("Enter the value of x", value=0.0, step=0.1)


        area_left = stats.norm.cdf(x, loc=mean, scale=std_dev)
        area_right = 1 - area_left

        # Display results
        st.success(f"Area to the left of x: {area_left:.4f} and Area to the right of x: {area_right:.4f}")

        # Plot the normal distribution and areas
        plot_normal_distribution_with_x(mean, std_dev, x, sample_size=None, population=True)

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
        st.header("Find x from Area under Normal Distribution")

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
        st.write(f"The value of x such that {area_left:.2f}% of the distribution is to the left is: {x:.4f}")

        # Plot the normal distribution and highlight the area to the left of x
        plot_normal_distribution_with_x(mean, std_dev, x)

if __name__ == "__main__":
    main()
