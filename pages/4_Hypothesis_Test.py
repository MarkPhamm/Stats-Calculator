import streamlit as st

import hypothesis_test.anova
import hypothesis_test.chi_square

# Import hypothesis test modules
import hypothesis_test.hypothesis_test
import utils

# Set up Streamlit page configuration
st.set_page_config(
    page_title="Hypothesis Testing",
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
st.sidebar.header("🧪 Test Types")

# Create radio buttons for hypothesis testing
test_type = st.sidebar.radio(
    "Select Test Type",
    ("🎯 Hypothesis Test (Mean/Prop)", "📊 Chi-Square Test", "📈 ANOVA Test"),
    key="hyp_test_type"
)

# ==========================================
# PAGE HEADER
# ==========================================
utils.render_header(
    title="🧪 Hypothesis Testing",
    subtitle="Make data-driven decisions using statistical hypothesis tests"
)

# ==========================================
# INFO BOX
# ==========================================
utils.render_info_box(
    title="What is Hypothesis Testing?",
    content="Hypothesis testing is a statistical method for making decisions about populations based on sample data. We test a null hypothesis (H0) against an alternative hypothesis (H1) to determine if there is significant evidence to reject the null hypothesis.",
    icon="🔬"
)

# ==========================================
# TEST TYPES OVERVIEW
# ==========================================
st.markdown("### 📋 Available Tests")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div style="
            background: linear-gradient(145deg, #0F172A, #0B1120);
            border-left: 4px solid #00AEEF;
            border-radius: 12px;
            padding: 25px;
            height: 280px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        ">
            <div style="font-size: 2rem; margin-bottom: 12px;">🎯</div>
            <div style="font-weight: 600; color: #E0E7FF; margin-bottom: 12px; font-size: 1.1rem;">
                T-Test & Z-Test
            </div>
            <div style="color: #CBD5E1; line-height: 1.6; font-size: 0.95rem;">
                Test hypotheses about population means and proportions using one-sample, two-sample,
                paired, and proportion tests.
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
            height: 280px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        ">
            <div style="font-size: 2rem; margin-bottom: 12px;">📊</div>
            <div style="font-weight: 600; color: #E0E7FF; margin-bottom: 12px; font-size: 1.1rem;">
                Chi-Square Test
            </div>
            <div style="color: #CBD5E1; line-height: 1.6; font-size: 0.95rem;">
                Test independence and goodness-of-fit for categorical data. Perfect for analyzing
                relationships between categorical variables.
            </div>
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
            padding: 25px;
            height: 280px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        ">
            <div style="font-size: 2rem; margin-bottom: 12px;">📈</div>
            <div style="font-weight: 600; color: #E0E7FF; margin-bottom: 12px; font-size: 1.1rem;">
                ANOVA
            </div>
            <div style="color: #CBD5E1; line-height: 1.6; font-size: 0.95rem;">
                Compare means across multiple groups simultaneously. Tests if there are significant
                differences between three or more groups.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ==========================================
# HYPOTHESIS TESTING STEPS
# ==========================================
utils.render_section_divider()

st.markdown("### 📝 The Hypothesis Testing Process")

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <div style="
            background: linear-gradient(145deg, rgba(0, 174, 239, 0.08), rgba(0, 174, 239, 0.02));
            border: 1px solid rgba(0, 174, 239, 0.2);
            border-radius: 12px;
            padding: 25px;
        ">
            <h4 style="color: #00AEEF; border-left: none; margin-top: 0;">1️⃣ Set Up Hypotheses</h4>
            <ul style="color: #CBD5E1; line-height: 1.8;">
                <li><strong>H₀ (Null):</strong> No effect or difference exists</li>
                <li><strong>H₁ (Alt):</strong> An effect or difference exists</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    st.markdown(
        """
        <div style="
            background: linear-gradient(145deg, rgba(0, 174, 239, 0.08), rgba(0, 174, 239, 0.02));
            border: 1px solid rgba(0, 174, 239, 0.2);
            border-radius: 12px;
            padding: 25px;
            margin-top: 15px;
        ">
            <h4 style="color: #00AEEF; border-left: none; margin-top: 0;">2️⃣ Choose Significance Level</h4>
            <ul style="color: #CBD5E1; line-height: 1.8;">
                <li><strong>α (alpha):</strong> Usually 0.05 (5%)</li>
                <li>Probability of rejecting H₀ when true</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div style="
            background: linear-gradient(145deg, rgba(0, 174, 239, 0.08), rgba(0, 174, 239, 0.02));
            border: 1px solid rgba(0, 174, 239, 0.2);
            border-radius: 12px;
            padding: 25px;
        ">
            <h4 style="color: #00AEEF; border-left: none; margin-top: 0;">3️⃣ Calculate Test Statistic</h4>
            <ul style="color: #CBD5E1; line-height: 1.8;">
                <li>T-statistic, Z-statistic, or χ² value</li>
                <li>Measure difference from null hypothesis</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    st.markdown(
        """
        <div style="
            background: linear-gradient(145deg, rgba(0, 174, 239, 0.08), rgba(0, 174, 239, 0.02));
            border: 1px solid rgba(0, 174, 239, 0.2);
            border-radius: 12px;
            padding: 25px;
            margin-top: 15px;
        ">
            <h4 style="color: #00AEEF; border-left: none; margin-top: 0;">4️⃣ Make a Decision</h4>
            <ul style="color: #CBD5E1; line-height: 1.8;">
                <li><strong>p-value &lt; α:</strong> Reject H₀</li>
                <li><strong>p-value ≥ α:</strong> Fail to reject H₀</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

utils.render_section_divider()

# ==========================================
# MAIN CONTENT
# ==========================================
if test_type == "🎯 Hypothesis Test (Mean/Prop)":
    hypothesis_test.hypothesis_test.main()
elif test_type == "📊 Chi-Square Test":
    hypothesis_test.chi_square.main()
elif test_type == "📈 ANOVA Test":
    hypothesis_test.anova.main()

# ==========================================
# FOOTER
# ==========================================
utils.render_footer()