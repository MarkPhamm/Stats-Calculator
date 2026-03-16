import streamlit as st

import distributions.continuous.exponential

# Import continuous distribution modules
import distributions.continuous.normal
import distributions.continuous.triangular
import distributions.continuous.uniform
import distributions.discrete.binomial
import distributions.discrete.poisson

# Import discrete distribution modules
import distributions.discrete.probability
import utils

# Set up Streamlit page configuration
st.set_page_config(
    page_title="Probability Distributions",
    page_icon="📊",
    initial_sidebar_state="expanded",
    layout="wide",
    menu_items={
        'Get Help': 'https://www.linkedin.com/in/minhbphamm/',
        'Report a bug': "https://www.linkedin.com/in/minhbphamm/",
        'About': "# Comprehensive Statistics Calculator"
    }
)

# Apply custom CSS styling
utils.add_custom_css()

# ==========================================
# SIDEBAR NAVIGATION
# ==========================================
st.sidebar.markdown("---")
st.sidebar.header("📊 Distribution Types")

# Create radio buttons for distribution type
topic = st.sidebar.radio(
    "Choose a statistical topic",
    ("🔢 Discrete Distributions", "📈 Continuous Distributions"),
    key="dist_type"
)

option = None

# Based on the distribution type selected, show the corresponding options
if topic == "🔢 Discrete Distributions":
    option = st.sidebar.radio(
        "Discrete Distributions",
        ["Binomial Distribution", "Probability Distribution", "Poisson Distribution"],
        key="discrete_option"
    )
elif topic == "📈 Continuous Distributions":
    option = st.sidebar.radio(
        "Continuous Distributions",
        ["Normal Distribution", "Triangular Distribution", "Uniform Distribution", "Exponential Distribution"],
        key="continuous_option"
    )

# ==========================================
# PAGE HEADER
# ==========================================
utils.render_header(
    title="📊 Probability Distributions",
    subtitle="Understand and visualize discrete and continuous probability distributions"
)

# ==========================================
# INFO BOX
# ==========================================
utils.render_info_box(
    title="About Probability Distributions",
    content="Probability distributions describe how values of a random variable are distributed. They are fundamental to statistics and help model real-world phenomena. Explore both discrete (e.g., Binomial, Poisson) and continuous (e.g., Normal, Uniform) distributions.",
    icon="📐"
)

utils.render_section_divider()

