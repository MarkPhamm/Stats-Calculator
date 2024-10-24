import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

def chi_square_goodness_of_fit(observed, expected):
    """Perform Chi-Square Goodness of Fit test."""
    chi2_stat, p_value = stats.chisquare(f_obs=observed, f_exp=expected)
    return chi2_stat, p_value

def chi_square_test_of_independence(contingency_table):
    """Perform Chi-Square Test of Independence."""
    chi2_stat, p_value, dof, expected = stats.chi2_contingency(contingency_table)
    return chi2_stat, p_value, dof, expected

def plot_chi_square_distribution(chi2_stat, dof=None):
    """Plot Chi-Square distribution with test statistic and critical value."""
    x = np.linspace(0, max(chi2_stat + 10, 20), 100)
    plt.figure(figsize=(10, 6))

    if dof:
        plt.plot(x, stats.chi2.pdf(x, df=dof), 'r-', label=f'Chi-Square Distribution (df={dof})')
        critical_value = stats.chi2.ppf(0.95, df=dof)
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

def display_results(chi2_stat, p_value, dof, expected=None):
    if expected is not None:
        st.write("Expected Frequencies:")
        st.dataframe(expected, use_container_width=True)
    st.success(f"Chi-Square Statistic: {chi2_stat:.4f}")
    st.success(f"P-Value: {p_value:.4f}")
    st.success(f"Degrees of Freedom: {dof}")

    critical_value = stats.chi2.ppf(0.95, df=dof)
    st.success(f"**Critical Value (95% confidence):** {critical_value:.4f}")

    if chi2_stat > critical_value:
        st.success("**Conclusion:** Reject the null hypothesis. There is significant evidence of a difference or dependence.")
    else:
        st.error("**Conclusion:** Fail to reject the null hypothesis. There is not enough evidence to conclude a difference or dependence.")

    plot_chi_square_distribution(chi2_stat, dof)

def main():
    st.title("Chi-Square Tests")

    test_type = st.sidebar.radio("Choose Chi-Square Test", ("Goodness of Fit", "Test of Independence"))

    if test_type == "Goodness of Fit":
        goodness_of_fit_test()
    elif test_type == "Test of Independence":
        independence_test()

def goodness_of_fit_test():
    st.subheader("Chi-Square Goodness of Fit Test")

    st.latex(r"\text{H₀: The observed distribution fits the expected distribution}")
    st.latex(r"\text{H₁: The observed distribution does not fit the expected distribution}")
    st.latex(r"\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}")

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
            elif not np.isclose(np.sum(observed), np.sum(expected), rtol=1e-8):
                st.error("The sum of observed frequencies must match the sum of expected frequencies.")
            else:
                chi2_stat, p_value = chi_square_goodness_of_fit(observed, expected)
                display_results(chi2_stat, p_value, len(observed) - 1)

def independence_test():
    st.subheader("Chi-Square Test of Independence")

    st.latex(r"\text{H₀: The two variables are independent}")
    st.latex(r"\text{H₁: The two variables are not independent}")
    st.latex(r"\chi^2 = \sum \frac{(O_{ij} - E_{ij})^2}{E_{ij}}")

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
            display_results(chi2_stat, p_value, dof, expected)

if __name__ == "__main__":
    main()
