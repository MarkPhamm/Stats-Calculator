import streamlit as st

import moe.moe

import distributions.binomial
import distributions.normal
import distributions.triangular
import distributions.uniform


import streamlit as st

# Create a two-column layout
col1, col2 = st.columns(2)

# Display a resized image in the first column
with col1:
    st.image("images/image.jpg", width=200)  # Adjust the width as needed

# Display header and text in the second column
with col2:
    st.header("Statistic Calculator")
    st.text("By Minh (Mark) Pham")

# Sidebar with radio buttons
option = st.sidebar.radio(
    "Choose an option",
    ["MOE", "Normal", "Triangular", "Uniform"]
)

# Main content based on the selected option
if option == "MOE":
    moe.moe.main()

elif option == "Normal":
    distributions.normal.main()

elif option == "Triangular":
    distributions.triangular.main()
# Option for the second "Normal"
elif option == "Uniform":
    distributions.uniform.main()
