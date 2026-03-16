import os
import sys

import pandas as pd
import streamlit as st

# Allow imports from project root
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import utils

# ==========================================
# PAGE CONFIG
# ==========================================
st.set_page_config(
    page_title="Tree-Based ML Models",
    page_icon="🌲",
    initial_sidebar_state="expanded",
    layout="wide",
    menu_items={
        "Get Help": "https://www.linkedin.com/in/minhbphamm/",
        "Report a bug": "https://www.linkedin.com/in/minhbphamm/",
        "About": "# Tree-Based Machine Learning Models",
    },
)

# Apply custom CSS
try:
    utils.add_custom_css()
except AttributeError:
    pass

# ==========================================
# SIDEBAR
# ==========================================
st.sidebar.markdown("---")
st.sidebar.header("🌲 Tree Model Selection")

model_options = [
    "🏠 Overview",
    "🌲 Random Forest",
    "📈 Gradient Boosting",
    "🔁 AdaBoost",
    "⚡ XGBoost",
    "🌿 LightGBM",
    "🐱 CatBoost",
]

selected = st.sidebar.radio("Choose a Model", model_options, key="tree_model_select")

# ==========================================
# HEADER
# ==========================================
try:
    utils.render_header(
        title="🌲 Tree-Based Machine Learning",
        subtitle="Explore ensemble tree algorithms: Random Forest, Gradient Boosting, XGBoost, LightGBM, AdaBoost & CatBoost",
    )
except AttributeError:
    st.title("🌲 Tree-Based Machine Learning Models")

# ==========================================
# OVERVIEW PAGE
# ==========================================
if selected == "🏠 Overview":
    try:
        utils.render_info_box(
            title="What Are Tree-Based Models?",
            content=(
                "Tree-based algorithms build models as decision trees or ensembles of trees. "
                "They split data step-by-step based on feature values, capturing complex non-linear "
                "patterns while remaining relatively interpretable."
            ),
            icon="🌳",
        )
    except AttributeError:
        st.info(
            "Tree-based algorithms build models as decision trees or ensembles of trees. They split data step-by-step based on feature values, capturing complex non-linear patterns while remaining relatively interpretable."
        )

    st.markdown("---")
    st.markdown("### 🗺️ Model Family Overview")

    col1, col2, col3 = st.columns(3)

    cards = [
        (
            "🌲",
            "Random Forest",
            "Bagging",
            "Trains many independent trees on bootstrap samples; averages predictions. Reduces variance.",
        ),
        (
            "📈",
            "Gradient Boosting",
            "Boosting",
            "Trains trees sequentially, each correcting residual errors of the prior ensemble.",
        ),
        (
            "🔁",
            "AdaBoost",
            "Boosting",
            "Re-weights training samples — hard samples get higher weights each round.",
        ),
        (
            "⚡",
            "XGBoost",
            "Boosting+",
            "Regularised gradient boosting with second-order gradients, pruning, and parallelism.",
        ),
        (
            "🌿",
            "LightGBM",
            "Boosting+",
            "Leaf-wise growth + histogram binning = extremely fast on large/high-dim datasets.",
        ),
        (
            "🐱",
            "CatBoost",
            "Boosting+",
            "Ordered boosting + native categorical handling. Minimal preprocessing needed.",
        ),
    ]

    cols = [col1, col2, col3, col1, col2, col3]
    for (emoji, name, tag, desc), col in zip(cards, cols):
        with col:
            st.markdown(
                f"""
                <div style="
                    background: linear-gradient(145deg, #0F172A, #0B1120);
                    border-left: 4px solid #00AEEF;
                    border-radius: 12px;
                    padding: 22px;
                    margin-bottom: 18px;
                    min-height: 180px;
                ">
                    <div style="font-size: 1.8rem; margin-bottom: 6px;">{emoji}</div>
                    <div style="color: #00AEEF; font-weight: 700; font-size: 1rem;">{name}</div>
                    <div style="color: #64748B; font-size: 0.78rem; margin-bottom: 10px;">
                        <span style="background:#1E293B; border-radius:4px; padding:2px 8px;">{tag}</span>
                    </div>
                    <div style="color: #CBD5E1; font-size: 0.88rem; line-height: 1.55;">{desc}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("---")
    st.markdown("### 📊 Quick Comparison")

    comparison_data = {
        "Model": [
            "Random Forest",
            "Gradient Boosting",
            "AdaBoost",
            "XGBoost",
            "LightGBM",
            "CatBoost",
        ],
        "Training Style": [
            "Parallel (Bagging)",
            "Sequential",
            "Sequential",
            "Sequential+Parallel",
            "Sequential+Parallel",
            "Sequential",
        ],
        "Speed": ["⚡⚡⚡", "⚡⚡", "⚡⚡", "⚡⚡⚡", "⚡⚡⚡⚡", "⚡⚡⚡"],
        "Accuracy": [
            "⭐⭐⭐⭐",
            "⭐⭐⭐⭐",
            "⭐⭐⭐",
            "⭐⭐⭐⭐⭐",
            "⭐⭐⭐⭐⭐",
            "⭐⭐⭐⭐⭐",
        ],
        "Ease of Use": [
            "🟢 Easy",
            "🟡 Medium",
            "🟢 Easy",
            "🟡 Medium",
            "🟡 Medium",
            "🟢 Easy",
        ],
        "Categorical Data": [
            "❌ Manual",
            "❌ Manual",
            "❌ Manual",
            "❌ Manual",
            "🟡 Partial",
            "✅ Native",
        ],
        "Overfitting Risk": [
            "Low",
            "Medium",
            "High (noisy data)",
            "Medium (regularised)",
            "Medium",
            "Low",
        ],
    }

    st.table(pd.DataFrame(comparison_data).set_index("Model"))

    st.markdown("---")
    st.markdown(
        """
        <div style="text-align:center; padding: 40px 20px;
            background: linear-gradient(145deg, rgba(0,174,239,0.05), rgba(0,174,239,0.02));
            border-radius: 16px; margin: 20px 0;">
            <div style="font-size: 2.5rem; margin-bottom: 12px;">👈</div>
            <h3 style="color: #E0E7FF; border-left: none;">Select a model from the sidebar to explore it</h3>
            <p style="color: #94A3B8;">Each model page includes theory, interactive simulations, and a practical training tool.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ==========================================
# MODEL PAGES
# ==========================================
elif selected == "🌲 Random Forest":
    from tree_based_ml import random_forest

    random_forest.main()

elif selected == "📈 Gradient Boosting":
    from tree_based_ml import gradient_boosting

    gradient_boosting.main()

elif selected == "🔁 AdaBoost":
    from tree_based_ml import adaboost

    adaboost.main()

elif selected == "⚡ XGBoost":
    from tree_based_ml import xgboost_model

    xgboost_model.main()

elif selected == "🌿 LightGBM":
    from tree_based_ml import lightgbm_model

    lightgbm_model.main()

elif selected == "🐱 CatBoost":
    from tree_based_ml import catboost_model

    catboost_model.main()

# ==========================================
# FOOTER
# ==========================================
try:
    utils.render_footer()
except AttributeError:
    pass
