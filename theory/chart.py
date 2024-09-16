import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from scipy.stats import gaussian_kde

import os
import sys

def create_histogram():
    # Let the user specify the number of data points
    n_points = st.slider("Select number of data points:", min_value=100, max_value=5000, value=1000, key="hist_n_points")
    
    # Let the user specify the number of bins
    bins = st.slider("Select number of bins:", min_value=5, max_value=50, value=20, key="hist_bins")
    
    # Let the user specify the number of categories
    n_categories = st.slider("Select number of categories:", min_value=1, max_value=3, value=2, key="hist_n_categories")
    
    # Generate random data
    np.random.seed(42)
    categories = np.random.choice([f'Category {i}' for i in range(1, n_categories + 1)], size=n_points)
    values = np.random.randn(n_points)
    
    # Create a DataFrame
    df = pd.DataFrame({'Value': values, 'Category': categories})
    
    # Create a histogram with Plotly
    fig = px.histogram(df, x='Value', color='Category', nbins=bins, 
                       title=f"Histogram of {n_points} Random Data Points across {n_categories} Categories")
    
    # Display the Plotly histogram
    st.plotly_chart(fig)

# Function to generate box plot
def create_box_plot():
    # Let the user specify the number of data points
    n_points = st.slider("Select number of data points for box plot:", min_value=100, max_value=5000, value=1000, key="box_n_points")
    
    # Let the user specify the number of categories
    n_categories = st.slider("Select number of categories:", min_value=2, max_value=5, value=3, key="box_n_categories")
    
    # Generate random data
    np.random.seed(42)
    categories = np.random.choice([f'Category {i}' for i in range(1, n_categories + 1)], size=n_points)
    values = np.random.randn(n_points)
    
    # Create a DataFrame
    df = pd.DataFrame({'Category': categories, 'Value': values})
    
    # Create a box plot with Plotly, coloring by category
    fig = px.box(df, x='Category', y='Value', color='Category', 
                 title=f"Box Plot with {n_points} Random Data Points and {n_categories} Categories")
    
    # Display the Plotly box plot
    st.plotly_chart(fig)

def create_line_histogram():
    # Let the user specify the number of data points
    n_points = st.slider("Select number of data points:", min_value=100, max_value=5000, value=1000, key="line_hist_n_points")
    
    # Let the user specify the number of bins
    n_categories = st.slider("Select number of categories:", min_value=1, max_value=3, value=2, key="line_hist_n_categories")
    
    # Generate random data
    np.random.seed(42)
    categories = np.random.choice([f'Category {i}' for i in range(1, n_categories + 1)], size=n_points)
    values = np.random.randn(n_points)
    
    # Create a DataFrame
    df = pd.DataFrame({'Value': values, 'Category': categories})
    
    # Define a function to smooth data using Gaussian KDE
    def smooth_data(data):
        kde = gaussian_kde(data, bw_method='scott')
        x = np.linspace(min(data), max(data), 1000)
        y = kde.evaluate(x)
        return x, y
    
    # Plotting data for each category
    fig = go.Figure()
    for category in df['Category'].unique():
        category_data = df[df['Category'] == category]['Value']
        x, y = smooth_data(category_data)
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=category))
    
    # Update layout
    fig.update_layout(title=f"Smoothed Line Histogram of {n_points} Data Points across {n_categories} Categories",
                      xaxis_title="Value",
                      yaxis_title="Density")
    
    # Display the Plotly line histogram
    st.plotly_chart(fig)

def create_bar_chart():
    # Let the user specify the number of data points
    n_points = st.slider("Select number of data points:", min_value=100, max_value=5000, value=1000, key="bar_n_points")

    # Let the user specify the number of categories
    n_categories = st.slider("Select number of categories:", min_value=1, max_value=5, value=3, key="bar_n_categories")
    
    # Generate random data
    np.random.seed(42)
    categories = [f'Category {i}' for i in range(1, n_categories + 1)]
    values = np.random.randint(10, 100, size=n_categories)
    
    # Create a DataFrame
    df = pd.DataFrame({'Category': categories, 'Value': values})
    
    # Create a bar chart with Plotly
    fig = px.bar(df, x='Category', y='Value', 
                 title=f"Bar Chart of {n_points} Random Data Points across {n_categories} Categories",
                 text='Value',  color='Category')
    
    # Update layout
    fig.update_layout(xaxis_title="Category",
                      yaxis_title="Value",
                      xaxis_tickangle=-45)
    
    # Display the Plotly bar chart
    st.plotly_chart(fig)

def create_line_chart():
    # Let the user specify the number of data points
    n_points = st.slider("Select number of data points:", min_value=5, max_value=20, value=10, key="line_n_points")

    # Let the user specify the number of categories
    n_categories = st.slider("Select number of categories:", min_value=1, max_value=5, value=3, key="line_n_categories")
    
    # Generate random data
    np.random.seed(42)
    x = np.arange(n_points)
    categories = [f'Category {i}' for i in range(1, n_categories + 1)]
    
    # Create a DataFrame
    df = pd.DataFrame({
        'X': np.tile(x, n_categories),
        'Y': np.random.randn(n_points * n_categories),
        'Category': np.repeat(categories, n_points)
    })
    
    # Create a line chart with Plotly
    fig = px.line(df, x='X', y='Y', color='Category', 
                  title=f"Line Chart of {n_points} Random Data Points across {n_categories} Categories")
    
    # Update layout
    fig.update_layout(xaxis_title="X-axis",
                      yaxis_title="Y-axis")
    
    # Display the Plotly line chart
    st.plotly_chart(fig)

def create_pie_chart():
    # Let the user specify the number of categories
    n_categories = st.slider("Select number of categories:", min_value=2, max_value=5, value=3, key="pie_n_categories")
    
    # Generate random data
    np.random.seed(42)
    categories = [f'Category {i}' for i in range(1, n_categories + 1)]
    values = np.random.randint(1, 100, size=n_categories)
    
    # Create a DataFrame
    df = pd.DataFrame({'Category': categories, 'Value': values})
    
    # Create a pie chart with Plotly
    fig = px.pie(df, names='Category', values='Value', title=f"Pie Chart with {n_categories} Categories")
    
    # Display the Plotly pie chart
    st.plotly_chart(fig)

def create_donut_chart():
    # Let the user specify the number of categories
    n_categories = st.slider("Select number of categories:", min_value=2, max_value=10, value=3, key="donut_n_categories")
    
    # Let the user specify the metric to display in the center
    center_metric = st.text_input("Enter metric for the center:", "Total")
    
    # Generate random data
    np.random.seed(42)
    categories = [f'Category {i}' for i in range(1, n_categories + 1)]
    values = np.random.randint(1, 100, size=n_categories)
    
    # Create a DataFrame
    df = pd.DataFrame({'Category': categories, 'Value': values})
    
    # Calculate the metric value for the center
    total_value = df['Value'].sum()
    
    # Create a donut chart with Plotly
    fig = px.pie(df, names='Category', values='Value', 
                 hole=0.4,  # Create a donut chart
                 title=f"Donut Chart with {n_categories} Categories\n{center_metric}: {total_value}")
    
    # Update layout to change the color of the center metric
    fig.update_layout(
        annotations=[dict(text=f"<b>{center_metric}: {total_value}</b>", 
                          x=0.5, y=0.5, 
                          font_size=20, 
                          showarrow=False,
                          font_color='white')]
    )
    
    # Display the Plotly donut chart
    st.plotly_chart(fig)

