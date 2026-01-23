import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import utils

# Page Configuration
st.set_page_config(
    page_title="Data Exploration",
    page_icon="🔍",
    layout="wide",
    menu_items={
        'Get Help': 'https://www.linkedin.com/in/minhbphamm/',
        'Report a bug': "https://www.linkedin.com/in/minhbphamm/",
        'About': "# Comprehensive Statistics Calculator"
    }
)

# Apply custom CSS if utility exists
try:
    utils.add_custom_css()
except AttributeError:
    pass

# ==========================================
# PAGE HEADER
# ==========================================
utils.render_header(
    title="🔍 Exploratory Data Analysis (EDA)",
    subtitle="Upload your dataset to automatically generate summary statistics and visualizations"
)

# ==========================================
# INFO BOX
# ==========================================
utils.render_info_box(
    title="What is EDA?",
    content="Exploratory Data Analysis is the process of analyzing datasets to understand their main characteristics, patterns, and anomalies. This tool provides automatic summaries, statistical overviews, correlation analysis, and missing value detection.",
    icon="📊"
)

# ==========================================
# MAIN CONTENT
# ==========================================

# File Uploader with styled container
st.markdown("### 📁 Upload Your Data")

uploaded_file = st.file_uploader(
    "Upload a CSV file to begin analysis",
    type=["csv"],
    help="Select a CSV file from your computer"
)

