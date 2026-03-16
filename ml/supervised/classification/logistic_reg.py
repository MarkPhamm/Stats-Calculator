import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def main():
    st.title("Logistic Regression (Binary Classification)")

    tab1, tab2 = st.tabs(["📚 Theory & Visualization", "🛠️ Practical Analysis"])

    # ==========================================
    # TAB 1: Theory (Sigmoid Visualization)
    # ==========================================
    with tab1:
        st.header("Understanding Logistic Regression")
        st.markdown(r"""
        Logistic Regression predicts probabilities (values between 0 and 1) using the **Sigmoid Function**.
        It is typically used for binary classification tasks (e.g., Yes/No, Spam/Not Spam).
        
        **Formula:**
        $$ P(y=1) = \frac{1}{1 + e^{-(mx + b)}} $$
        """)

        # Interactive Controls
        col_viz, col_desc = st.columns([2, 1])
        
        with col_desc:
            st.subheader("Parameter Tuning")
            m_val = st.slider("Slope (m) - Steepness", -10.0, 10.0, 1.0, help="Controls how quickly the probability changes.")
            b_val = st.slider("Intercept (b) - Shift", -10.0, 10.0, 0.0, help="Shifts the curve left or right.")
            st.info("Observe how 'm' affects the sharpness of the decision boundary.")

        with col_viz:
            # Generate Sigmoid Curve
            x_vals = np.linspace(-10, 10, 100)
            y_vals = 1 / (1 + np.exp(-(m_val * x_vals + b_val)))
            
            fig, ax = plt.subplots()
            ax.plot(x_vals, y_vals, color='green', linewidth=3, label='Sigmoid Curve')
            
            # Draw Threshold Line
            ax.axhline(0.5, color='red', linestyle='--', alpha=0.5, label='Decision Threshold (0.5)')
            
            # Draw Decision Boundary (Vertical Line)
            boundary_x = -b_val/m_val if m_val != 0 else 0
            if -10 <= boundary_x <= 10:
                ax.axvline(boundary_x, color='gray', linestyle=':', alpha=0.5, label=f'Boundary (x={boundary_x:.2f})')
            
            ax.set_title("Sigmoid Activation Function")
            ax.set_ylabel("Probability P(y=1)")
            ax.set_xlabel("Input Value (x)")
            ax.legend()
            ax.grid(True, alpha=0.3)
            st.pyplot(fig)

    # ==========================================
    # TAB 2: Practical Analysis (Real Data)
    # ==========================================
    with tab2:
        st.header("Train a Classification Model")
        
        uploaded_file = st.file_uploader("Upload CSV or Excel File", type=["csv", "xlsx"], key="logreg_upload")

        if uploaded_file is not None:
            # Load Data
            if uploaded_file.name.endswith(".csv"):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
            
            # Preprocessing
            df = df.fillna(df.median(numeric_only=True))
            st.write("Data Preview:", df.head())

            # Target Selection
            target_col = st.selectbox("Select Target Variable (Label 0/1)", df.columns, key="log_y")
            
            # Validate Target (Should be roughly binary for this demo)
            if df[target_col].nunique() > 2:
                st.warning("⚠️ The selected target has more than 2 unique classes. The model will run in Multinomial mode.")

            # Feature Selection (Numeric Only)
            numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
            if target_col in numeric_cols:
                numeric_cols.remove(target_col)
            
            feature_cols = st.multiselect("Select Feature Variables (X)", numeric_cols, key="log_x")

            if feature_cols and st.button("Train Logistic Model"):
                X = df[feature_cols]
                y = df[target_col]

                # Train/Test Split
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
                
                # Standard Scaling (Crucial for Logistic Regression performance)
                scaler = StandardScaler()
                X_train_s = scaler.fit_transform(X_train)
                X_test_s = scaler.transform(X_test)

                # Model Training
                model = LogisticRegression(max_iter=1000)
                model.fit(X_train_s, y_train)
                y_pred = model.predict(X_test_s)

                # Metrics
                acc = accuracy_score(y_test, y_pred)
                st.success(f"Model Accuracy: {acc:.2%}")

                col_cm, col_coef = st.columns(2)
                
                # Visual 1: Confusion Matrix
                with col_cm:
                    st.subheader("Confusion Matrix")
                    cm = confusion_matrix(y_test, y_pred)
                    fig_cm, ax_cm = plt.subplots(figsize=(6, 5))
                    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax_cm)
                    ax_cm.set_ylabel('True Label')
                    ax_cm.set_xlabel('Predicted Label')
                    st.pyplot(fig_cm)

                # Visual 2: Feature Importance (Coefficients)
                with col_coef:
                    st.subheader("Feature Importance")
                    st.caption("Positive weights increase probability of class 1.")
                    coef_df = pd.DataFrame({
                        'Feature': feature_cols,
                        'Weight': model.coef_[0]
                    }).sort_values(by='Weight', ascending=False)
                    st.dataframe(coef_df, hide_index=True, use_container_width=True)
                
                # Detailed Report
                st.subheader("Classification Report")
                report = classification_report(y_test, y_pred, output_dict=True)
                st.dataframe(pd.DataFrame(report).transpose())