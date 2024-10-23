import streamlit as st
import math
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

def main():
    def calculate_n_mean_known(z_score, std_dev, moe):
        return (z_score * std_dev / moe) ** 2

    def calculate_n_mean_unknown(t_score, sample_std_dev, moe):
        return (t_score * sample_std_dev / moe) ** 2

    def calculate_n_proportion(z_score, proportion, moe):
        return (z_score ** 2 * proportion * (1 - proportion)) / (moe ** 2)

    def get_z_score(confidence_level):
        return stats.norm.ppf((1 + confidence_level / 100) / 2)

    def get_t_score(confidence_level, sample_size):
        return stats.t.ppf((1 + confidence_level / 100) / 2, df=sample_size - 1)

    st.title("Margin of Error Inverse Calculator")

    st.latex(r"\text{Sample Size for Mean (known } \sigma\text{)}: n = \left(\frac{Z \cdot \sigma}{MOE}\right)^2")
    st.latex(r"\text{Sample Size for Mean (unknown } \sigma\text{)}: n = \left(\frac{t \cdot s}{MOE}\right)^2")
    st.latex(r"\text{Sample Size for Proportion}: n = \frac{Z^2 \cdot p(1 - p)}{MOE^2}")

    calculation_type = st.selectbox("Calculate Sample Size for:", ["Mean", "Proportion"])

    confidence_level = st.slider("Select Confidence Level (%)", min_value=50, max_value=99, value=95, step=1)
    moe = st.number_input("Enter Margin of Error (MOE)", value=0.05, step=0.01)

    if calculation_type == "Mean":
        sigma_known = st.selectbox("Is Population Standard Deviation (σ) known?", ["Yes", "No"])
        
        if sigma_known == "Yes":
            z_score = get_z_score(confidence_level)
            std_dev = st.number_input("Enter Population Standard Deviation (σ)", value=1.0, step=0.1)

            n = calculate_n_mean_known(z_score, std_dev, moe)
            st.success(f"Required Sample Size (n): {n:.2f}")
        
        else:
            sample_std_dev = st.number_input("Enter Sample Standard Deviation (s)", value=1.0, step=0.1)

            t_score = get_t_score(confidence_level, 30)  # Assuming a default sample size for t-score
            n = calculate_n_mean_unknown(t_score, sample_std_dev, moe)

            st.success(f"Required Sample Size (n): {n:.2f}")

    elif calculation_type == "Proportion":
        z_score = get_z_score(confidence_level)
        proportion = st.number_input("Enter Sample Proportion (p)", min_value=0.0, max_value=1.0, value=0.5, step=0.01)

        n = calculate_n_proportion(z_score, proportion, moe)

        st.success(f"Required Sample Size (n): {n:.2f}")

if __name__ == "__main__":
    main()
