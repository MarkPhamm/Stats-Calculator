import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import statsmodels.api as sm

def calculate_regression_metrics(X, y):
    # Add constant to predictor variables (for intercept term in OLS model)
    X = sm.add_constant(X)
    
    # Fit OLS model
    model = sm.OLS(y, X)
    results = model.fit()

    # Extract R^2, p-values, and coefficients
    r_squared = results.rsquared
    p_values = results.pvalues
    coefficients = results.params

    return results, r_squared, p_values, coefficients

def main():
    st.title("Linear Regression Analysis from File")

    st.subheader("Step 1: Upload your file (.xlsx or .csv)")

    # File upload option
    uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx"])

    if uploaded_file is not None:
        # Load the file into a DataFrame
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        # Fill missing values (NaN) with the median of each column
        df = df.fillna(df.median(numeric_only=True))

        # Show first 5 rows of the dataset
        st.write("First 5 rows of the dataset (NaN values filled with column medians):")
        st.dataframe(df.head())

        # Step 2: Let the user choose the target column
        st.subheader("Step 2: Select the target column for regression")
        target_column = st.selectbox("Choose the target column (dependent variable):", df.columns)

        # Step 3: Select predictor columns (all other numeric columns except the target)
        predictor_columns = st.multiselect(
            "Choose predictor columns (independent variables):",
            [col for col in df.columns if col != target_column and np.issubdtype(df[col].dtype, np.number)]
        )

        if len(predictor_columns) > 0 and target_column is not None:
            # Split into X (predictors) and y (target)
            X = df[predictor_columns]
            y = df[target_column]

            # Step 4: Perform linear regression
            st.subheader("Step 3: Run Linear Regression")
            if st.button("Run Regression"):
                # Split into training and test sets
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

                # Fit the linear regression model
                model = LinearRegression()
                model.fit(X_train, y_train)

                # Predictions
                y_pred = model.predict(X_test)

                # Calculate metrics
                rmse = np.sqrt(mean_squared_error(y_test, y_pred))
                r2 = r2_score(y_test, y_pred)

                # OLS metrics from statsmodels
                ols_results, ols_r_squared, p_values, coefficients = calculate_regression_metrics(X_train, y_train)

                # Display metrics
                st.write(f"### Regression Metrics:")
                st.write(f"**R² (Training Set):** {r2:.4f}")
                st.write(f"**RMSE (Test Set):** {rmse:.4f}")

                # OLS summary
                st.write(f"### OLS Model Summary:")
                st.write(ols_results.summary())

                # Display p-values and coefficients in two columns
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write(f"**P-values:**")
                    st.dataframe(p_values, width=300)  # Adjust width as needed
                
                with col2:
                    st.write(f"**Coefficients:**")
                    st.dataframe(coefficients, width=300)  # Adjust width as needed
                    
if __name__ == "__main__":
    main()
