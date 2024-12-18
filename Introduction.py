import streamlit as st

import utils

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

st.markdown("""
    <h2 style="text-align:center;">Welcome to the Statistics Calculator App!</h2>
    <p style="font-size:18px;">👋 Hi y'all, it's Mark here! I'm a BIS and Mathematics student at <strong>Texas Christian University</strong>. I noticed that many TCU students are struggling with the <strong>INSC 20153</strong> and <strong>MATH 30853</strong> courses. That's why I designed this app to help you easily perform various statistical calculations and explore machine learning concepts.</p>
    
    <h3 style="margin-top:30px;">🚀 Quick Guide on How to Use the App:</h3>
    <ul style="font-size:16px; line-height:1.6;">
        <li>📊 Select a topic from the sidebar to explore different statistical methods or ml categories.</li>
        <li>📝 Follow the prompts to input your data or parameters.</li>
        <li>📈 View the results and visualizations generated by the app.</li>
    </ul>
    
    <p style="font-size:18px; margin-top:20px;">💡 Feel free to <strong>reach out</strong> for help or <strong>report any bugs</strong> using the links in the menu!</p>
""", unsafe_allow_html=True)
