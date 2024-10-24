import streamlit as st
import utils
# Import theory modules
import theory.chart
import theory.vocab

# Import theorem modules
import theorem.clt
import theorem.llon

# Import probability modules
import probability.probability
import probability.monty_hall

# Set up Streamlit page configuration
st.set_page_config(
    page_title="Statistics Theory",
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
    ("Statistical Theory", "Statistical Theorems", "Probability Concepts")
)

option = None
machine_learning_type = None

# Based on the distribution type selected, show the corresponding options
if topic == "Statistical Theory":
    option = st.sidebar.radio(
        "Theory Topics",
        ["Statistical Vocabulary", "Chart Principles"]
    )
elif topic == "Statistical Theorems":
    option = st.sidebar.radio(
        "Theorems",
        ["Central Limit Theorem", "Law of Large Numbers"]
    )
elif topic == "Probability Concepts":
    option = st.sidebar.radio(
        "Probability Concepts",
        ["Probability Calculations", "Monty Hall Problem"]
    )

# Main content based on the selected option
if option == "Statistical Vocabulary":
    theory.vocab.main()
elif option == "Chart Principles":
    theory.chart.main()
elif option == "Central Limit Theorem":
    theorem.clt.main()
elif option == "Law of Large Numbers":
    theorem.llon.main()
elif option == "Probability Calculations":
    probability.probability.main()
elif option == "Monty Hall Problem":
    probability.monty_hall.main()