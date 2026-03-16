"""
Shared Utilities - Styling, Components and Common Functions
Modern UI/UX components with dark theme and smooth animations
"""

import streamlit as st


def add_custom_css():
    """
    Applies global CSS styling to the Streamlit app.
    Dark theme with cyan accent (Barclays inspired)
    """
    st.markdown(
        """
        <style>
            /* ========================================
               1. MAIN LAYOUT & BACKGROUND
               ======================================== */
            
            [data-testid="stAppViewContainer"] {
                background: linear-gradient(to bottom, #020617 0%, #0F172A 50%, #1E293B 100%);
                background-attachment: fixed;
                color: #F1F5F9;
                font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            }

            [data-testid="stHeader"] {
                background-color: rgba(0, 0, 0, 0);
                border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            }

            .block-container {
                padding-top: 2rem;
                padding-bottom: 3rem;
                max-width: 1400px;
            }

            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

            /* ========================================
               2. SIDEBAR STYLING
               ======================================== */
            
            section[data-testid="stSidebar"] {
                background: linear-gradient(180deg, #00395D 0%, #002B4A 50%, #001F35 100%);
                box-shadow: 4px 0 20px rgba(0, 57, 93, 0.25);
            }

            section[data-testid="stSidebar"] h1,
            section[data-testid="stSidebar"] h2,
            section[data-testid="stSidebar"] h3,
            section[data-testid="stSidebar"] span,
            section[data-testid="stSidebar"] label,
            section[data-testid="stSidebar"] p {
                color: #FFFFFF !important;
                text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
            }

            section[data-testid="stSidebar"] .stRadio > label,
            section[data-testid="stSidebar"] .stSelectbox > label {
                color: #E0E7FF !important;
                font-weight: 500;
            }

            /* ========================================
               3. HEADERS & TYPOGRAPHY
               ======================================== */
            
            h1, h2, h3, h4, h5, h6 {
                color: #FFFFFF;
                font-weight: 700;
                letter-spacing: -0.5px;
            }

            h1 {
                font-size: 2.5rem !important;
                background: linear-gradient(90deg, #00AEEF 0%, #38BDF8 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                padding-bottom: 12px;
                border-bottom: 2px solid #00AEEF;
                margin-bottom: 20px !important;
            }

            h2 {
                font-size: 1.8rem !important;
                border-left: 4px solid #00AEEF;
                padding-left: 12px;
                margin-top: 25px !important;
                margin-bottom: 15px !important;
            }

            h3 {
                font-size: 1.3rem !important;
                color: #E0E7FF;
                margin-top: 20px !important;
                margin-bottom: 12px !important;
            }

            p {
                color: #CBD5E1;
                font-size: 1rem;
                line-height: 1.6;
            }

            /* ========================================
               4. CARD COMPONENTS
               ======================================== */
            
            [data-testid="stExpander"] {
                background: linear-gradient(145deg, #0F172A, #0B1120) !important;
                border: 1px solid rgba(56, 189, 248, 0.2) !important;
                border-radius: 12px !important;
            }

            [data-testid="stExpander"] > div > div:first-child {
                color: #E0E7FF !important;
            }

            /* ========================================
               5. METRIC CARDS
               ======================================== */
            
            [data-testid="stMetric"] {
                background: linear-gradient(145deg, #0F172A, #0B1120);
                border: 1px solid rgba(56, 189, 248, 0.15);
                border-radius: 12px;
                padding: 20px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
            }

            [data-testid="stMetric"] > div:first-child {
                color: #94A3B8;
                font-size: 0.85rem;
                font-weight: 600;
                text-transform: uppercase;
                letter-spacing: 1px;
            }

            [data-testid="stMetric"] > div:nth-child(2) {
                color: #00AEEF;
                font-size: 2rem;
                font-weight: 700;
            }

            /* ========================================
               6. FORM CONTROLS
               ======================================== */
            
            /* Multiselect */
            span[data-baseweb="tag"] {
                background-color: #00AEEF !important;
                color: #000000 !important;
                font-weight: 600 !important;
            }

            /* Select/Multiselect Dropdowns */
            div[data-baseweb="select"] > div {
                background-color: rgba(0, 174, 239, 0.1) !important;
                border: 2px solid #00AEEF !important;
                border-radius: 12px !important;
                color: #E0E7FF !important;
            }

            /* Radio Buttons */
            div[data-testid="stRadio"] > div {
                background-color: rgba(0, 174, 239, 0.08) !important;
                border: 2px solid rgba(0, 174, 239, 0.5) !important;
                border-radius: 12px !important;
                padding: 12px !important;
            }

            div[data-testid="stRadio"] label {
                color: #E0E7FF !important;
            }

            /* Selectbox */
            div[data-testid="stSelectbox"] > div {
                background-color: rgba(0, 174, 239, 0.1) !important;
                border: 2px solid #00AEEF !important;
                border-radius: 12px !important;
            }

            div[data-testid="stSelectbox"] span {
                color: #E0E7FF !important;
            }

            /* Text Input */
            input[type="text"],
            input[type="number"],
            textarea {
                background-color: rgba(255, 255, 255, 0.05) !important;
                border: 1px solid rgba(255, 255, 255, 0.12) !important;
                color: #E0E7FF !important;
                border-radius: 8px !important;
                padding: 10px !important;
            }

            input[type="text"]:focus,
            input[type="number"]:focus,
            textarea:focus {
                border: 2px solid #00AEEF !important;
                box-shadow: 0 0 10px rgba(0, 174, 239, 0.3) !important;
            }

            /* File Uploader */
            [data-testid="stFileUploader"] {
                background-color: rgba(0, 174, 239, 0.08);
                border: 2px dashed #00AEEF;
                border-radius: 12px;
                padding: 20px;
            }

            /* ========================================
               7. BUTTONS
               ======================================== */
            
            button[kind="primary"] {
                background: linear-gradient(135deg, #00AEEF 0%, #0090C8 100%) !important;
                color: #000000 !important;
                font-weight: 700 !important;
                border: none !important;
                border-radius: 12px !important;
                padding: 12px 24px !important;
                transition: all 0.3s ease !important;
            }

            button[kind="primary"]:hover {
                transform: translateY(-2px) !important;
                box-shadow: 0 8px 20px rgba(0, 174, 239, 0.4) !important;
            }

            button[kind="primary"]:active {
                transform: translateY(0) !important;
            }

            /* ========================================
               8. DATA TABLE
               ======================================== */
            
            [data-testid="stDataFrame"] {
                border: 1px solid rgba(255, 255, 255, 0.1) !important;
                border-radius: 12px !important;
                overflow: hidden !important;
            }

            [data-testid="stDataFrame"] tbody tr {
                border-bottom: 1px solid rgba(255, 255, 255, 0.05);
            }

            [data-testid="stDataFrame"] tbody tr:hover {
                background-color: rgba(0, 174, 239, 0.1) !important;
            }

            [data-testid="stDataFrame"] thead {
                background-color: rgba(0, 57, 93, 0.3);
                border-bottom: 2px solid #00AEEF;
            }

            /* ========================================
               9. ALERTS & MESSAGES
               ======================================== */
            
            div[data-testid="stAlert"] {
                border-radius: 12px !important;
                border: 1px solid rgba(255, 255, 255, 0.1) !important;
            }

            div[data-testid="stAlert"] p {
                color: #E0E7FF !important;
                font-weight: 500;
            }

            /* Success */
            div[data-testid="stAlert"][type="success"] {
                background-color: rgba(74, 222, 128, 0.1) !important;
                border-color: #4ADE80 !important;
            }

            /* Warning */
            div[data-testid="stAlert"][type="warning"] {
                background-color: rgba(250, 204, 21, 0.1) !important;
                border-color: #FACC15 !important;
            }

            /* Error */
            div[data-testid="stAlert"][type="error"] {
                background-color: rgba(220, 38, 38, 0.1) !important;
                border-color: #DC2626 !important;
            }

            /* Info */
            div[data-testid="stAlert"][type="info"] {
                background-color: rgba(0, 174, 239, 0.1) !important;
                border-color: #00AEEF !important;
            }

            /* ========================================
               10. CHART CONTAINERS
               ======================================== */
            
            [data-testid="stPlotlyChart"] > div {
                border-radius: 16px !important;
                background: rgba(255, 255, 255, 0.02) !important;
                border: 1px solid rgba(255, 255, 255, 0.08) !important;
                box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3) !important;
                padding: 16px !important;
                overflow: hidden !important;
            }

            [data-testid="stMatplotlibChart"] > div {
                border-radius: 16px !important;
                background: rgba(255, 255, 255, 0.02) !important;
                border: 1px solid rgba(255, 255, 255, 0.08) !important;
                box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3) !important;
                padding: 16px !important;
            }

            /* ========================================
               11. ANIMATIONS
               ======================================== */
            
            @keyframes fadeInUp {
                from {
                    opacity: 0;
                    transform: translateY(20px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }

            @keyframes slideInLeft {
                from {
                    opacity: 0;
                    transform: translateX(-20px);
                }
                to {
                    opacity: 1;
                    transform: translateX(0);
                }
            }

            @keyframes glowPulse {
                0%, 100% { box-shadow: 0 0 5px rgba(0, 174, 239, 0.2); }
                50% { box-shadow: 0 0 15px rgba(0, 174, 239, 0.5); }
            }

            [data-testid="stMetric"] {
                animation: fadeInUp 0.6s ease-out;
            }

            h2 {
                animation: slideInLeft 0.5s ease-out;
            }

            /* ========================================
               12. SCROLLBAR STYLING
               ======================================== */
            
            ::-webkit-scrollbar {
                width: 8px;
                height: 8px;
            }

            ::-webkit-scrollbar-track {
                background: rgba(0, 0, 0, 0.3);
            }

            ::-webkit-scrollbar-thumb {
                background: #00AEEF;
                border-radius: 4px;
            }

            ::-webkit-scrollbar-thumb:hover {
                background: #0090C8;
            }

            /* ========================================
               13. CODE BLOCKS
               ======================================== */
            
            code {
                background-color: rgba(0, 0, 0, 0.5) !important;
                color: #00AEEF !important;
                border-radius: 6px !important;
                padding: 2px 6px !important;
                font-family: 'Monaco', 'Courier New', monospace !important;
            }

            pre {
                background-color: rgba(0, 0, 0, 0.7) !important;
                border: 1px solid rgba(0, 174, 239, 0.2) !important;
                border-radius: 8px !important;
                padding: 12px !important;
            }

            /* ========================================
               14. LINKS
               ======================================== */
            
            a {
                color: #00AEEF !important;
                text-decoration: none;
                transition: color 0.3s ease;
                font-weight: 500;
            }

            a:hover {
                color: #38BDF8 !important;
                text-decoration: underline;
            }

        </style>
        """,
        unsafe_allow_html=True,
    )


