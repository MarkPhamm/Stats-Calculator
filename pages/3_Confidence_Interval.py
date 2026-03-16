import streamlit as st

import moe.moe
import moe.moe_inverse
import utils

# Set up Streamlit page configuration
st.set_page_config(
    page_title="Confidence Intervals & Margin of Error",
    page_icon="📊",
    initial_sidebar_state="expanded",
    layout="wide",
    menu_items={
        "Get Help": "https://www.linkedin.com/in/minhbphamm/",
        "Report a bug": "https://www.linkedin.com/in/minhbphamm/",
        "About": "# Comprehensive Statistics Calculator",
    },
)

# Apply custom CSS styling
utils.add_custom_css()

# ==========================================
# SIDEBAR NAVIGATION
# ==========================================
st.sidebar.markdown("---")
st.sidebar.header("📊 Margin of Error")

# Create radio buttons for margin of error options
option = st.sidebar.radio(
    "Choose an option",
    ["📐 Margin of Error", "🔄 Margin of Error Inverse"],
    key="moe_option",
)

# ==========================================
# PAGE HEADER
# ==========================================
utils.render_header(
    title="🎯 Confidence Intervals & Margin of Error",
    subtitle="Calculate confidence intervals and margin of error for your sample data",
)

# ==========================================
# INFO BOX
# ==========================================
utils.render_info_box(
    title="What is Margin of Error?",
    content="The margin of error (MOE) measures the maximum expected difference between an estimated parameter and the true population parameter. It depends on sample size, confidence level, and population variability. Use this tool to calculate MOE or find the required sample size.",
    icon="📐",
)

# ==========================================
# CONCEPT CARDS
# ==========================================
st.markdown("### 📚 Key Concepts")

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <div style="
            background: linear-gradient(145deg, #0F172A, #0B1120);
            border-left: 4px solid #00AEEF;
            border-radius: 12px;
            padding: 25px;
        ">
            <div style="font-weight: 600; color: #00AEEF; margin-bottom: 12px; font-size: 1.1rem;">
                📐 Margin of Error (Forward)
            </div>
            <div style="color: #CBD5E1; line-height: 1.7; font-size: 0.95rem;">
                <strong>What it does:</strong> Given sample size, confidence level, and population 
                proportion, calculate the margin of error.
                <br><br>
                <strong>Formula:</strong> MOE = Z × √(p(1-p)/n)
                <br><br>
                <strong>Use when:</strong> You have a sample and want to estimate precision.
            </div>
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
            padding: 25px;
        ">
            <div style="font-weight: 600; color: #00AEEF; margin-bottom: 12px; font-size: 1.1rem;">
                🔄 Inverse (Reverse)
            </div>
            <div style="color: #CBD5E1; line-height: 1.7; font-size: 0.95rem;">
                <strong>What it does:</strong> Given desired margin of error and confidence level, 
                calculate the required sample size.
                <br><br>
                <strong>Formula:</strong> n = (Z² × p(1-p)) / MOE²
                <br><br>
                <strong>Use when:</strong> You want to determine sample size requirements.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

utils.render_section_divider()

# ==========================================
# CONFIDENCE LEVELS REFERENCE
# ==========================================
st.markdown("### 📊 Confidence Levels & Z-Scores")

col1, col2, col3 = st.columns(3)

confidence_levels = [("90%", "1.645"), ("95%", "1.960"), ("99%", "2.576")]

for idx, (conf, z_score) in enumerate(confidence_levels):
    cols = [col1, col2, col3]
    with cols[idx]:
        st.markdown(
            f"""
            <div style="
                background: linear-gradient(145deg, rgba(0, 174, 239, 0.1), rgba(0, 174, 239, 0.05));
                border: 1px solid rgba(0, 174, 239, 0.3);
                border-radius: 12px;
                padding: 20px;
                text-align: center;
            ">
                <div style="font-size: 1.8rem; color: #00AEEF; font-weight: 700; margin-bottom: 8px;">
                    {conf}
                </div>
                <div style="color: #CBD5E1; font-size: 0.9rem; margin-bottom: 10px;">Confidence Level</div>
                <div style="color: #E0E7FF; font-weight: 600; font-size: 1.2rem;">
                    Z = {z_score}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

utils.render_section_divider()

# ==========================================
# MAIN CONTENT
# ==========================================
if option == "📐 Margin of Error":
    moe.moe.main()
elif option == "🔄 Margin of Error Inverse":
    moe.moe_inverse.main()

# ==========================================
# FOOTER
# ==========================================
utils.render_footer()
