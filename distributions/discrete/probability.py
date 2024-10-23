import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def calculate_statistics(df):
    """Calculate expected value, variance, and standard deviation."""
    x = df['X']
    px = df['P(X)']
    
    expected_value = np.sum(x * px)
    variance = np.sum((x - expected_value)**2 * px)
    std_deviation = np.sqrt(variance)
    
    return expected_value, variance, std_deviation

def plot_distribution(df):
    """Plot the custom probability distribution."""
    fig, ax = plt.subplots()
    ax.bar(df["X"], df["P(X)"], width=0.4, color='blue', alpha=0.7)
    ax.set_title("Custom Probability Distribution")
    ax.set_xlabel("X")
    ax.set_ylabel("P(X)")
    return fig

def main():
    st.title("Probability Distribution Calculator")

    st.latex(r"E(X) = \sum_{i=1}^{n} X_i \cdot P(X_i)")
    st.latex(r"\text{Var}(X) = \sum_{i=1}^{n} (X_i - E(X))^2 \cdot P(X_i)")

    if 'df' not in st.session_state:
        st.session_state.df = pd.DataFrame({"X": [0.0], "P(X)": [0.0]})

    st.subheader("Enter X and P(X) values")
    
    edited_df = st.data_editor(
        st.session_state.df,
        use_container_width=True,
        num_rows="dynamic",
        column_config={
            "X": st.column_config.NumberColumn("X", format="%.2f", required=True),
            "P(X)": st.column_config.NumberColumn("P(X)", format="%.2f", required=True)
        },
        key="data_editor"
    )

    if st.button("Submit"):
        df = pd.DataFrame(edited_df)

        # Remove rows where both X and P(X) are 0
        df = df[(df['X'] != 0) | (df['P(X)'] != 0)]  

        if df.empty:
            st.error("Please enter valid numerical values for X and P(X).")
        elif not np.isclose(df["P(X)"].sum(), 1.0, atol=1e-8):
            st.error("The sum of P(X) values must equal 1.")
        else:
            st.subheader("X and P(X) Table")
            st.dataframe(df, use_container_width=True)

            expected_value, variance, std_deviation = calculate_statistics(df)

            st.subheader("Statistics")
            st.write(f"Expected Value E(X): {expected_value:.4f}")
            st.write(f"Variance Var(X): {variance:.4f}")
            st.write(f"Standard Deviation Std(X): {std_deviation:.4f}")

            st.pyplot(plot_distribution(df))

if __name__ == "__main__":
    main()
