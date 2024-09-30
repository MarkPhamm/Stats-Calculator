import streamlit as st
import math
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

def main():
    def calculate_moe_mean_known(z_score, std_dev, sample_size):
        return z_score * (std_dev / math.sqrt(sample_size))

    def calculate_moe_mean_unknown(t_score, sample_std_dev, sample_size):
        return t_score * (sample_std_dev / math.sqrt(sample_size))

    def calculate_moe_proportion(z_score, proportion, sample_size):
        return z_score * math.sqrt((proportion * (1 - proportion)) / sample_size)

    def get_z_score(confidence_level):
        return stats.norm.ppf((1 + confidence_level / 100) / 2)

    def get_t_score(confidence_level, sample_size):
        return stats.t.ppf((1 + confidence_level / 100) / 2, df=sample_size - 1)

    def plot_normal_distribution_with_moe(center, moe, std_error, confidence_level):
        x = np.linspace(center - 3 * std_error, center + 3 * std_error, 1000)
        y = stats.norm.pdf(x, loc=center, scale=std_error)

        fig, ax = plt.subplots()
        ax.plot(x, y, label="Normal Distribution")

        ci_lower = center - moe
        ci_upper = center + moe

        ax.fill_between(x, 0, y, where=(x >= ci_lower) & (x <= ci_upper),
                        color='blue', alpha=0.3, label=f'{confidence_level}% Confidence Interval')

        ax.axvline(x=ci_lower, color='red', linestyle='--', label=f'Lower Bound = {ci_lower:.2f}')
        ax.axvline(x=ci_upper, color='red', linestyle='--', label=f'Upper Bound = {ci_upper:.2f}')
        ax.axvline(x=center, color='green', linestyle='-', label=f'Center = {center:.2f}')
        
        ax.set_title(f'Normal Distribution with {confidence_level}% Confidence Interval')
        ax.set_xlabel('Value')
        ax.set_ylabel('Probability Density')
        ax.legend()

        st.pyplot(fig)

    st.title("Margin of Error Calculator")

    st.latex(r"\text{MOE for Mean (known } \sigma\text{)} = Z \cdot \frac{\sigma}{\sqrt{n}}")
    st.latex(r"\text{MOE for Mean (unknown } \sigma\text{)} = t \cdot \frac{s}{\sqrt{n}}")
    st.latex(r"\text{MOE for Proportion} = Z \cdot \sqrt{\frac{p(1 - p)}{n}}")

    calculation_type = st.selectbox("Calculate MOE for:", ["Mean", "Proportion"])

    sample_size = st.number_input("Enter Sample Size (n)", min_value=1, value=30, step=1)
    confidence_level = st.slider("Select Confidence Level (%)", min_value=50, max_value=99, value=95, step=1)

    if calculation_type == "Mean":
        sigma_known = st.selectbox("Is Population Standard Deviation (σ) known?", ["Yes", "No"])
        
        if sigma_known == "Yes":
            z_score = get_z_score(confidence_level)
            std_dev = st.number_input("Enter Population Standard Deviation (σ)", value=1.0, step=0.1)
            sample_mean = st.number_input("Enter Sample Mean (x̄)", value=0.0, step=0.1)
            std_error = std_dev / math.sqrt(sample_size)

            moe = calculate_moe_mean_known(z_score, std_dev, sample_size)

            st.success(f"Standard Error: {std_error:.4f}")
            st.success(f"Margin of Error (MOE): {moe:.4f}")
            st.success(f"Confidence Interval: ({sample_mean - moe:.4f}, {sample_mean + moe:.4f})")
            
            plot_normal_distribution_with_moe(sample_mean, moe, std_error, confidence_level)

            st.write(f"With {confidence_level}% confidence, the population mean is estimated to be between {sample_mean - moe:.4f} and {sample_mean + moe:.4f}.")
        
        else:
            sample_std_dev = st.number_input("Enter Sample Standard Deviation (s)", value=1.0, step=0.1)
            sample_mean = st.number_input("Enter Sample Mean (x̄)", value=0.0, step=0.1)
            t_score = get_t_score(confidence_level, sample_size)
            std_error = sample_std_dev / math.sqrt(sample_size)
            
            moe = calculate_moe_mean_unknown(t_score, sample_std_dev, sample_size)

            st.success(f"Standard Error: {std_error:.4f}")
            st.success(f"Margin of Error (MOE): {moe:.4f}")
            st.success(f"Confidence Interval: ({sample_mean - moe:.4f}, {sample_mean + moe:.4f})")

            plot_normal_distribution_with_moe(sample_mean, moe, std_error, confidence_level)

            st.write(f"With {confidence_level}% confidence, the population mean is estimated to be between {sample_mean - moe:.4f} and {sample_mean + moe:.4f}.")

    elif calculation_type == "Proportion":
        z_score = get_z_score(confidence_level)
        proportion = st.number_input("Enter Sample Proportion (p)", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        std_error = math.sqrt((proportion * (1 - proportion)) / sample_size)
        
        moe = calculate_moe_proportion(z_score, proportion, sample_size)

        st.success(f"Standard Error: {std_error:.4f}")
        st.success(f"Margin of Error (MOE): {moe:.4f}")
        st.success(f"Confidence Interval: ({proportion - moe:.4f}, {proportion + moe:.4f})")

        plot_normal_distribution_with_moe(proportion, moe, std_error, confidence_level)

        st.write(f"With {confidence_level}% confidence, the population proportion is estimated to be between {proportion - moe:.4f} and {proportion + moe:.4f}.")

if __name__ == "__main__":
    main()
