import streamlit as st

def main():
    # Title of the app
    st.title("Probability Rules and Concepts")

    # Union of Two Events
    st.header("1. Union of Two Events")
    st.latex(r'''
    P(A \cup B) = P(A) + P(B) - P(A \cap B)
    ''')
    st.latex(r'''
    \text{If } P(A \cap B) = 0 \text{, then } A \text{ and } B \text{ are mutually exclusive.}
    ''')
    st.latex(r'''
    \text{If } P(A \cap B) = P(A) \cdot P(B) \text{, then } A \text{ and } B \text{ are independent.}
    ''')
    st.latex(r'''
    \text{Never conclude: } P(A \cap B) = P(A) \cdot P(B) \not\rightarrow A \text{ and } B \text{ are independent.}
    ''')
    st.latex(r'''
    \text{Only conclude: } P(A \cap B) \neq P(A) \cdot P(B) \rightarrow A \text{ and } B \text{ are not independent.}
    ''')

    # Conditional Probability
    st.header("2. Conditional Probability")
    st.latex(r'''
    P(A|B) = \frac{P(A \cap B)}{P(B)}
    ''')
    st.latex(r'''
    \text{If } P(A|B) = P(A) \text{ and } P(B|A) = P(B) \text{, then } A \text{ and } B \text{ are independent.}
    ''')
    st.latex(r'''
    \text{If } P(A|B) \neq P(A) \text{ and } P(B|A) \neq P(B) \text{, then } A \text{ and } B \text{ are dependent.}
    ''')

    # Complements
    st.header("3. Complements")
    st.latex(r'''
    P(A^c) = 1 - P(A)
    ''')

    # The General Multiplication Rule
    st.header("4. The General Multiplication Rule")
    st.latex(r'''
    P(A \cap B) = P(A) \cdot P(A|B)
    ''')

if __name__ == "__main__":
    main()
