import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import seaborn as sns
import streamlit as st


def main():
    """
    Main function to render the One-Way ANOVA test interface.
    Allows users to input raw data for three groups, performs the F-test,
    and visualizes the distributions using boxplots.
    """
    st.markdown("### One-Way ANOVA Test")
    st.write(
        "Test whether there is a statistically significant difference between the means of three or more independent groups."
    )

    st.sidebar.markdown("---")
    st.sidebar.header("Data Input")

    st.info(
        "Please enter numerical values separated by commas (e.g., 10.5, 12.1, 14.2)."
    )

    # Text areas for raw data input
    group_a_str = st.text_area("Group A Data", "85, 87, 90, 88, 92, 95")
    group_b_str = st.text_area("Group B Data", "70, 75, 72, 74, 78, 73")
    group_c_str = st.text_area("Group C Data", "80, 82, 85, 81, 84, 83")

    # Significance level selection
    alpha = st.sidebar.slider("Significance Level (α)", 0.01, 0.10, 0.05)

    if st.button("Run ANOVA Test"):
        try:
            # Helper function to parse string input into list of floats
            def parse_input(data_str):
                if not data_str.strip():
                    return []
                return [float(x.strip()) for x in data_str.split(",") if x.strip()]

            # Parse the inputs
            data_a = parse_input(group_a_str)
            data_b = parse_input(group_b_str)
            data_c = parse_input(group_c_str)

            # Validate inputs
            if len(data_a) < 2 or len(data_b) < 2 or len(data_c) < 2:
                st.error("Error: Each group must have at least 2 data points.")
                return

            # 1. Perform One-Way ANOVA
            f_stat, p_value = stats.f_oneway(data_a, data_b, data_c)

            # 2. Display Statistics
            st.markdown("#### Results")
            col1, col2 = st.columns(2)
            col1.metric("F-Statistic", f"{f_stat:.4f}")
            col2.metric("P-Value", f"{p_value:.4f}")

            # Interpretation of results
            if p_value < alpha:
                st.error(
                    f"Conclusion: Reject Null Hypothesis (H₀). There is a significant difference between the group means (α={alpha})."
                )
            else:
                st.success(
                    "Conclusion: Fail to Reject Null Hypothesis (H₀). No significant difference found between group means."
                )

            # 3. Visualization (Boxplot)
            st.markdown("#### Distribution Visualization")

            # Combine data into a DataFrame for Seaborn plotting
            df_vis = pd.DataFrame(
                {
                    "Value": data_a + data_b + data_c,
                    "Group": ["Group A"] * len(data_a)
                    + ["Group B"] * len(data_b)
                    + ["Group C"] * len(data_c),
                }
            )

            fig, ax = plt.subplots(figsize=(8, 5))

            # Draw boxplot
            sns.boxplot(x="Group", y="Value", data=df_vis, ax=ax, palette="Set2")

            # Add swarmplot to show individual data points
            sns.swarmplot(x="Group", y="Value", data=df_vis, color=".25", ax=ax)

            ax.set_title("Distribution Comparison by Group")
            ax.set_ylabel("Value")
            st.pyplot(fig)

        except ValueError:
            st.error(
                "Input Error: Please ensure all inputs are valid numbers separated by commas."
            )
