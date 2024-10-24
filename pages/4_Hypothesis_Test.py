import streamlit as st
import utils

# Import hypothesis test modules
import hypothesis_test.hypothesis_test
import hypothesis_test.chi_square

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

# Create radio buttons for hypothesis testing
option = st.sidebar.radio(
    "Choose a hypothesis test option",
    ["Hypothesis Tests", "Chi-Square Tests"]
)

# Main content based on the selected option
if option == "Hypothesis Tests":
    hypothesis_test.hypothesis_test.main()
elif option == "Chi-Square Tests":
    hypothesis_test.chi_square.main()