def render_footer():
    """
    Renders the footer with creator links
    """
    st.markdown("---")
    st.markdown(
        """
        <div style="
            text-align: center;
            padding: 30px 20px;
            color: #94A3B8;
            font-size: 0.95rem;
        ">
            <p style="margin-bottom: 15px;">
                Built by Mark Pham, Hoan Nguyen and Gina Nguyen
            </p>
            <div style="display: flex; justify-content: center; gap: 20px; align-items: center;">
                <a href="https://www.linkedin.com/in/minhbphamm/" target="_blank" style="
                    color: #00AEEF;
                    text-decoration: none;
                    font-weight: 600;
                    padding: 8px 16px;
                    border: 1px solid #00AEEF;
                    border-radius: 8px;
                    transition: all 0.3s ease;
                    display: inline-block;
                ">
                    🔗 Connect with Mark
                </a>
                <a href="https://www.linkedin.com/in/hoanng15/" target="_blank" style="
                    color: #00AEEF;
                    text-decoration: none;
                    font-weight: 600;
                    padding: 8px 16px;
                    border: 1px solid #00AEEF;
                    border-radius: 8px;
                    transition: all 0.3s ease;
                    display: inline-block;
                ">
                    🔗 Connect with Hoan
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_header(title, subtitle=""):
    """
    Renders a professional page header
    
    Args:
        title (str): Main title
        subtitle (str): Optional subtitle
    """
    st.markdown(
        f"""
        <div style="margin-bottom: 30px;">
            <h1>{title}</h1>
            {f'<p style="color: #94A3B8; font-size: 1.1rem; margin-top: 10px;">{subtitle}</p>' if subtitle else ''}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_info_box(title, content, icon="ℹ️"):
    """
    Renders a styled info box
    
    Args:
        title (str): Box title
        content (str): Box content (plain text only, no HTML)
        icon (str): Emoji icon
    """
    # Escape HTML special characters
    content_safe = content.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    
    st.markdown(
        f"""
        <div style="background: linear-gradient(145deg, rgba(0, 174, 239, 0.1), rgba(0, 174, 239, 0.05)); border-left: 4px solid #00AEEF; border-radius: 12px; padding: 20px; margin: 15px 0;">
            <div style="font-weight: 600; color: #00AEEF; margin-bottom: 8px; font-size: 1.1rem;">
                {icon} {title}
            </div>
            <div style="color: #CBD5E1; line-height: 1.6;">
                {content_safe}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_kpi_cards(kpi_data):
    """
    Renders KPI cards in a grid
    
    Args:
        kpi_data (list): List of dicts with keys: label, value, icon
    """
    cols = st.columns(len(kpi_data))
    for col, kpi in zip(cols, kpi_data):
        with col:
            st.metric(
                label=f"{kpi.get('icon', '📊')} {kpi['label']}",
                value=kpi['value']
            )


def render_section_divider():
    """Renders a visual section divider"""
    st.markdown(
        """
        <div style="
            margin: 40px 0;
            height: 2px;
            background: linear-gradient(90deg, transparent, #00AEEF, transparent);
            border-radius: 2px;
        "></div>
        """,
        unsafe_allow_html=True,
    )


def render_warning_box(title, content):
    """Renders a styled warning box"""
    content_safe = content.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    
    st.markdown(
        f"""
        <div style="background: linear-gradient(145deg, rgba(250, 204, 21, 0.1), rgba(250, 204, 21, 0.05)); border-left: 4px solid #FACC15; border-radius: 12px; padding: 20px; margin: 15px 0;">
            <div style="font-weight: 600; color: #FACC15; margin-bottom: 8px; font-size: 1.1rem;">
                ⚠️ {title}
            </div>
            <div style="color: #CBD5E1; line-height: 1.6;">
                {content_safe}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_success_box(title, content):
    """Renders a styled success box"""
    content_safe = content.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    
    st.markdown(
        f"""
        <div style="background: linear-gradient(145deg, rgba(74, 222, 128, 0.1), rgba(74, 222, 128, 0.05)); border-left: 4px solid #4ADE80; border-radius: 12px; padding: 20px; margin: 15px 0;">
            <div style="font-weight: 600; color: #4ADE80; margin-bottom: 8px; font-size: 1.1rem;">
                ✅ {title}
            </div>
            <div style="color: #CBD5E1; line-height: 1.6;">
                {content_safe}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_logo_header(image_path, app_name, creator=""):
    """
    Renders a professional logo + header
    
    Args:
        image_path (str): Path to logo image (not used, kept for compatibility)
        app_name (str): Application name
        creator (str): Creator name/link (not used, kept for compatibility)
    """
    st.markdown(
        f"""
        <div style="margin-bottom: 30px;">
            <h1>{app_name}</h1>
            <p style="color: #94A3B8; font-size: 1.1rem; margin-top: 10px;">
                Built by <strong style="color: #00AEEF; font-size: 1.2rem;">Mark Pham</strong> and <strong style="color: #00AEEF; font-size: 1.2rem;">Hoan Nguyen</strong>
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )