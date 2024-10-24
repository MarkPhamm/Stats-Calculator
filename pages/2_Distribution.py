import streamlit as st
import utils

# Import discrete distribution modules
import distributions.discrete.probability
import distributions.discrete.binomial
import distributions.discrete.poisson  # Added import for Poisson distribution

# Import continuous distribution modules
import distributions.continuous.normal
import distributions.continuous.triangular
import distributions.continuous.uniform
import distributions.continuous.exponential

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

utils.add_custom_css()

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
    ("Discrete Distributions", "Continuous Distributions")  # Only keeping distribution options
)

option = None

# Based on the distribution type selected, show the corresponding options
if topic == "Discrete Distributions":
    option = st.sidebar.radio(
        "Discrete Distributions",
        ["Binomial Distribution", "Probability Distribution", "Poisson Distribution"]  # Added Poisson Distribution option
    )
elif topic == "Continuous Distributions":
    option = st.sidebar.radio(
        "Continuous Distributions",
        ["Normal Distribution", "Triangular Distribution", "Uniform Distribution", "Exponential Distribution"]
    )

# Main content based on the selected option
if option == "Binomial Distribution":
    distributions.discrete.binomial.main()
elif option == "Probability Distribution":
    distributions.discrete.probability.main()
elif option == "Poisson Distribution":  # Added handling for Poisson distribution
    distributions.discrete.poisson.main()
elif option == "Normal Distribution":
    distributions.continuous.normal.main()
elif option == "Triangular Distribution":
    distributions.continuous.triangular.main()
elif option == "Uniform Distribution":
    distributions.continuous.uniform.main()
elif option == "Exponential Distribution":
    distributions.continuous.exponential.main()