import streamlit as st
import math
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

def main():
    # Function to calculate margin of error for mean (sigma known)
    def calculate_moe_mean_known(z_score, std_dev, sample_size):
        return z_score * (std_dev / math.sqrt(sample_size))

    # Function to calculate margin of error for mean (sigma unknown, using t-distribution)
    def calculate_moe_mean_unknown(t_score, sample_std_dev, sample_size):
        return t_score * (sample_std_dev / math.sqrt(sample_size))

    # Function to calculate margin of error for proportion
    def calculate_moe_proportion(z_score, proportion, sample_size):
        return z_score * math.sqrt((proportion * (1 - proportion)) / sample_size)

    # Function to calculate Z or t score based on confidence level
    def get_z_score(confidence_level):
        return stats.norm.ppf(1 - (1 - confidence_level / 100) / 2)

    def get_t_score(confidence_level, sample_size):
        return stats.t.ppf(1 - (1 - confidence_level / 100) / 2, df=sample_size - 1)

    # Plot normal distribution centered around mean/proportion with MOE and adjusted scaling
    def plot_normal_distribution_with_moe(center, moe, std_error, confidence_level):
        # Define the x-axis limits based on standard error, so it covers ~99.7% of the distribution (3 standard errors)
        lower_bound = center - 3 * std_error
        upper_bound = center + 3 * std_error
        x = np.linspace(lower_bound, upper_bound, 1000)

        # Calculate the normal distribution (mean=center, std=std_error)
        y = stats.norm.pdf(x, loc=center, scale=std_error)

        # Create the plot
        fig, ax = plt.subplots()
        ax.plot(x, y, label="Normal Distribution")

        # Calculate the bounds for the confidence interval
        confidence_interval_lower = center - moe
        confidence_interval_upper = center + moe

        # Highlight the confidence interval region (center - MOE to center + MOE)
        ax.fill_between(x, 0, y, where=(x >= confidence_interval_lower) & (x <= confidence_interval_upper),
                        color='blue', alpha=0.3, label=f'{confidence_level}% Confidence Interval')

        # Plot MOE lines
        ax.axvline(x=confidence_interval_lower, color='red', linestyle='--', label=f'Lower Bound = {confidence_interval_lower:.2f}')
        ax.axvline(x=confidence_interval_upper, color='red', linestyle='--', label=f'Upper Bound = {confidence_interval_upper:.2f}')
        ax.axvline(x=center, color='green', linestyle='-', label=f'Center = {center:.2f}')
        
        # Set labels and title
        ax.set_title(f'Normal Distribution with {confidence_level}% Confidence Interval')
        ax.set_xlabel('Value')
        ax.set_ylabel('Probability Density')
        ax.legend()

        # Display the plot in Streamlit
        st.pyplot(fig)

    # Streamlit App
    st.title("Margin of Error Calculator with Interpretation and Plot")

    # Display LaTeX formulas at the top
    st.latex(r"\text{MOE for Mean (known } \sigma\text{)} = Z \cdot \frac{\sigma}{\sqrt{n}}")
    st.latex(r"\text{MOE for Mean (unknown } \sigma\text{)} = t \cdot \frac{s}{\sqrt{n}}")
    st.latex(r"\text{MOE for Proportion} = Z \cdot \sqrt{\frac{p(1 - p)}{n}}")

    # User selects between mean and proportion
    calculation_type = st.selectbox("Calculate MOE for:", ["Mean", "Proportion"])

    # Common inputs
    sample_size = st.number_input("Enter Sample Size (n)", min_value=1, value=30, step=1)
    confidence_level = st.slider("Select Confidence Level (%)", min_value=50, max_value=99, value=95, step=1)

    # If calculating for mean
    if calculation_type == "Mean":
        sigma_known = st.selectbox("Is Standard Deviation (σ) known?", ["Yes", "No"])
        
        if sigma_known == "Yes":
            # Known sigma (Z-distribution)
            z_score = get_z_score(confidence_level)
            std_dev = st.number_input("Enter Population Standard Deviation (σ)", value=1.0, step=0.1)
            sample_mean = st.number_input("Enter Sample Mean (x̄)", value=0.0, step=0.1)
            std_error = std_dev / math.sqrt(sample_size)

            moe = calculate_moe_mean_known(z_score, std_dev, sample_size)

            # Display Standard Error, MOE, and Confidence Interval
            st.success(f"Standard Error: {std_error:.4f}")
            st.success(f"Margin of Error (MOE): {moe:.4f}")
            st.success(f"Confidence Interval: ({sample_mean - moe:.4f}, {sample_mean + moe:.4f})")
            
            # Plot the normal distribution with MOE and center
            plot_normal_distribution_with_moe(sample_mean, moe, std_error, confidence_level)

            # Interpretation
            st.write(f"With a confidence level of {confidence_level}%, we expect that the true population mean lies within ±{moe:.4f} of the sample mean, i.e., between {sample_mean - moe:.4f} and {sample_mean + moe:.4f}.")
        
        else:
            # Unknown sigma (t-distribution)
            sample_std_dev = st.number_input("Enter Sample Standard Deviation (s)", value=1.0, step=0.1)
            sample_mean = st.number_input("Enter Sample Mean (x̄)", value=0.0, step=0.1)
            t_score = get_t_score(confidence_level, sample_size)
            std_error = sample_std_dev / math.sqrt(sample_size)
            
            moe = calculate_moe_mean_unknown(t_score, sample_std_dev, sample_size)

            # Display Standard Error, MOE, and Confidence Interval
            st.success(f"Standard Error: {std_error:.4f}")
            st.success(f"Margin of Error (MOE): {moe:.4f}")
            st.success(f"Confidence Interval: ({sample_mean - moe:.4f}, {sample_mean + moe:.4f})")

            # Plot the normal distribution with MOE and center
            plot_normal_distribution_with_moe(sample_mean, moe, std_error, confidence_level)

            # Interpretation
            st.write(f"With a confidence level of {confidence_level}%, we expect that the true population mean lies within ±{moe:.4f} of the sample mean, i.e., between {sample_mean - moe:.4f} and {sample_mean + moe:.4f}.")

    # If calculating for proportion
    elif calculation_type == "Proportion":
        z_score = get_z_score(confidence_level)
        proportion = st.number_input("Enter Proportion (p)", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        std_error = math.sqrt((proportion * (1 - proportion)) / sample_size)
        
        moe = calculate_moe_proportion(z_score, proportion, sample_size)

        # Display Standard Error, MOE, and Confidence Interval
        st.success(f"Standard Error: {std_error:.4f}")
        st.success(f"Margin of Error (MOE): {moe:.4f}")
        st.success(f"Confidence Interval: ({proportion - moe:.4f}, {proportion + moe:.4f})")

        # Plot the normal distribution with MOE and center
        plot_normal_distribution_with_moe(proportion, moe, std_error, confidence_level)

        # Interpretation
        st.write(f"With a confidence level of {confidence_level}%, we expect that the true population proportion lies within ±{moe:.4f} of the sample proportion, i.e., between {proportion - moe:.4f} and {proportion + moe:.4f}.")

if __name__ == "__main__":
    main()
