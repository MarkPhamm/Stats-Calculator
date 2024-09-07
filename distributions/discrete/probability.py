import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def calculate_statistics(df):
    x = df['X']
    px = df['P(X)']
    
    # Expected value E(X)
    ex = np.sum(x * px)
    
    # Variance Var(X)
    varx = np.sum((x - ex)**2 * px)
    
    # Standard deviation Std(X)
    stdx = np.sqrt(varx)
    
    return ex, varx, stdx

def main():
    st.title("Custom Probability Distribution Calculator")

    # Initialize the session state
    if 'df' not in st.session_state:
        st.session_state.df = pd.DataFrame({"X": [0.0], "P(X)": [0.0]})

    # Function to update the DataFrame
    def update_df(edited_df):
        st.session_state.df = pd.DataFrame(edited_df)

    # Display an editable data editor for the user to input X and P(X) values
    st.subheader("Enter X and P(X) values")
    edited_df = st.data_editor(
        st.session_state.df,
        use_container_width=True,
        num_rows="dynamic",
        column_config={
            "X": st.column_config.NumberColumn("X", format="%.2f", required=True),
            "P(X)": st.column_config.NumberColumn("P(X)", format="%.2f", required=True)
        },
        key="data_editor",
        on_change=update_df,
        args=(st.session_state.df,)
    )

    # Ensure df is always a DataFrame
    st.session_state.df = pd.DataFrame(edited_df)

    # Button to validate and process the DataFrame
    if st.button("Submit"):
        df = st.session_state.df.copy()

        if df.empty:
            st.info("Please enter data in the table.")
        else:
            # Remove rows where both X and P(X) are 0
            df = df[(df['X'] != 0) | (df['P(X)'] != 0)]

            if df.empty:
                st.error("Please enter valid numerical values for X and P(X).")
            else:
                # Check that P(X) values sum up to 1 (with a tolerance for floating point precision)
                if not np.isclose(df["P(X)"].sum(), 1.0, atol=1e-8):
                    st.error("The sum of P(X) values must equal 1.")
                else:
                    # Display the table of X and P(X) values
                    st.subheader("X and P(X) Table")
                    st.dataframe(df, use_container_width=True)

                    # Calculate statistics
                    ex, varx, stdx = calculate_statistics(df)

                    # Display statistics
                    st.subheader("Statistics")
                    st.write(f"Expected Value E(X): {ex:.4f}")
                    st.write(f"Variance Var(X): {varx:.4f}")
                    st.write(f"Standard Deviation Std(X): {stdx:.4f}")

                    # Plot the custom probability distribution
                    fig, ax = plt.subplots()
                    ax.bar(df["X"], df["P(X)"], width=0.4, color='blue', alpha=0.7)

                    # Add labels and title
                    ax.set_title("Custom Probability Distribution")
                    ax.set_xlabel("X")
                    ax.set_ylabel("P(X)")

                    # Show the plot in Streamlit
                    st.pyplot(fig)

if __name__ == "__main__":
    main()