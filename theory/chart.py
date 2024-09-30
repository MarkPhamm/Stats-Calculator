import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from scipy.stats import gaussian_kde

def create_histogram():
    n_points = st.slider("Number of data points:", 100, 5000, 1000, key="hist_n_points")
    bins = st.slider("Number of bins:", 5, 50, 20, key="hist_bins")
    n_categories = st.slider("Number of categories:", 1, 3, 2, key="hist_n_categories")
    
    np.random.seed(42)
    categories = [f'Category {i}' for i in range(1, n_categories + 1)]
    df = pd.DataFrame({
        'Value': np.random.randn(n_points),
        'Category': np.random.choice(categories, size=n_points)
    })
    
    fig = px.histogram(df, x='Value', color='Category', nbins=bins, 
                       title=f"Histogram of {n_points} Random Data Points across {n_categories} Categories")
    st.plotly_chart(fig)

def create_box_plot():
    n_points = st.slider("Number of data points for box plot:", 100, 5000, 1000, key="box_n_points")
    n_categories = st.slider("Number of categories:", 2, 5, 3, key="box_n_categories")
    
    np.random.seed(42)
    categories = [f'Category {i}' for i in range(1, n_categories + 1)]
    df = pd.DataFrame({
        'Category': np.random.choice(categories, size=n_points),
        'Value': np.random.randn(n_points)
    })
    
    fig = px.box(df, x='Category', y='Value', color='Category', 
                 title=f"Box Plot with {n_points} Random Data Points and {n_categories} Categories")
    st.plotly_chart(fig)

def create_line_histogram():
    n_points = st.slider("Number of data points:", 100, 5000, 1000, key="line_hist_n_points")
    n_categories = st.slider("Number of categories:", 1, 3, 2, key="line_hist_n_categories")
    
    np.random.seed(42)
    categories = [f'Category {i}' for i in range(1, n_categories + 1)]
    df = pd.DataFrame({
        'Value': np.random.randn(n_points),
        'Category': np.random.choice(categories, size=n_points)
    })
    
    def smooth_data(data):
        kde = gaussian_kde(data, bw_method='scott')
        x = np.linspace(min(data), max(data), 1000)
        return x, kde.evaluate(x)
    
    fig = go.Figure()
    for category in df['Category'].unique():
        x, y = smooth_data(df[df['Category'] == category]['Value'])
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=category))
    
    fig.update_layout(
        title=f"Smoothed Line Histogram of {n_points} Data Points across {n_categories} Categories",
        xaxis_title="Value",
        yaxis_title="Density"
    )
    st.plotly_chart(fig)

def create_bar_chart():
    n_points = st.slider("Number of data points:", 100, 5000, 1000, key="bar_n_points")
    n_categories = st.slider("Number of categories:", 1, 5, 3, key="bar_n_categories")
    
    np.random.seed(42)
    df = pd.DataFrame({
        'Category': [f'Category {i}' for i in range(1, n_categories + 1)],
        'Value': np.random.randint(10, 100, size=n_categories)
    })
    
    fig = px.bar(df, x='Category', y='Value', 
                 title=f"Bar Chart of {n_points} Random Data Points across {n_categories} Categories",
                 text='Value', color='Category')
    
    fig.update_layout(xaxis_title="Category", yaxis_title="Value", xaxis_tickangle=-45)
    st.plotly_chart(fig)

def create_line_chart():
    n_points = st.slider("Number of data points:", 5, 20, 10, key="line_n_points")
    n_categories = st.slider("Number of categories:", 1, 5, 3, key="line_n_categories")
    
    np.random.seed(42)
    categories = [f'Category {i}' for i in range(1, n_categories + 1)]
    df = pd.DataFrame({
        'X': np.tile(np.arange(n_points), n_categories),
        'Y': np.random.randn(n_points * n_categories),
        'Category': np.repeat(categories, n_points)
    })
    
    fig = px.line(df, x='X', y='Y', color='Category', 
                  title=f"Line Chart of {n_points} Random Data Points across {n_categories} Categories")
    
    fig.update_layout(xaxis_title="X-axis", yaxis_title="Y-axis")
    st.plotly_chart(fig)

def create_pie_chart():
    n_categories = st.slider("Number of categories:", 2, 5, 3, key="pie_n_categories")
    
    np.random.seed(42)
    df = pd.DataFrame({
        'Category': [f'Category {i}' for i in range(1, n_categories + 1)],
        'Value': np.random.randint(1, 100, size=n_categories)
    })
    
    fig = px.pie(df, names='Category', values='Value', title=f"Pie Chart with {n_categories} Categories")
    st.plotly_chart(fig)

def create_donut_chart():
    n_categories = st.slider("Number of categories:", 2, 10, 3, key="donut_n_categories")
    center_metric = st.text_input("Metric for the center:", "Total")
    
    np.random.seed(42)
    df = pd.DataFrame({
        'Category': [f'Category {i}' for i in range(1, n_categories + 1)],
        'Value': np.random.randint(1, 100, size=n_categories)
    })
    
    total_value = df['Value'].sum()
    
    fig = px.pie(df, names='Category', values='Value', 
                 hole=0.4,
                 title=f"Donut Chart with {n_categories} Categories\n{center_metric}: {total_value}")
    
    fig.update_layout(
        annotations=[dict(text=f"<b>{center_metric}: {total_value}</b>", 
                          x=0.5, y=0.5, 
                          font_size=20, 
                          showarrow=False,
                          font_color='white')]
    )
    
    st.plotly_chart(fig)