def create_donut_chart():
    # Let the user specify the number of categories
    n_categories = st.slider("Select number of categories:", min_value=2, max_value=5, value=3, key="donut_n_categories")
    
    # Let the user specify the metric to display in the center
    center_metric = st.text_input("Enter metric for the center:", "Total")
    
    # Generate random data
    np.random.seed(42)
    categories = [f'Category {i}' for i in range(1, n_categories + 1)]
    values = np.random.randint(1, 100, size=n_categories)
    
    # Create a DataFrame
    df = pd.DataFrame({'Category': categories, 'Value': values})
    
    # Calculate the metric value for the center
    total_value = df['Value'].sum()
    
    # Create a donut chart with Plotly
    fig = px.pie(df, names='Category', values='Value', 
                 hole=0.4,  # Create a donut chart
                 title=f"Donut Chart with {n_categories} Categories\n{center_metric}: {total_value}")
    
    # Update layout to change the color of the center metric
    fig.update_layout(
        annotations=[dict(text=f"<b>{center_metric}: {total_value}</b>", 
                          x=0.5, y=0.5, 
                          font_size=20, 
                          showarrow=False,
                          font_color='white')]
    )
    
    # Display the Plotly donut chart
    st.plotly_chart(fig)

def create_stacked_bar_chart():
    # Let the user specify the number of categories and series
    n_categories = st.slider("Select number of categories:", min_value=2, max_value=10, value=5, key="stacked_bar_n_categories")
    n_series = st.slider("Select number of series:", min_value=2, max_value=5, value=3, key="stacked_bar_n_series")
    
    # Generate random data
    np.random.seed(42)
    categories = [f'Category {i}' for i in range(1, n_categories + 1)]
    series = [f'Series {i}' for i in range(1, n_series + 1)]
    
    # Create random values for each series and category
    data = {
        'Category': np.repeat(categories, n_series),
        'Series': np.tile(series, n_categories),
        'Value': np.random.randint(1, 100, size=n_categories * n_series)
    }
    
    # Create a DataFrame
    df = pd.DataFrame(data)
    
    # Create a stacked bar chart with Plotly
    fig = px.bar(df, x='Category', y='Value', color='Series', 
                 title=f"Stacked Bar Chart with {n_categories} Categories and {n_series} Series",
                 labels={'Value': 'Value'},
                 height=400)
    
    # Display the Plotly stacked bar chart
    st.plotly_chart(fig)

def create_scatter_plot():
    # Let the user specify the number of data points
    n_points = st.slider("Select number of data points:", min_value=50, max_value=1000, value=200, key="scatter_n_points")
    
    # Let the user specify the number of categories
    n_categories = st.slider("Select number of categories:", min_value=1, max_value=5, value=3, key="scatter_n_categories")
    
    # Generate random data
    np.random.seed(42)
    categories = [f'Category {i}' for i in range(1, n_categories + 1)]
    x_values = np.random.randn(n_points)
    y_values = np.random.randn(n_points)
    category_labels = np.random.choice(categories, size=n_points)
    
    # Create a DataFrame
    df = pd.DataFrame({'X': x_values, 'Y': y_values, 'Category': category_labels})
    
    # Create a scatter plot with Plotly
    fig = px.scatter(df, x='X', y='Y', color='Category', 
                     title=f"Scatter Plot with {n_points} Data Points and {n_categories} Categories",
                     labels={'X': 'X Axis', 'Y': 'Y Axis'},
                     height=400)
    
    # Display the Plotly scatter plot
    st.plotly_chart(fig)

def create_bubble_chart():
    # Let the user specify the number of data points
    n_points = st.slider("Select number of data points:", min_value=50, max_value=1000, value=200, key="bubble_n_points")
    
    # Let the user specify the number of categories
    n_categories = st.slider("Select number of categories:", min_value=1, max_value=5, value=3, key="bubble_n_categories")
    
    # Generate random data
    np.random.seed(42)
    categories = [f'Category {i}' for i in range(1, n_categories + 1)]
    x_values = np.random.randn(n_points)
    y_values = np.random.randn(n_points)
    sizes = np.random.rand(n_points) * 100  # Bubble sizes
    category_labels = np.random.choice(categories, size=n_points)
    
    # Create a DataFrame
    df = pd.DataFrame({'X': x_values, 'Y': y_values, 'Size': sizes, 'Category': category_labels})
    
    # Create a bubble chart with Plotly
    fig = px.scatter(df, x='X', y='Y', size='Size', color='Category', 
                     title=f"Bubble Chart with {n_points} Data Points and {n_categories} Categories",
                     labels={'X': 'X Axis', 'Y': 'Y Axis', 'Size': 'Bubble Size'},
                     height=400)
    
    # Display the Plotly bubble chart
    st.plotly_chart(fig)

