import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

def chi_square_goodness_of_fit(observed, expected):
    chi2_stat, p_value = stats.chisquare(f_obs=observed, f_exp=expected)
    return chi2_stat, p_value

def chi_square_test_of_independence(contingency_table):
    chi2_stat, p_value, dof, expected = stats.chi2_contingency(contingency_table)
    return chi2_stat, p_value, dof, expected

def plot_chi_square_distribution(chi2_stat, dof=None):
    x = np.linspace(0, chi2_stat + 10, 100)
    plt.figure(figsize=(10, 6))

    # Plot the Chi-Square distribution
    if dof:
        plt.plot(x, stats.chi2.pdf(x, df=dof), 'r-', label=f'Chi-Square Distribution (df={dof})')
        critical_value = stats.chi2.ppf(0.95, df=dof)  # Critical value for 95% confidence
        plt.axvline(x=critical_value, color='g', linestyle='--', label=f'Critical Value (df={dof})')
    else:
        plt.axvline(x=chi2_stat, color='r', linestyle='--', label=f'Chi-Square Statistic: {chi2_stat:.4f}')
    
    plt.axvline(x=chi2_stat, color='b', linestyle='--', label=f'Test Statistic: {chi2_stat:.4f}')
    plt.title('Chi-Square Distribution')
    plt.xlabel('Chi-Square Value')
    plt.ylabel('Probability Density')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt.gcf())
    plt.close()

def main():
    st.title("Chi-Square Tests")

    # Radio buttons for test selection
    test_type = st.sidebar.radio("Choose Chi-Square Test", ("Goodness of Fit", "Test of Independence"))

    if test_type == "Goodness of Fit":
        st.subheader("Chi-Square Goodness of Fit Test")

        st.latex(r"""
        \text{Null Hypothesis (H₀)}: \text{The observed distribution fits the expected distribution}
        """)
        st.latex(r"""
        \text{Alternative Hypothesis (H₁)}: \text{The observed distribution does not fit the expected distribution}
        """)
        st.latex(r"""
        \text{Test Statistic (Chi-Square)}: \chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}
        """)

        # Input observed and expected frequencies
        st.write("Enter the observed and expected frequencies for the Goodness of Fit test.")
        num_categories = st.number_input("Number of categories", min_value=1, value=3, step=1)
        
        observed_df = pd.DataFrame({"Observed": [0.0] * num_categories})
        expected_df = pd.DataFrame({"Expected": [0.0] * num_categories})

        observed_values = st.data_editor(observed_df, use_container_width=True, key="observed_data")
        expected_values = st.data_editor(expected_df, use_container_width=True, key="expected_data")

        if st.button("Run Goodness of Fit Test"):
            if observed_values.empty or expected_values.empty:
                st.error("Please enter values for both observed and expected frequencies.")
            else:
                observed = observed_values['Observed'].values
                expected = expected_values['Expected'].values
                
                if len(observed) != len(expected):
                    st.error("Length of observed and expected frequencies must be the same.")
                else:
                    chi2_stat, p_value = chi_square_goodness_of_fit(observed, expected)
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write(f"Chi-Square Statistic: {chi2_stat:.4f}")
                    with col2:
                        st.write(f"P-Value: {p_value:.4f}")

                    # Null and Alternative Hypotheses
                    st.write("### Hypotheses:")
                    st.write("**Null Hypothesis (H0):** The observed frequencies match the expected frequencies.")
                    st.write("**Alternative Hypothesis (H1):** The observed frequencies do not match the expected frequencies.")

                    # Critical value for a 95% confidence level
                    critical_value = stats.chi2.ppf(0.95, df=len(observed)-1)
                    st.write(f"**Critical Value (95% confidence):** {critical_value:.4f}")

                    # Conclusion
                    if chi2_stat > critical_value:
                        st.write("**Conclusion:** Reject the null hypothesis. There is significant evidence that the observed frequencies differ from the expected frequencies.")
                    else:
                        st.write("**Conclusion:** Fail to reject the null hypothesis. There is not enough evidence to conclude that the observed frequencies differ from the expected frequencies.")

                    # Plot distribution
                    plot_chi_square_distribution(chi2_stat)

    elif test_type == "Test of Independence":
        st.subheader("Chi-Square Test of Independence")

        st.latex(r"""
        \text{Null Hypothesis (H₀)}: \text{The two variables are independent}
        """)
        st.latex(r"""
        \text{Alternative Hypothesis (H₁)}: \text{The two variables are not independent}
        """)
        st.latex(r"""
        \text{Test Statistic (Chi-Square)}: \chi^2 = \sum \frac{(O_{ij} - E_{ij})^2}{E_{ij}}
        """)

        # Input contingency table
        st.write("Enter the contingency table for the Test of Independence.")
        num_rows = st.number_input("Number of rows", min_value=2, value=3, step=1)
        num_cols = st.number_input("Number of columns", min_value=2, value=3, step=1)

        contingency_df = pd.DataFrame(np.zeros((num_rows, num_cols)), columns=[f"Col{i+1}" for i in range(num_cols)])
        contingency_table = st.data_editor(contingency_df, use_container_width=True, key="contingency_table")

        if st.button("Run Test of Independence"):
            if contingency_table.empty:
                st.error("Please enter values for the contingency table.")
            else:
                contingency_table = contingency_table.values
                chi2_stat, p_value, dof, expected = chi_square_test_of_independence(contingency_table)
                col1, col2 = st.columns(2)

                with col1:
                    st.write(f"Chi-Square Statistic: {chi2_stat:.4f}")
                    st.write(f"P-Value: {p_value:.4f}")

                with col2:
                    st.write(f"Degrees of Freedom: {dof}")
                    st.write("Expected Frequencies:")
                st.dataframe(expected, use_container_width=True)

                # Null and Alternative Hypotheses
                st.write("### Hypotheses:")
                st.write("**Null Hypothesis (H0):** The variables are independent.")
                st.write("**Alternative Hypothesis (H1):** The variables are not independent.")

                # Critical value for a 95% confidence level
                critical_value = stats.chi2.ppf(0.95, df=dof)
                st.write(f"**Critical Value (95% confidence):** {critical_value:.4f}")

                # Conclusion
                if chi2_stat > critical_value:
                    st.write("**Conclusion:** Reject the null hypothesis. There is significant evidence that the variables are not independent.")
                else:
                    st.write("**Conclusion:** Fail to reject the null hypothesis. There is not enough evidence to conclude that the variables are not independent.")

                # Plot distribution
                plot_chi_square_distribution(chi2_stat, dof)

if __name__ == "__main__":
    main()
