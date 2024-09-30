import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def plot_normal_distribution(mean, std_dev, percentages):
    x = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 1000)
    y = norm.pdf(x, mean, std_dev)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, y, 'b-', linewidth=2, label='Normal Distribution')
    
    colors = ['#FFA07A', '#98FB98', '#87CEFA']
    for i, (start, end, percentage) in enumerate(percentages):
        ax.fill_between(x, y, where=(x >= start) & (x <= end), color=colors[i], alpha=0.3, 
                        label=f'{percentage}% within {i+1} std dev')
    
    ax.set_title('Normal Distribution and Empirical Rule')
    ax.set_xlabel('Value')
    ax.set_ylabel('Probability Density')
    ax.legend()
    
    st.pyplot(fig)

def main():
    st.title("Empirical Rule (68-95-99.7 Rule)")
    
    st.write("""
    The Empirical Rule, also known as the 68-95-99.7 rule, is a statistical principle that describes 
    the distribution of data in a normal distribution (bell curve).
    """)
    
    st.subheader("Key Points of the Empirical Rule:")
    st.write("""
    1. Approximately 68% of the data falls within 1 standard deviation of the mean.
    2. Approximately 95% of the data falls within 2 standard deviations of the mean.
    3. Approximately 99.7% of the data falls within 3 standard deviations of the mean.
    """)
    
    st.subheader("Interactive Visualization")
    
    mean = st.slider("Select the mean", -10.0, 10.0, 0.0, 0.1)
    std_dev = st.slider("Select the standard deviation", 0.1, 5.0, 1.0, 0.1)
    
    percentages = [
        (mean - std_dev, mean + std_dev, 68),
        (mean - 2*std_dev, mean + 2*std_dev, 95),
        (mean - 3*std_dev, mean + 3*std_dev, 99.7)
    ]
    
    plot_normal_distribution(mean, std_dev, percentages)
    
    st.subheader("Applications of the Empirical Rule")
    st.write("""
    The Empirical Rule is useful in various fields:
    
    1. Quality Control: Identifying products that fall outside expected ranges.
    2. Finance: Assessing risk and volatility in stock prices.
    3. Education: Evaluating test scores and student performance.
    4. Weather Forecasting: Predicting temperature ranges.
    5. Manufacturing: Setting tolerance limits for product specifications.
    """)
    
    st.subheader("Limitations")
    st.write("""
    It's important to note that the Empirical Rule assumes a normal distribution. 
    Not all data sets follow a normal distribution, so always check the shape of your data 
    before applying this rule.
    """)

if __name__ == "__main__":
    main()
