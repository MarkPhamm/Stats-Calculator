import streamlit as st
import utils

# Import machine learning modules
import ml.supervised.regression.linear_reg
import ml.supervised.regression.gradient_descent
import ml.unsupervised.kmeans

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
st.sidebar.header("Machine Learning Topics")

# Create radio buttons for machine learning categories
machine_learning_type = st.sidebar.radio(
    "Choose a machine learning category",
    ["Supervised", "Unsupervised"]
)

if machine_learning_type == "Supervised":
    option = st.sidebar.radio(
        "Supervised Learning Models",
        ["Gradient Descent", "Linear Regression"]
    )
elif machine_learning_type == "Unsupervised":
    option = st.sidebar.radio(
        "Unsupervised Learning Models",
        ["K-means Clustering"]
    )

# Main content based on the selected option
if option == "Gradient Descent":
    ml.supervised.regression.gradient_descent.main()
elif option == "Linear Regression":
    ml.supervised.regression.linear_reg.main()
elif option == "K-means Clustering":
    ml.unsupervised.kmeans.main()