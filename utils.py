import streamlit as st

# Function to add custom CSS
def add_custom_css():
    st.markdown("""
        <style>
        h1, h2 {
            color: red !important;
        }
        </style>
        """, unsafe_allow_html=True)