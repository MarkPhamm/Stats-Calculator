import streamlit as st

import theory.vocab
import theory.vocab

import theorem.clt
import theorem.llon

import distributions.discrete.probability
import distributions.discrete.binomial

import moe.moe

import distributions.continuous.normal
import distributions.continuous.triangular
import distributions.continuous.uniform

import hypothesis_test.hypothesis_test
import hypothesis_test.chi_square

import ml.regression.linear_reg.gradient_descent
import ml.regression.linear_reg.linear_reg

import ml.others.kmeans

import streamlit as st

st.set_page_config(
    page_title="Streamlit Statistics Calculator",
    page_icon="🧊",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.linkedin.com/in/minhbphamm/',
        'Report a bug': "https://www.linkedin.com/in/minhbphamm/",
        'About': "# This an comprehensive Statistics Calculator"
    }
)
# Function to add custom CSS
def add_custom_css():
    st.markdown("""
        <style>
        h1, h2 {
            color: red !important;
        }
        </style>
        """, unsafe_allow_html=True)

add_custom_css()

# Create a two-column layout
col1, col2 = st.columns(2)

# Display a resized image in the first column
with col1:
    st.image("images/image.jpg", width=200)  # Adjust the width as needed

# Display header and text in the second column
with col2:
    st.header("Statistics Calculator")
    st.markdown("By [Minh (Mark) Pham](https://www.linkedin.com/in/minhbphamm/)")


# Sidebar with grouped radio buttons
st.sidebar.header("Distribution Types")

# Create radio buttons for each group
distribution_type = st.sidebar.radio(
    "Choose a topic",
    ("Theory", "Theorem", "Discrete Distributions", "Continuous Distributions", "Margin of Error", "Hypothesis Test", "Chi Square", "Machine Learning")
)

option = None
machine_learning_type = None

# Based on the distribution type selected, show the corresponding options
if distribution_type == "Theory":
    option = st.sidebar.radio(
        "Discrete Distributions",
        ["Vocabulary", "Chart Principles"]
    )

elif distribution_type == "Discrete Distributions":
    option = st.sidebar.radio(
        "Discrete Distributions",
        ["Binomial", "Probability"]
    )

elif distribution_type == "Continuous Distributions":
    option = st.sidebar.radio(
        "Continuous Distributions",
        ["Normal", "Triangular", "Uniform"]
    )

elif distribution_type == "Margin of Error":
    option = "MOE"

elif distribution_type == "Hypothesis Test":
    option = "Hypothesis Test"

elif distribution_type == "Chi Square":
    option = "Chi Square"

elif distribution_type == "Theorem":
    option = st.sidebar.radio(
        "Theorem",
        ["Central Limit Theorem", "Law of the Large number"]
    )

elif distribution_type == "Machine Learning":
    machine_learning_type = st.sidebar.radio(
        "Machine Learning",
        ["Continuous", "Classification", "Others"]
    )

if machine_learning_type == "Continuous":
    option = st.sidebar.radio(
        "Continuous ML model",
        ["Gradient Descent", "Linear Regression"])

elif machine_learning_type == "Others":
    option = st.sidebar.radio(
        "Others ML model",
        ["Kmeans Clustering"])

# Main content based on the selected option
if option == "Vocabulary":
    theory.vocab.main()

elif option == "Binomial":
    distributions.discrete.binomial.main()

elif option == "Probability":
    distributions.discrete.probability.main()

elif option == "Normal":
    distributions.continuous.normal.main()

elif option == "Triangular":
    distributions.continuous.triangular.main()

elif option == "Uniform":
    distributions.continuous.uniform.main()

elif option == "MOE":
    moe.moe.main()

elif option == "Hypothesis Test":
    hypothesis_test.hypothesis_test.main()

elif option == "Chi Square":
    hypothesis_test.chi_square.main()

elif option == "Central Limit Theorem":
    theorem.clt.main()

elif option == "Law of the Large number":
    theorem.llon.main()

elif option == "Gradient Descent":
    ml.regression.linear_reg.gradient_descent.main()

elif option == "Linear Regression":
    ml.regression.linear_reg.linear_reg.main()

elif option == "Kmeans Clustering":
    ml.others.kmeans.main()





    