def main():
    # Title and Introduction
    st.title("Chart Types & Usages")
    st.write("""
        Explore different types of charts categorized into four sections: Distribution, Comparison, Composition, and Relationships. 
        Each section provides examples and tips for choosing the right chart based on your data and the story you want to tell.
    """)
    st.image('charts.png')

    # Distribution Section
    st.header("1. Distribution Charts")
    st.write("""
        Distribution charts are useful for showing how data is spread over a range of values. These charts help you understand the frequency, variation, and central tendency.
    """)

    st.subheader("1.1. Histogram")
    st.write("Use a histogram to display the distribution of a single continuous variable. It’s useful for identifying patterns like skewness or outliers.")
    create_histogram()

    st.subheader("1.2. Box Plot")
    st.write("A box plot helps you visualize the spread and identify outliers in your data. It's good for comparing distributions across different categories.")
    create_box_plot()

    st.subheader("1.3. Line Histogram")
    st.write("Use a line histogram to display the distribution of a single continuous variable with a density plot. It’s useful for visualizing the shape of the distribution and comparing distributions across different categories.")
    create_line_histogram()

    # Comparison Section
    st.header("2. Comparison Charts")
    st.write("""
        Comparison charts are used to compare different groups or trends over time. They highlight differences and similarities between datasets.
    """)

    st.subheader("2.1 Bar Chart")
    st.write("Use a bar chart to compare different categories or groups. This is ideal for comparing discrete items or categorical data.")
    create_bar_chart()

    st.subheader("2.2. Line Chart")
    st.write("A line chart is used to visualize trends over time. It's great for showing changes and patterns in continuous data.")
    create_line_chart()

    # Composition Section
    st.header("3. Composition Charts")
    st.write("""
        Composition charts show how different parts make up a whole. They help you see the proportion of components within a dataset.
    """)
    st.subheader("3.1. Pie Chart")
    st.write("A pie chart shows the relative size of parts to a whole. It's effective for showing proportions, but avoid using it for too many categories (<=5).")
    create_pie_chart()

    st.subheader("3.2. Donut Chart")
    st.write("A donut chart is similar to a pie chart but has a hole in the middle. This design allows for additional metrics or information to be displayed in the center of the donut. While both charts show proportions, the donut chart can provide more context by incorporating additional details in the center.")
    create_donut_chart()

    st.subheader("3.3. Stacked Bar Chart")
    st.write("A stacked bar chart shows the total value of different categories while also indicating the proportion of each subcategory within the whole.")
    create_stacked_bar_chart()

    # Relationships Section
    st.header("4. Relationship Charts")
    st.write("""
        Relationship charts are designed to show connections or correlations between variables. They help you understand how one variable affects another.
    """)
    st.subheader("4.1 Scatter Plot")
    st.write("A scatter plot is used to show the relationship between two continuous variables. It’s helpful for spotting correlations or clusters.")
    create_scatter_plot()

    st.subheader("4.2. Bubble Chart")
    st.write("A bubble chart is a variation of a scatter plot where the size of the bubbles represents a third variable. It’s useful for adding more dimensions to the analysis.")
    create_bubble_chart()

    # Footer
    st.write("""
        By understanding the differences between these chart types, you can choose the right chart for your data and convey your insights more effectively.
    """)

if __name__ == "__main__":
    main()