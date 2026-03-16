import streamlit as st

import utils
from ml.supervised.classification import decision_tree, logistic_reg

# Import machine learning modules
from ml.supervised.regression import linear_reg
from ml.unsupervised import kmeans, pca

# Set up Streamlit page configuration
st.set_page_config(
    page_title="Machine Learning Models",
    page_icon="🤖",
    initial_sidebar_state="expanded",
    layout="wide",
    menu_items={
        "Get Help": "https://www.linkedin.com/in/minhbphamm/",
        "Report a bug": "https://www.linkedin.com/in/minhbphamm/",
        "About": "# Comprehensive Statistics Calculator",
    },
)

# Apply custom CSS styling
try:
    utils.add_custom_css()
except AttributeError:
    pass

# ==========================================
# SIDEBAR NAVIGATION
# ==========================================
st.sidebar.markdown("---")
st.sidebar.header("🤖 Model Configuration")

# 1. Select Main Category
ml_category = st.sidebar.radio(
    "1️⃣ Choose Learning Type",
    ["🔵 Supervised Learning", "🟣 Unsupervised Learning"],
    key="ml_category",
)

selected_model = None

if ml_category == "🔵 Supervised Learning":
    task_type = st.sidebar.selectbox(
        "2️⃣ Choose Task Type",
        ["📊 Regression (Continuous)", "🎯 Classification (Discrete)"],
        key="task_type",
    )

    if task_type == "📊 Regression (Continuous)":
        selected_model = st.sidebar.radio(
            "3️⃣ Choose Model", ["📈 Linear Regression"], key="regression_model"
        )
    elif task_type == "🎯 Classification (Discrete)":
        selected_model = st.sidebar.radio(
            "3️⃣ Choose Model",
            ["🔵 Logistic Regression", "🌳 Decision Tree Classifier"],
            key="classification_model",
        )

elif ml_category == "🟣 Unsupervised Learning":
    selected_model = st.sidebar.radio(
        "2️⃣ Choose Model",
        ["🎪 K-Means Clustering", "📉 PCA (Dimensionality Reduction)"],
        key="unsupervised_model",
    )

# ==========================================
# PAGE HEADER
# ==========================================
utils.render_header(
    title="🤖 Machine Learning Models",
    subtitle="Build, train, and evaluate machine learning models for prediction and analysis",
)

# ==========================================
# INFO BOX
# ==========================================
utils.render_info_box(
    title="About Machine Learning",
    content="Machine learning enables computers to learn patterns from data and make predictions without explicit programming. Explore supervised learning (prediction with labeled data) and unsupervised learning (pattern discovery in unlabeled data).",
    icon="🔮",
)

# ==========================================
# ML CATEGORIES OVERVIEW
# ==========================================
st.markdown("### 📚 Machine Learning Categories")

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <div style="
            background: linear-gradient(145deg, rgba(0, 174, 239, 0.08), rgba(0, 174, 239, 0.02));
            border: 1px solid rgba(0, 174, 239, 0.2);
            border-radius: 12px;
            padding: 30px;
        ">
            <h3 style="color: #00AEEF; border-left: none; margin-top: 0;">🔵 Supervised Learning</h3>
            <p style="color: #CBD5E1; line-height: 1.7;">
                Learn from <strong>labeled training data</strong> to predict outputs for new inputs.
            </p>
            <div style="margin-top: 20px;">
                <div style="margin-bottom: 15px;">
                    <div style="color: #00AEEF; font-weight: 600; margin-bottom: 5px;">📊 Regression</div>
                    <div style="color: #94A3B8; font-size: 0.9rem;">Predict continuous values (prices, temperatures)</div>
                </div>
                <div>
                    <div style="color: #00AEEF; font-weight: 600; margin-bottom: 5px;">🎯 Classification</div>
                    <div style="color: #94A3B8; font-size: 0.9rem;">Predict categories (spam/not spam, disease/healthy)</div>
                </div>
            </div>
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
            padding: 30px;
        ">
            <h3 style="color: #00AEEF; border-left: none; margin-top: 0;">🟣 Unsupervised Learning</h3>
            <p style="color: #CBD5E1; line-height: 1.7;">
                Discover <strong>hidden patterns</strong> in unlabeled data without predefined outputs.
            </p>
            <div style="margin-top: 20px;">
                <div style="margin-bottom: 15px;">
                    <div style="color: #00AEEF; font-weight: 600; margin-bottom: 5px;">🎪 Clustering</div>
                    <div style="color: #94A3B8; font-size: 0.9rem;">Group similar items together (customer segments)</div>
                </div>
                <div>
                    <div style="color: #00AEEF; font-weight: 600; margin-bottom: 5px;">📉 Dimensionality Reduction</div>
                    <div style="color: #94A3B8; font-size: 0.9rem;">Reduce features while preserving information (PCA)</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ==========================================
# AVAILABLE MODELS
# ==========================================
utils.render_section_divider()

st.markdown("### 🛠️ Available Models")

col1, col2, col3, col4, col5 = st.columns(5)

model_cards = [
    ("📈", "Linear Regression", "Predict continuous values"),
    ("🔵", "Logistic Regression", "Binary/multi-class classification"),
    ("🌳", "Decision Tree", "Non-linear classification"),
    ("🎪", "K-Means", "Unsupervised clustering"),
    ("📉", "PCA", "Dimensionality reduction"),
]

for idx, (emoji, name, desc) in enumerate(model_cards):
    with [col1, col2, col3, col4, col5][idx]:
        st.markdown(
            f"""
            <div style="
                background: linear-gradient(145deg, #0F172A, #0B1120);
                border-left: 4px solid #00AEEF;
                border-radius: 12px;
                padding: 20px;
                text-align: center;
                height: 200px;
                display: flex;
                flex-direction: column;
                justify-content: center;
            ">
                <div style="font-size: 2rem; margin-bottom: 10px;">{emoji}</div>
                <div style="color: #E0E7FF; font-weight: 600; margin-bottom: 8px; font-size: 0.95rem;">
                    {name}
                </div>
                <div style="color: #94A3B8; font-size: 0.85rem; line-height: 1.4;">
                    {desc}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

utils.render_section_divider()

# ==========================================
# MAIN CONTENT
# ==========================================
if selected_model == "📈 Linear Regression":
    linear_reg.main()
elif selected_model == "🔵 Logistic Regression":
    logistic_reg.main()
elif selected_model == "🌳 Decision Tree Classifier":
    decision_tree.main()
elif selected_model == "🎪 K-Means Clustering":
    kmeans.main()
elif selected_model == "📉 PCA (Dimensionality Reduction)":
    pca.main()
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
            <div style="font-size: 3rem; margin-bottom: 20px;">🤖</div>
            <h3 style="color: #E0E7FF; border-left: none;">Select a model to begin</h3>
            <p style="color: #94A3B8; font-size: 1.1rem;">
                Choose a learning type, task type, and model from the sidebar to start building your machine learning model.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ==========================================
# FOOTER
# ==========================================
utils.render_footer()
