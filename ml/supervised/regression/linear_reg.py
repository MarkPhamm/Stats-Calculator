import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# ==========================================
# HELPER: Gradient Descent Function (For Tab 1)
# ==========================================
def run_gradient_descent(X, y, learning_rate=0.01, iterations=100):
    """
    Performs Gradient Descent to optimize the linear regression parameters m (slope) and b (intercept).
    """
    m = 0  # Initial slope
    b = 0  # Initial intercept
    n = len(X)
    history = []
    cost_history = []

    for _ in range(iterations):
        y_pred = m * X + b
        
        # Calculate gradients (Partial derivatives)
        dm = (-2/n) * np.sum(X * (y - y_pred))
        db = (-2/n) * np.sum(y - y_pred)
        
        # Update parameters
        m -= learning_rate * dm
        b -= learning_rate * db
        
        # Calculate Cost (Mean Squared Error)
        cost = np.mean((y - y_pred) ** 2)
        
        # Store state for visualization
        history.append((m, b))
        cost_history.append(cost)
    
    return history, cost_history

# ==========================================
# MAIN APP MODULE
# ==========================================
def main():
    st.title("Linear Regression Analysis")

    # Create two tabs: Educational (Theory) and Functional (Practice)
    tab1, tab2 = st.tabs(["📚 Theory (Gradient Descent)", "🛠️ Practical Analysis"])

    # -------------------------------------------------------------------------
    # TAB 1: Theory & Visualization (Gradient Descent Animation)
    # -------------------------------------------------------------------------
    with tab1:
        st.header("How Linear Regression 'Learns'")
        st.markdown(r"""
        Linear Regression models ($y = mx + b$) find the best-fitting line by minimizing the error between predictions and actual values. 
        This optimization process is often performed using an algorithm called **Gradient Descent**.
        """)

        col_input, col_plot = st.columns([1, 2])

        with col_input:
            st.subheader("Simulation Configuration")
            # Synthetic Data Parameters
            n_points = st.slider("Number of Data Points", 10, 100, 30)
            noise = st.slider("Noise Level", 0.0, 5.0, 1.0)
            
            st.markdown("---")
            st.write("**Hyperparameters:**")
            lr = st.slider("Learning Rate", 0.001, 0.1, 0.01, format="%.3f")
            iters = st.slider("Iterations (Steps)", 10, 100, 50)
            
            run_btn = st.button("Run Simulation")

        with col_plot:
            # Generate Synthetic Data for Visualization
            np.random.seed(42)
            X_vis = 2 * np.random.rand(n_points)
            y_vis = 4 + 3 * X_vis + np.random.randn(n_points) * noise

            # Placeholders for dynamic plotting
            plot_placeholder = st.empty()

            if run_btn:
                history, cost_history = run_gradient_descent(X_vis, y_vis, lr, iters)
                
                # Animation Loop
                for i in range(len(history)):
                    m_curr, b_curr = history[i]
                    
                    # Create plot figure
                    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
                    
                    # Subplot 1: Regression Line fitting the data
                    ax1.scatter(X_vis, y_vis, color='blue', alpha=0.6, label='Data Points')
                    ax1.plot(X_vis, m_curr * X_vis + b_curr, color='red', linewidth=2, label='Regression Line')
                    ax1.set_title(f"Step {i+1}: y = {m_curr:.2f}x + {b_curr:.2f}")
                    ax1.set_ylim(0, max(y_vis) + 2)
                    ax1.legend()
                    
                    # Subplot 2: Cost Function (Loss) decreasing
                    ax2.plot(range(i+1), cost_history[:i+1], color='orange', linewidth=2)
                    ax2.set_title(f"Cost (MSE): {cost_history[i]:.4f}")
                    ax2.set_xlabel("Iteration")
                    ax2.set_ylabel("Loss")
                    
                    # Render plot
                    plot_placeholder.pyplot(fig)
                    plt.close(fig) # Clear memory
                
                st.success("Gradient Descent Optimization Completed!")
            else:
                # Show initial state before running
                fig, ax = plt.subplots(figsize=(6, 4))
                ax.scatter(X_vis, y_vis, label='Data Points')
                ax.set_title("Original Data")
                ax.legend()
                plot_placeholder.pyplot(fig)

    # -------------------------------------------------------------------------
    # TAB 2: Practical Analysis (Real File Upload)
    # -------------------------------------------------------------------------
    with tab2:
        st.header("Linear Regression on Real Data")
        
        uploaded_file = st.file_uploader("Upload CSV or Excel File", type=["csv", "xlsx"])

        if uploaded_file is not None:
            # Data Loading
            if uploaded_file.name.endswith(".csv"):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
            
            # Simple Preprocessing: Fill missing numeric values with median
            df = df.fillna(df.median(numeric_only=True))
            st.write("Data Preview:", df.head())

            # Feature Selection
            target = st.selectbox("Select Target Variable (Y)", df.columns)
            
            # Filter valid numeric features excluding the target
            numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
            if target in numeric_cols:
                numeric_cols.remove(target)
            
            features = st.multiselect("Select Feature Variables (X)", numeric_cols)

            if features and st.button("Train Linear Model"):
                X = df[features]
                y = df[target]

                # Train/Test Split
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

                # Train Model (Scikit-Learn)
                model = LinearRegression()
                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)

                # Performance Metrics
                rmse = np.sqrt(mean_squared_error(y_test, y_pred))
                r2 = r2_score(y_test, y_pred)

                col1, col2 = st.columns(2)
                col1.metric("R² Score (Goodness of Fit)", f"{r2:.4f}")
                col2.metric("RMSE (Root Mean Squared Error)", f"{rmse:.4f}")

                # Visualization: Actual vs Predicted
                fig, ax = plt.subplots()
                ax.scatter(y_test, y_pred, alpha=0.7)
                ax.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2, label='Perfect Prediction')
                ax.set_xlabel("Actual Values")
                ax.set_ylabel("Predicted Values")
                ax.set_title("Actual vs Predicted")
                ax.legend()
                st.pyplot(fig)
                
                # Detailed Statistical Summary (Statsmodels)
                st.subheader("Statistical Summary (OLS)")
                X_const = sm.add_constant(X_train) # Add intercept term
                ols = sm.OLS(y_train, X_const).fit()
                st.write(ols.summary())