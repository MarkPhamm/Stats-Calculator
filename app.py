import streamlit as st

import distributions.discrete.probability
import moe.moe

import distributions.discrete.binomial
import distributions.continuous.normal
import distributions.continuous.triangular
import distributions.continuous.uniform

import hypothesis_test.hypothesis_test

import theorem.clt
import theorem.llon


import streamlit as st

# Create a two-column layout
col1, col2 = st.columns(2)

# Display a resized image in the first column
with col1:
    st.image("images/image.jpg", width=200)  # Adjust the width as needed

# Display header and text in the second column
with col2:
    st.header("Statistic Calculator")
    st.markdown("By [Minh (Mark) Pham](https://www.linkedin.com/in/minhbphamm/)")

# Sidebar with grouped radio buttons
st.sidebar.header("Distribution Types")

# Create radio buttons for each group
distribution_type = st.sidebar.radio(
    "Choose a topic",
    ("Discrete Distributions", "Continuous Distributions", "MOE", "Hypothesis Test", "Theorem")
)

option = None

# Based on the distribution type selected, show the corresponding options
if distribution_type == "Discrete Distributions":
    option = st.sidebar.radio(
        "Discrete Distributions",
        ["Binomial", "Probability"]
    )
elif distribution_type == "Continuous Distributions":
    option = st.sidebar.radio(
        "Continuous Distributions",
        ["Normal", "Triangular", "Uniform"]
    )

elif distribution_type == "MOE":
    option = "MOE"

elif distribution_type == "Hypothesis Test":
    option = "Hypothesis Test"

elif distribution_type == "Theorem":
    option = st.sidebar.radio(
        "Theorem",
        ["Central Limit Theorem", "Law of the Large number"]
    )



# Main content based on the selected option
if option == "Binomial":
    distributions.discrete.binomial.main()

if option == "Probability":
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

elif option == "Central Limit Theorem":
    theorem.clt.main()

elif option == "Law of the Large number":
    theorem.llon.main()