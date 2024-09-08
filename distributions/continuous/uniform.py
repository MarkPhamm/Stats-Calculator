import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform

def main():

    # Function to calculate mean and standard deviation for a uniform distribution
    def calculate_uniform_distribution_stats(a, b):
        mean = (a + b) / 2
        std_dev = (b - a) / np.sqrt(12)
        return mean, std_dev

    # Function to plot uniform distribution
    def plot_uniform_distribution(a, b, x):
        # Define the x-axis limits
        x_vals = np.linspace(a - 0.1, b + 0.1, 1000)
        
        # Create the uniform distribution
        y_vals = uniform.pdf(x_vals, loc=a, scale=b - a)
        
        # Create the plot
        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals, label="Uniform Distribution")
        
        # Highlight the area under the curve to the left of x
        ax.fill_between(x_vals, 0, y_vals, where=(x_vals <= x), color='blue', alpha=0.3, label=f"Area to the left of x = {x:.2f}")
        
        # Plot the vertical line at x
        ax.axvline(x=x, color='red', linestyle='--', label=f'x = {x:.2f}')
        
        # Set labels and title
        ax.set_title(f'Uniform Distribution (a={a}, b={b})')
        ax.set_xlabel('Value')
        ax.set_ylabel('Probability Density')
        ax.legend()
        
        # Display the plot in Streamlit
        st.pyplot(fig)

    # Streamlit App
    st.title("Uniform Distribution Calculator")

    # Display LaTeX formulas for mean and variance
    st.latex(r"\text{Mean: } \mu = \frac{a + b}{2}")
    st.latex(r"\text{Variance: } \sigma^2 = \frac{(b - a)^2}{12}")
    st.latex(r"P(a \leq X \leq b) = \int_{a}^{b} \frac{1}{b-a} \, dx = \frac{b - a}{b - a} = 1")
    st.latex(r"P(x \leq X \leq y) = \int_{x}^{y} \frac{1}{b-a} \, dt = \frac{y - x}{b - a}")



    # User inputs for a, b (uniform distribution parameters)
    a = st.number_input("Enter the Lower Limit (a)", value=0.0, step=0.1)
    b = st.number_input("Enter the Upper Limit (b)", value=1.0, step=0.1)

    # Check for invalid inputs and raise errors if conditions are violated
    if a > b:
        st.error("Lower limit 'a' must be less than or equal to upper limit 'b'.")
    else:
        # Set a dynamic default value for x based on the current values of a and b
        default_x = (a + b) / 2  # Default to the midpoint of a and b

        # User input for x
        x = st.number_input("Enter the value of x", value=default_x, step=0.1, min_value=a, max_value=b)

        # Calculate the uniform distribution stats
        mean, std_dev = calculate_uniform_distribution_stats(a, b)

        # Calculate cumulative probabilities P(X < x) and P(X >= x)
        p_less_than_x = uniform.cdf(x, loc=a, scale=b - a)  # CDF at x
        p_greater_equal_x = 1 - p_less_than_x  # P(X >= x)

        # Display results
        st.write(f"Mean: {mean:.4f}")
        st.write(f"Standard Deviation: {std_dev:.4f}")
        st.write(f"Cumulative Probability P(X < x): {p_less_than_x:.4f}")
        st.write(f"Cumulative Probability P(X >= x): {p_greater_equal_x:.4f}")

        # Plot the uniform distribution with area to the left of x
        plot_uniform_distribution(a, b, x)

if __name__ == "__main__":
    main()
