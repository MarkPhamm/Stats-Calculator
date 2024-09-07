import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def plot_probability_of_heads(ax, probabilities, title):
    ax.plot(probabilities, color='blue')
    ax.axhline(y=0.5, color='red', linestyle='--', label='True Probability (0.5)')
    ax.set_title(title)
    ax.set_xlabel('Number of Tosses')
    ax.set_ylabel('Probability of Heads')
    ax.legend()

def generate_coin_tosses(size):
    # Generate a sequence of coin tosses (0 for tails, 1 for heads)
    return np.random.binomial(n=1, p=0.5, size=size)

def calculate_running_probabilities(data):
    # Calculate the running probability of heads
    cumulative_sums = np.cumsum(data)
    running_probabilities = cumulative_sums / (np.arange(1, len(data) + 1))
    return running_probabilities

def main():
    st.title("Law of Large Numbers Demonstration")

    st.markdown('''
    <style>
    .katex-html {
        text-align: left;
    }
    </style>''',
    unsafe_allow_html=True
    )

    # Display the formula for the Law of Large Numbers using st.latex
    st.latex(r"""
        \text{The Law of Large Numbers (LLN) states that as the number of trials } n \text{ increases,} \\
        \text{the sample mean } \bar{X} \text{ of a random variable will converge to the population mean } \mu. \\
        \text{In other words, for a large number of trials, the average of the results will be close to the} \\
        \text{expected value (population mean).}
    """)

    st.latex(r"""
    \bar{X} \approx \mu \text{ as } n \to \infty
    """)

    st.latex(r"""
    \begin{align*}
    \bar{X} & \text{ is the sample mean} \\
    \mu & \text{ is the population mean} \\
    n & \text{ is the number of trials}
    \end{align*}
    """)

    # Number of coin tosses
    num_tosses = st.slider("Number of Coin Tosses", 10, 10000, 1000)

    # Generate the coin toss data
    data = generate_coin_tosses(num_tosses)

    # Calculate running probabilities
    running_probabilities = calculate_running_probabilities(data)

    # Plot the running probability of heads
    fig, ax = plt.subplots(figsize=(10, 6))
    plot_probability_of_heads(ax, running_probabilities, 'Convergence of Head Probability to 0.5')
    st.pyplot(fig)

if __name__ == "__main__":
    main()
