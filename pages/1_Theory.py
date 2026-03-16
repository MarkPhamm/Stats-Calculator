import streamlit as st

import probability.monty_hall

# Import probability modules
import probability.probability

# Import theorem modules
import theorem.clt
import theorem.llon

# Import theory modules
import theory.chart
import theory.vocab
import utils

# Set up Streamlit page configuration
st.set_page_config(
    page_title="Statistical Theory",
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
st.sidebar.header("📚 Theory Topics")

# Create radio buttons for each group
topic = st.sidebar.radio(
    "Choose a statistical topic",
    ("📖 Statistical Theory", "📐 Statistical Theorems", "🎲 Probability Concepts"),
    key="theory_topic"
)

option = None

# Based on the distribution type selected, show the corresponding options
if topic == "📖 Statistical Theory":
    option = st.sidebar.radio(
        "Theory Topics",
        ["Statistical Vocabulary", "Chart Principles"],
        key="theory_option"
    )
elif topic == "📐 Statistical Theorems":
    option = st.sidebar.radio(
        "Theorems",
        ["Central Limit Theorem", "Law of Large Numbers"],
        key="theorem_option"
    )
elif topic == "🎲 Probability Concepts":
    option = st.sidebar.radio(
        "Probability Concepts",
        ["Probability Calculations", "Monty Hall Problem"],
        key="prob_option"
    )

# ==========================================
# PAGE HEADER
# ==========================================
utils.render_header(
    title="📚 Statistical Theory & Concepts",
    subtitle="Master the fundamentals of statistics, probability, and key theoretical concepts"
)

# ==========================================
# INFO BOX
# ==========================================
utils.render_info_box(
    title="About This Section",
    content="Explore the theoretical foundations of statistics. From basic vocabulary to advanced theorems, this section helps you understand the why behind statistical methods. Select a topic from the sidebar to dive deeper.",
    icon="🔍"
)

utils.render_section_divider()

# ==========================================
# MAIN CONTENT
# ==========================================
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
            <div style="font-size: 3rem; margin-bottom: 20px;">📖</div>
            <h3 style="color: #E0E7FF; border-left: none;">Select a topic to begin</h3>
            <p style="color: #94A3B8; font-size: 1.1rem;">
                Choose from the sidebar to explore statistical theory, key theorems, or probability concepts.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ==========================================
# FOOTER
# ==========================================
utils.render_footer()