# ==========================================
# QUICK REFERENCE CARDS
# ==========================================
if topic == "🔢 Discrete Distributions":
    st.markdown("### 🔢 Discrete Distributions")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(
            """
            <div style="
                background: linear-gradient(145deg, #0F172A, #0B1120);
                border-left: 4px solid #00AEEF;
                border-radius: 12px;
                padding: 20px;
                text-align: center;
            ">
                <div style="font-size: 2rem; margin-bottom: 10px;">🎲</div>
                <div style="color: #E0E7FF; font-weight: 600; margin-bottom: 5px;">Binomial</div>
                <div style="color: #94A3B8; font-size: 0.9rem;">Success/failure outcomes</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    
    with col2:
        st.markdown(
            """
            <div style="
                background: linear-gradient(145deg, #0F172A, #0B1120);
                border-left: 4px solid #00AEEF;
                border-radius: 12px;
                padding: 20px;
                text-align: center;
            ">
                <div style="font-size: 2rem; margin-bottom: 10px;">📊</div>
                <div style="color: #E0E7FF; font-weight: 600; margin-bottom: 5px;">Poisson</div>
                <div style="color: #94A3B8; font-size: 0.9rem;">Count of events</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    
    with col3:
        st.markdown(
            """
            <div style="
                background: linear-gradient(145deg, #0F172A, #0B1120);
                border-left: 4px solid #00AEEF;
                border-radius: 12px;
                padding: 20px;
                text-align: center;
            ">
                <div style="font-size: 2rem; margin-bottom: 10px;">🎯</div>
                <div style="color: #E0E7FF; font-weight: 600; margin-bottom: 5px;">Probability</div>
                <div style="color: #94A3B8; font-size: 0.9rem;">Basic probabilities</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

else:
    st.markdown("### 📈 Continuous Distributions")
    col1, col2 = st.columns(2)
    
    with col1:
        col1a, col1b = st.columns(2)
        with col1a:
            st.markdown(
                """
                <div style="
                    background: linear-gradient(145deg, #0F172A, #0B1120);
                    border-left: 4px solid #00AEEF;
                    border-radius: 12px;
                    padding: 20px;
                    text-align: center;
                ">
                    <div style="font-size: 2rem; margin-bottom: 10px;">🔔</div>
                    <div style="color: #E0E7FF; font-weight: 600; margin-bottom: 5px;">Normal</div>
                    <div style="color: #94A3B8; font-size: 0.9rem;">Bell curve</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with col1b:
            st.markdown(
                """
                <div style="
                    background: linear-gradient(145deg, #0F172A, #0B1120);
                    border-left: 4px solid #00AEEF;
                    border-radius: 12px;
                    padding: 20px;
                    text-align: center;
                ">
                    <div style="font-size: 2rem; margin-bottom: 10px;">⚡</div>
                    <div style="color: #E0E7FF; font-weight: 600; margin-bottom: 5px;">Exponential</div>
                    <div style="color: #94A3B8; font-size: 0.9rem;">Decay rate</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
    
    with col2:
        col2a, col2b = st.columns(2)
        with col2a:
            st.markdown(
                """
                <div style="
                    background: linear-gradient(145deg, #0F172A, #0B1120);
                    border-left: 4px solid #00AEEF;
                    border-radius: 12px;
                    padding: 20px;
                    text-align: center;
                ">
                    <div style="font-size: 2rem; margin-bottom: 10px;">📏</div>
                    <div style="color: #E0E7FF; font-weight: 600; margin-bottom: 5px;">Uniform</div>
                    <div style="color: #94A3B8; font-size: 0.9rem;">Equal probability</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with col2b:
            st.markdown(
                """
                <div style="
                    background: linear-gradient(145deg, #0F172A, #0B1120);
                    border-left: 4px solid #00AEEF;
                    border-radius: 12px;
                    padding: 20px;
                    text-align: center;
                ">
                    <div style="font-size: 2rem; margin-bottom: 10px;">📐</div>
                    <div style="color: #E0E7FF; font-weight: 600; margin-bottom: 5px;">Triangular</div>
                    <div style="color: #94A3B8; font-size: 0.9rem;">Three-point dist.</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

utils.render_section_divider()

# ==========================================
# MAIN CONTENT
# ==========================================
if option == "Binomial Distribution":
    distributions.discrete.binomial.main()
elif option == "Probability Distribution":
    distributions.discrete.probability.main()
elif option == "Poisson Distribution":
    distributions.discrete.poisson.main()
elif option == "Normal Distribution":
    distributions.continuous.normal.main()
elif option == "Triangular Distribution":
    distributions.continuous.triangular.main()
elif option == "Uniform Distribution":
    distributions.continuous.uniform.main()
elif option == "Exponential Distribution":
    distributions.continuous.exponential.main()
else:
    # Default welcome message
    st.markdown(
        """
        <div style="
            text-align: center;
            padding: 60px 20px;
            background: linear-gradient(145deg, rgba(0, 174, 239, 0.05), rgba(0, 174, 239, 0.02));
            border-radius: 16px;
            margin: 30px 0;
        ">
            <div style="font-size: 3rem; margin-bottom: 20px;">📊</div>
            <h3 style="color: #E0E7FF; border-left: none;">Select a distribution to explore</h3>
            <p style="color: #94A3B8; font-size: 1.1rem;">
                Choose from discrete or continuous distributions in the sidebar.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ==========================================
# FOOTER
# ==========================================
utils.render_footer()