def create_stacked_bar_chart():
    n_categories = st.slider("Number of categories:", 2, 10, 5, key="stacked_bar_n_categories")
    n_series = st.slider("Number of series:", 2, 5, 3, key="stacked_bar_n_series")
    
    np.random.seed(42)
    df = pd.DataFrame({
        'Category': np.repeat([f'Category {i}' for i in range(1, n_categories + 1)], n_series),
        'Series': np.tile([f'Series {i}' for i in range(1, n_series + 1)], n_categories),
        'Value': np.random.randint(1, 100, size=n_categories * n_series)
    })
    
    fig = px.bar(df, x='Category', y='Value', color='Series', 
                 title=f"Stacked Bar Chart with {n_categories} Categories and {n_series} Series",
                 labels={'Value': 'Value'},
                 height=400)
    
    st.plotly_chart(fig)

def create_scatter_plot():
    n_points = st.slider("Number of data points:", 50, 1000, 200, key="scatter_n_points")
    n_categories = st.slider("Number of categories:", 1, 5, 3, key="scatter_n_categories")
    
    np.random.seed(42)
    categories = [f'Category {i}' for i in range(1, n_categories + 1)]
    df = pd.DataFrame({
        'X': np.random.randn(n_points),
        'Y': np.random.randn(n_points),
        'Category': np.random.choice(categories, size=n_points)
    })
    
    fig = px.scatter(df, x='X', y='Y', color='Category', 
                     title=f"Scatter Plot with {n_points} Data Points and {n_categories} Categories",
                     labels={'X': 'X Axis', 'Y': 'Y Axis'},
                     height=400)
    
    st.plotly_chart(fig)

def create_bubble_chart():
    n_points = st.slider("Number of data points:", 50, 1000, 200, key="bubble_n_points")
    n_categories = st.slider("Number of categories:", 1, 5, 3, key="bubble_n_categories")
    
    np.random.seed(42)
    categories = [f'Category {i}' for i in range(1, n_categories + 1)]
    df = pd.DataFrame({
        'X': np.random.randn(n_points),
        'Y': np.random.randn(n_points),
        'Size': np.random.rand(n_points) * 100,
        'Category': np.random.choice(categories, size=n_points)
    })
    
    fig = px.scatter(df, x='X', y='Y', size='Size', color='Category', 
                     title=f"Bubble Chart with {n_points} Data Points and {n_categories} Categories",
                     labels={'X': 'X Axis', 'Y': 'Y Axis', 'Size': 'Bubble Size'},
                     height=400)
    
    st.plotly_chart(fig)

def main():
    st.title("Chart Types & Usages")
    st.write("""
        Explore different types of charts categorized into four sections: Distribution, Comparison, Composition, and Relationships. 
        Each section provides examples and tips for choosing the right chart based on your data and the story you want to tell.
    """)
    st.image('theory/charts.png')

    st.header("1. Distribution Charts")
    st.write("Distribution charts show how data is spread over a range of values, helping you understand frequency, variation, and central tendency.")

    st.subheader("1.1. Histogram")
    st.write("Use a histogram to display the distribution of a single continuous variable. It's useful for identifying patterns like skewness or outliers.")
    create_histogram()

    st.subheader("1.2. Box Plot")
    st.write("A box plot helps you visualize the spread and identify outliers in your data. It's good for comparing distributions across different categories.")
    create_box_plot()

    st.subheader("1.3. Line Histogram")
    st.write("Use a line histogram to display the distribution of a single continuous variable with a density plot. It's useful for visualizing the shape of the distribution and comparing distributions across different categories.")
    create_line_histogram()

    st.header("2. Comparison Charts")
    st.write("Comparison charts are used to compare different groups or trends over time. They highlight differences and similarities between datasets.")

    st.subheader("2.1 Bar Chart")
    st.write("Use a bar chart to compare different categories or groups. This is ideal for comparing discrete items or categorical data.")
    create_bar_chart()

    st.subheader("2.2. Line Chart")
    st.write("A line chart is used to visualize trends over time. It's great for showing changes and patterns in continuous data.")
    create_line_chart()

    st.header("3. Composition Charts")
    st.write("Composition charts show how different parts make up a whole. They help you see the proportion of components within a dataset.")

    st.subheader("3.1. Pie Chart")
    st.write("A pie chart shows the relative size of parts to a whole. It's effective for showing proportions, but avoid using it for too many categories (<=5).")
    create_pie_chart()

    st.subheader("3.2. Donut Chart")
    st.write("A donut chart is similar to a pie chart but has a hole in the middle. This design allows for additional metrics or information to be displayed in the center of the donut. While both charts show proportions, the donut chart can provide more context by incorporating additional details in the center.")
    create_donut_chart()

    st.subheader("3.3. Stacked Bar Chart")
    st.write("A stacked bar chart shows the total value of different categories while also indicating the proportion of each subcategory within the whole.")
    create_stacked_bar_chart()

    st.header("4. Relationship Charts")
    st.write("Relationship charts are designed to show connections or correlations between variables. They help you understand how one variable affects another.")

    st.subheader("4.1 Scatter Plot")
    st.write("A scatter plot is used to show the relationship between two continuous variables. It's helpful for spotting correlations or clusters.")
    create_scatter_plot()

    st.subheader("4.2. Bubble Chart")
    st.write("A bubble chart is a variation of a scatter plot where the size of the bubbles represents a third variable. It's useful for adding more dimensions to the analysis.")
    create_bubble_chart()

    st.write("By understanding the differences between these chart types, you can choose the right chart for your data and convey your insights more effectively.")

if __name__ == "__main__":
    main()