import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def plot_probability_convergence(ax, probabilities):
    ax.plot(probabilities, color='blue', label='Observed Probability')
    ax.axhline(y=0.5, color='red', linestyle='--', label='True Probability (0.5)')
    ax.set_title('Convergence of Coin Flip Probability to 0.5')
    ax.set_xlabel('Number of Coin Flips')
    ax.set_ylabel('Probability of Heads')
    ax.legend()

def simulate_coin_flips(num_flips):
    return np.random.choice([0, 1], size=num_flips)

def calculate_cumulative_probabilities(flips):
    cumulative_heads = np.cumsum(flips)
    return cumulative_heads / (np.arange(1, len(flips) + 1))

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

    st.latex(r"""
        \text{Law of Large Numbers (LLN):} \\
        \text{As the number of trials } n \text{ increases,} \\
        \text{the sample mean } \bar{X} \text{ converges to the population mean } \mu.
    """)

    st.latex(r"""
    \lim_{n \to \infty} P(|\bar{X}_n - \mu| < \epsilon) = 1, \text{ for any } \epsilon > 0
    """)

    st.latex(r"""
    \begin{align*}
    \bar{X}_n & : \text{ Sample mean after } n \text{ trials} \\
    \mu & : \text{ Population mean} \\
    n & : \text{ Number of trials} \\
    \epsilon & : \text{ Any small positive number}
    \end{align*}
    """)

    num_flips = st.slider("Number of Coin Flips", 10, 10000, 1000)

    coin_flips = simulate_coin_flips(num_flips)
    cumulative_probabilities = calculate_cumulative_probabilities(coin_flips)

    fig, ax = plt.subplots(figsize=(10, 6))
    plot_probability_convergence(ax, cumulative_probabilities)
    st.pyplot(fig)

    st.write(f"Final observed probability after {num_flips} flips: {cumulative_probabilities[-1]:.4f}")

if __name__ == "__main__":
    main()