if uploaded_file is not None:
    try:
        # Load Data
        df = pd.read_csv(uploaded_file)
        
        success_msg = f"Dataset: {uploaded_file.name} ({df.shape[0]} rows, {df.shape[1]} columns)"
        utils.render_success_box(
            title="File Loaded Successfully",
            content=success_msg
        )

        # ==========================================
        # SECTION 1: DATA OVERVIEW
        # ==========================================
        st.markdown("### 📊 1. Data Overview")
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("📈 Total Rows", f"{df.shape[0]:,}")
        with col2:
            st.metric("📋 Total Columns", f"{df.shape[1]}")
        with col3:
            missing_count = df.isna().sum().sum()
            st.metric("❌ Missing Values", f"{missing_count:,}")
        with col4:
            numeric_count = df.select_dtypes(include=['float64', 'int64']).shape[1]
            st.metric("🔢 Numeric Columns", f"{numeric_count}")

        with st.expander("📋 View First 10 Rows", expanded=False):
            st.dataframe(df.head(10), use_container_width=True)

        with st.expander("📚 Column Information", expanded=False):
            col_info = pd.DataFrame({
                'Column': df.columns,
                'Type': df.dtypes.astype(str),
                'Non-Null': df.notna().sum().values,
                'Null': df.isna().sum().values,
                'Unique': df.nunique().values
            })
            st.dataframe(col_info, use_container_width=True)

        utils.render_section_divider()

        # ==========================================
        # SECTION 2: DESCRIPTIVE STATISTICS
        # ==========================================
        st.markdown("### 📊 2. Descriptive Statistics")
        
        st.write("Summary statistics for numerical columns:")
        
        numeric_df = df.select_dtypes(include=['float64', 'int64'])
        if not numeric_df.empty:
            stats_df = numeric_df.describe().T
            stats_df = stats_df[['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']]
            st.dataframe(stats_df, use_container_width=True)
        else:
            utils.render_warning_box(
                title="No Numeric Data",
                content="Your dataset contains no numerical columns. Descriptive statistics are only calculated for numeric data."
            )

        utils.render_section_divider()

        # ==========================================
        # SECTION 3: CORRELATION ANALYSIS
        # ==========================================
        st.markdown("### 🔗 3. Correlation Matrix")
        st.write("Analyze the relationship between numerical variables.")
        
        # Filter only numeric columns for correlation
        numeric_df = df.select_dtypes(include=['float64', 'int64'])
        
        if not numeric_df.empty:
            # Calculate correlation
            corr = numeric_df.corr()
            
            # Create two columns for better layout
            col1, col2 = st.columns([1, 2])
            
            with col1:
                st.markdown("#### Correlation Statistics")
                st.write(f"Variables analyzed: {corr.shape[0]}")
                
                # Find highest correlations (excluding 1.0)
                corr_pairs = []
                for i in range(len(corr.columns)):
                    for j in range(i+1, len(corr.columns)):
                        corr_pairs.append({
                            'Var1': corr.columns[i],
                            'Var2': corr.columns[j],
                            'Correlation': corr.iloc[i, j]
                        })
                
                if corr_pairs:
                    corr_pairs_df = pd.DataFrame(corr_pairs)
                    corr_pairs_df['Abs_Corr'] = corr_pairs_df['Correlation'].abs()
                    top_corr = corr_pairs_df.nlargest(5, 'Abs_Corr')[['Var1', 'Var2', 'Correlation']]
                    
                    st.write("**Top 5 Correlations:**")
                    for idx, row in top_corr.iterrows():
                        st.write(f"• {row['Var1']} ↔ {row['Var2']}: **{row['Correlation']:.3f}**")
            
            with col2:
                # Plot Heatmap
                fig, ax = plt.subplots(figsize=(10, 8))
                sns.heatmap(
                    corr,
                    annot=True,
                    cmap='coolwarm',
                    fmt=".2f",
                    ax=ax,
                    linewidths=0.5,
                    cbar_kws={'label': 'Correlation'}
                )
                ax.set_title("Correlation Heatmap", fontsize=14, fontweight='bold', pad=20)
                plt.tight_layout()
                st.pyplot(fig)
        else:
            utils.render_warning_box(
                title="No Numeric Data",
                content="Correlation analysis requires numerical columns. Your dataset may only contain categorical data."
            )

        utils.render_section_divider()

        # ==========================================
        # SECTION 4: MISSING VALUES ANALYSIS
        # ==========================================
        st.markdown("### 🔍 4. Missing Values Analysis")
        
        missing_data = df.isna().sum()
        missing_data = missing_data[missing_data > 0].sort_values(ascending=False)
        
        if not missing_data.empty:
            col1, col2 = st.columns([1, 2])
            
            with col1:
                st.markdown("#### Missing Value Summary")
                total_cells = df.shape[0] * df.shape[1]
                total_missing = missing_data.sum()
                missing_percentage = (total_missing / total_cells) * 100
                
                st.metric("Total Missing Cells", f"{total_missing:,}")
                st.metric("Missing Percentage", f"{missing_percentage:.2f}%")
                
                st.markdown("#### Affected Columns")
                for col, count in missing_data.items():
                    pct = (count / df.shape[0]) * 100
                    st.write(f"• **{col}**: {count} ({pct:.1f}%)")
            
            with col2:
                # Create bar chart
                fig, ax = plt.subplots(figsize=(10, 6))
                missing_data.plot(kind='barh', ax=ax, color='#FF6B6B', edgecolor='black')
                ax.set_xlabel('Count of Missing Values', fontsize=12, fontweight='bold')
                ax.set_ylabel('Columns', fontsize=12, fontweight='bold')
                ax.set_title('Missing Values by Column', fontsize=14, fontweight='bold', pad=20)
                plt.tight_layout()
                st.pyplot(fig)
        else:
            utils.render_success_box(
                title="No Missing Values Found",
                content="Your dataset is complete with no missing values across all columns!"
            )

        utils.render_section_divider()

        # ==========================================
        # SECTION 5: DISTRIBUTION ANALYSIS
        # ==========================================
        st.markdown("### 📈 5. Distribution Analysis")
        
        numeric_df = df.select_dtypes(include=['float64', 'int64'])
        
        if not numeric_df.empty:
            selected_column = st.selectbox(
                "Select a numeric column to visualize its distribution",
                numeric_df.columns,
                key="dist_col"
            )
            
            col1, col2 = st.columns(2)
            
            with col1:
                fig, ax = plt.subplots(figsize=(8, 5))
                numeric_df[selected_column].hist(bins=30, ax=ax, color='#00AEEF', edgecolor='black', alpha=0.7)
                ax.set_title(f'Distribution of {selected_column}', fontsize=12, fontweight='bold')
                ax.set_xlabel('Value')
                ax.set_ylabel('Frequency')
                plt.tight_layout()
                st.pyplot(fig)
            
            with col2:
                fig, ax = plt.subplots(figsize=(8, 5))
                numeric_df[selected_column].plot(kind='box', ax=ax, vert=True)
                ax.set_title(f'Box Plot of {selected_column}', fontsize=12, fontweight='bold')
                ax.set_ylabel('Value')
                plt.tight_layout()
                st.pyplot(fig)
        else:
            utils.render_warning_box(
                title="No Numeric Columns",
                content="Distribution analysis requires numeric columns."
            )

        utils.render_section_divider()

        # ==========================================
        # SECTION 6: DATA QUALITY REPORT
        # ==========================================
        st.markdown("### 📋 6. Data Quality Report")
        
        quality_metrics = {
            'Completeness': f"{((total_cells - total_missing) / total_cells * 100):.2f}%",
            'Duplicate Rows': df.duplicated().sum(),
            'Unique Values Ratio': f"{df.nunique().sum() / df.shape[1]:.2f}",
        }
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("✅ Data Completeness", quality_metrics['Completeness'])
        with col2:
            st.metric("⚠️ Duplicate Rows", quality_metrics['Duplicate Rows'])
        with col3:
            st.metric("🔢 Avg Unique Values", quality_metrics['Unique Values Ratio'])

    except Exception as e:
        error_msg = f"An error occurred: {str(e)}"
        utils.render_warning_box(
            title="Error Processing File",
            content=error_msg
        )
else:
    # Default state when no file is uploaded
    st.markdown(
        """
        <div style="
            text-align: center;
            padding: 80px 20px;
            background: linear-gradient(145deg, rgba(0, 174, 239, 0.05), rgba(0, 174, 239, 0.02));
            border: 2px dashed #00AEEF;
            border-radius: 16px;
            margin: 40px 0;
        ">
            <div style="font-size: 4rem; margin-bottom: 20px;">📁</div>
            <h3 style="color: #E0E7FF; border-left: none; margin-top: 0;">No file uploaded yet</h3>
            <p style="color: #94A3B8; font-size: 1.1rem; max-width: 600px; margin: 0 auto;">
                Upload a CSV file above to begin your exploratory data analysis. 
                Get instant insights about your data including descriptive statistics, 
                correlations, missing values, and more!
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ==========================================
# FOOTER
# ==========================================
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: #94A3B8; font-size: 0.9rem; margin-top: 30px;">
        <p>Tip: Use this tool to understand your data before building models or performing statistical tests.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

utils.render_footer()