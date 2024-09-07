import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

def main():
    # Function to calculate mean and standard deviation for a binomial distribution
    def calculate_binomial_distribution_stats(n, p):
        mean = n * p
        variance = n * p * (1 - p)
        std_dev = np.sqrt(variance)
        return mean, std_dev

    # Function to plot binomial distribution
    def plot_binomial_distribution(n, p, s_min, s_max):
        # Define the x-axis values for the possible outcomes (0 to n)
        x_vals = np.arange(0, n + 1)
        
        # Create the binomial distribution
        y_vals = binom.pmf(x_vals, n, p)
        
        # Create the plot
        fig, ax = plt.subplots()
        ax.bar(x_vals, y_vals, label="Binomial Distribution", alpha=0.7)
        
        # Highlight the bars in the range [s_min, s_max]
        mask = (x_vals >= s_min) & (x_vals <= s_max)
        ax.bar(x_vals[mask], y_vals[mask], color='blue', alpha=0.5, label=f"P({s_min} <= X <= {s_max})")
        
        # Plot the vertical lines at s_min and s_max
        ax.axvline(x=s_min, color='red', linestyle='--', label=f's_min = {s_min}')
        ax.axvline(x=s_max, color='green', linestyle='--', label=f's_max = {s_max}')
        
        # Set labels and title
        ax.set_title(f'Binomial Distribution (n={n}, p={p})')
        ax.set_xlabel('Number of Successes')
        ax.set_ylabel('Probability Mass')
        ax.legend()
        
        # Display the plot in Streamlit
        st.pyplot(fig)

    # Streamlit App
    st.title("Binomial Distribution Calculator")

    # User inputs for n, p (binomial distribution parameters)
    n = st.number_input("Enter the Number of Trials (n)", value=10, step=1, min_value=1)
    p = st.number_input("Enter the Probability of Success (p)", value=0.5, step=0.01, min_value=0.0, max_value=1.0)

    # Set default values for s_min and s_max based on the current values of n
    default_s_min = 0  # Minimum successes
    default_s_max = n  # Maximum successes

    # User inputs for s_min and s_max (range of number of successes)
    s_min = st.number_input("Enter the Minimum Number of Successes (s_min)", value=default_s_min, step=1, min_value=0, max_value=n)
    s_max = st.number_input("Enter the Maximum Number of Successes (s_max)", value=default_s_max, step=1, min_value=s_min, max_value=n)

    # Calculate the binomial distribution stats
    mean, std_dev = calculate_binomial_distribution_stats(n, p)

    # Calculate probabilities P(s_min <= X <= s_max) and P(X <= s_max)
    p_range = binom.cdf(s_max, n, p) - binom.cdf(s_min - 1, n, p)  # P(s_min <= X <= s_max)
    p_less_than_equal_s_max = binom.cdf(s_max, n, p) # P(X <= s_max)
    p_less_than_equal_s_min = binom.cdf(s_min, n, p) # P(X <= s_min)

    # Display results
    st.write(f"Mean: {mean:.4f}")
    st.write(f"Standard Deviation: {std_dev:.4f}")
    st.write(f"Cumulative Probability P(X <= {s_min}): {p_less_than_equal_s_min:.4f}")
    st.write(f"Cumulative Probability P(X <= {s_max}): {p_less_than_equal_s_max:.4f}")

    st.success(f"Probability P({s_min} <= X <= {s_max}): {p_range:.4f}")

    # Let user input multiple values of x to calculate P(X = x)
    st.header("Calculate P(X = x) for specific values")
    x_values_input = st.text_input("Enter values of x (separated by commas)", value="0, 1, 2")
    
    # Convert the user input into a list of integers
    try:
        x_values = [int(x.strip()) for x in x_values_input.split(",")]
        valid_x_values = [x for x in x_values if 0 <= x <= n]  # Ensure x values are within valid range
        
        if len(valid_x_values) > 0:
            # Display the probabilities for the input x values
            for x in valid_x_values:
                prob = binom.pmf(x, n, p)
                st.write(f"P(X = {x}): {prob:.4f}")
        else:
            st.warning("Please enter valid x values between 0 and n.")
    except ValueError:
        st.error("Invalid input for x values. Please enter integers separated by commas.")
    
    # Plot the binomial distribution with the range of successes highlighted
    plot_binomial_distribution(n, p, s_min, s_max)

if __name__ == "__main__":
    main()
