import streamlit as st

def main():
    # Title of the app
    st.title("Fundamental Probability Rules and Concepts")

    # Union of Two Events
    st.header("1. Union of Two Events")
    st.markdown("<p style='font-size: 24px;'>The probability of either event A or event B occurring:</p>", unsafe_allow_html=True)
    st.latex(r'''
    P(A \cup B) = P(A) + P(B) - P(A \cap B)
    ''')
    st.markdown("<h3 style='font-size: 24px;'>Important concepts:</h3>", unsafe_allow_html=True)
    st.write("   • Mutually Exclusive Events:")
    st.latex(r'''
    \text{If } P(A \cap B) = 0 \text{, then } A \text{ and } B \text{ are mutually exclusive.}
    ''')
    st.write("   • Independent Events:")
    st.latex(r'''
    \text{If } P(A \cap B) = P(A) \cdot P(B) \text{, then } A \text{ and } B \text{ are independent.}
    ''')
    st.write("   • **Caution:**")
    st.markdown("     <p style='font-size: 20px;'>", unsafe_allow_html=True)
    st.latex(r'''
    P(A \cap B) = P(A) \cdot P(B) \text{ does not necessarily imply independence.}
    ''')
    st.latex(r'''
    \text{However, } P(A \cap B) \neq P(A) \cdot P(B) \text{ does imply dependence.}
    ''')
    st.markdown("</p>", unsafe_allow_html=True)

    # Conditional Probability
    st.header("2. Conditional Probability")
    st.markdown("<p style='font-size: 24px;'>The probability of event A occurring, given that event B has occurred:</p>", unsafe_allow_html=True)
    st.latex(r'''
    P(A|B) = \frac{P(A \cap B)}{P(B)}
    ''')
    st.markdown("<p style='font-size: 24px;'>Independence in terms of conditional probability:</p>", unsafe_allow_html=True)
    st.latex(r'''
    \text{If } P(A|B) = P(A) \text{ and } P(B|A) = P(B) \text{, then } A \text{ and } B \text{ are independent.}
    ''')
    st.latex(r'''
    \text{If } P(A|B) \neq P(A) \text{ or } P(B|A) \neq P(B) \text{, then } A \text{ and } B \text{ are dependent.}
    ''')

    # Complements
    st.header("3. Complement of an Event")
    st.markdown("<p style='font-size: 24px;'>The probability of an event not occurring:</p>", unsafe_allow_html=True)
    st.latex(r'''
    P(A^c) = 1 - P(A)
    ''')

    # The General Multiplication Rule
    st.header("4. The General Multiplication Rule")
    st.markdown("<p style='font-size: 24px;'>The probability of both events A and B occurring:</p>", unsafe_allow_html=True)
    st.latex(r'''
    P(A \cap B) = P(A) \cdot P(B|A)
    ''')
    st.markdown("<p style='font-size: 24px;'>Note: This rule applies to both dependent and independent events.</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
