import streamlit as st

# Import theory modules
import theory.chart
import theory.vocab

# Import theorem modules
import theorem.clt
import theorem.llon

# Import probability modules
import probability.probability
import probability.monty_hall

# Import discrete distribution modules
import distributions.discrete.probability
import distributions.discrete.binomial

# Import continuous distribution modules
import distributions.continuous.normal
import distributions.continuous.triangular
import distributions.continuous.uniform
import distributions.continuous.exponential

# Import margin of error module
import moe.moe

# Import hypothesis test modules
import hypothesis_test.hypothesis_test
import hypothesis_test.chi_square

# Import machine learning modules
import ml.regression.linear_reg.gradient_descent
import ml.regression.linear_reg.linear_reg
import ml.others.kmeans

# Set up Streamlit page configuration
st.set_page_config(
    page_title="Streamlit Statistics Calculator",
    page_icon="📊",
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
st.sidebar.header("Statistical Topics")

# Create radio buttons for each group
topic = st.sidebar.radio(
    "Choose a statistical topic",
    ("Statistical Theory", "Statistical Theorems", "Probability Concepts", "Discrete Distributions", "Continuous Distributions", "Margin of Error", "Hypothesis Testing", "Chi-Square Analysis", "Machine Learning Techniques")
)

option = None
machine_learning_type = None

# Based on the distribution type selected, show the corresponding options
if topic == "Statistical Theory":
    option = st.sidebar.radio(
        "Theory Topics",
        ["Statistical Vocabulary", "Chart Principles"]
    )
elif topic == "Discrete Distributions":
    option = st.sidebar.radio(
        "Discrete Distributions",
        ["Binomial Distribution", "Probability Distribution"]
    )
elif topic == "Continuous Distributions":
    option = st.sidebar.radio(
        "Continuous Distributions",
        ["Normal Distribution", "Triangular Distribution", "Uniform Distribution", "Exponential Distribution"]
    )
elif topic == "Probability Concepts":
    option = st.sidebar.radio(
        "Probability Concepts",
        ["Probability Calculations", "Monty Hall Problem"]
    )
elif topic == "Margin of Error":
    option = "Margin of Error Calculations"
elif topic == "Hypothesis Testing":
    option = "Hypothesis Test Procedures"
elif topic == "Chi-Square Analysis":
    option = "Chi-Square Tests"
elif topic == "Statistical Theorems":
    option = st.sidebar.radio(
        "Theorems",
        ["Central Limit Theorem", "Law of Large Numbers"]
    )
elif topic == "Machine Learning Techniques":
    machine_learning_type = st.sidebar.radio(
        "Machine Learning Categories",
        ["Regression", "Classification", "Clustering"]
    )

if machine_learning_type == "Regression":
    option = st.sidebar.radio(
        "Regression Models",
        ["Gradient Descent", "Linear Regression"])
elif machine_learning_type == "Clustering":
    option = st.sidebar.radio(
        "Clustering Models",
        ["K-means Clustering"])

# Main content based on the selected option
if option == "Statistical Vocabulary":
    theory.vocab.main()
elif option == "Chart Principles":
    theory.chart.main()
elif option == "Probability Calculations":
    probability.probability.main()
elif option == "Monty Hall Problem":
    probability.monty_hall.main()
elif option == "Binomial Distribution":
    distributions.discrete.binomial.main()
elif option == "Probability Distribution":
    distributions.discrete.probability.main()
elif option == "Normal Distribution":
    distributions.continuous.normal.main()
elif option == "Triangular Distribution":
    distributions.continuous.triangular.main()
elif option == "Uniform Distribution":
    distributions.continuous.uniform.main()
elif option == "Exponential Distribution":
    distributions.continuous.exponential.main()
elif option == "Margin of Error Calculations":
    moe.moe.main()
elif option == "Hypothesis Test Procedures":
    hypothesis_test.hypothesis_test.main()
elif option == "Chi-Square Tests":
    hypothesis_test.chi_square.main()
elif option == "Central Limit Theorem":
    theorem.clt.main()
elif option == "Law of Large Numbers":
    theorem.llon.main()
elif option == "Gradient Descent":
    ml.regression.linear_reg.gradient_descent.main()
elif option == "Linear Regression":
    ml.regression.linear_reg.linear_reg.main()
elif option == "K-means Clustering":
    ml.others.kmeans.main()