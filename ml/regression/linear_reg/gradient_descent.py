import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Gradient Descent Algorithm for Linear Regression
def gradient_descent(X, y, learning_rate=0.01, iterations=100):
    m = 0  # Initial slope
    b = 0  # Initial intercept
    n = len(X)
    history = []
    cost_history = []

    for _ in range(iterations):
        y_pred = m * X + b
        # Calculate gradients
        dm = (-2/n) * np.sum(X * (y - y_pred))
        db = (-2/n) * np.sum(y - y_pred)
        # Update m and b
        m -= learning_rate * dm
        b -= learning_rate * db
        # Calculate cost (mean squared error)
        cost = np.mean((y - y_pred) ** 2)
        # Save history of m, b, and cost
        history.append((m, b))
        cost_history.append(cost)
    
    return history, cost_history

def main():
    st.title("Gradient Descent Visualization")

    # Add LaTeX formulas to explain the process of gradient descent
    st.subheader("Gradient Descent Formulas")

    # Linear regression model
    st.latex(r"y = mx + b")

    # Mean Squared Error (Cost function)
    st.latex(r"J(m, b) = \frac{1}{n} \sum_{i=1}^{n} \left( y_i - (mx_i + b) \right)^2")

    # Gradients with respect to m and b
    st.latex(r"\frac{\partial J}{\partial m} = -\frac{2}{n} \sum_{i=1}^{n} x_i (y_i - (mx_i + b))")
    st.latex(r"\frac{\partial J}{\partial b} = -\frac{2}{n} \sum_{i=1}^{n} (y_i - (mx_i + b))")

    # Gradient descent update rule
    st.latex(r"m := m - \alpha \frac{\partial J}{\partial m}")
    st.latex(r"b := b - \alpha \frac{\partial J}{\partial b}")

    # Randomly generate 100 (x, y) points with some noise
    np.random.seed(42)
    X = 2 * np.random.rand(100)
    y = 4 + 3 * X + np.random.randn(100)

    # Plot the random points
    st.subheader("Randomly Generated Data Points")

    # Initial figure and axis
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Scatter plot of the data points
    ax1.scatter(X, y, color='blue', label="Data points")
    line, = ax1.plot(X, np.zeros_like(X), color='red', label="Fitted line")  # Initial empty line
    ax1.set_title("Linear Regression with Gradient Descent")
    ax1.set_xlabel("X")
    ax1.set_ylabel("Y")
    ax1.legend()

    # Plot for the loss function
    ax2.set_title("Loss Function over Iterations")
    ax2.set_xlabel("Iterations")
    ax2.set_ylabel("Cost")
    cost_plot, = ax2.plot([], [], color='green')

    # Initialize the plot in Streamlit (create a single placeholder for the plot)
    plot_placeholder = st.pyplot(fig)

    # User inputs for gradient descent
    learning_rate = st.slider("Select Learning Rate", min_value=0.001, max_value=0.1, value=0.01, step=0.001)
    iterations = st.slider("Select Number of Iterations", min_value=1, max_value=100, value=50, step=1)

    if st.button("Run Gradient Descent"):
        # Run gradient descent
        history, cost_history = gradient_descent(X, y, learning_rate, iterations)

        # Loop through the gradient descent history to update the line and loss function
        for i in range(len(history)):
            # Update the line with current m and b
            m, b = history[i]
            line.set_ydata(m * X + b)

            # Update the loss plot
            cost_plot.set_data(range(i), cost_history[:i])

            # Set axis limits dynamically
            ax2.set_xlim(0, len(cost_history))
            ax2.set_ylim(0, max(cost_history))

            # Redraw the plot (single plot update)
            plot_placeholder.pyplot(fig)

        # Display the final loss
        final_loss = cost_history[-1]
        st.success(f"Final Loss: {final_loss:.4f}")

    st.markdown("""
    - **y = mx + b**: Linear regression model.
    - **J(m, b)**: Cost function, the mean squared error between predicted and actual values.
    - **∂J/∂m** and **∂J/∂b**: Gradients of the cost function with respect to the slope (m) and intercept (b).
    - **Gradient Descent Update**: Update rules for slope (m) and intercept (b), where α is the learning rate.
    """)

if __name__ == "__main__":
    main()
