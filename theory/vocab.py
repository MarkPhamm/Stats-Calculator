import streamlit as st

def main():
    st.title("Statistics Overview")

    st.header("What is Statistics?")
    st.write("""
    Statistics is:
    - A method for extracting meaningful information from data.
    - A powerful tool for generating new insights from numerical data sets.
    """)

    st.header("Types of Statistics")
    
    st.subheader("1. Descriptive Statistics")
    st.write("""
    Descriptive statistics focuses on:
    - Organizing data effectively
    - Summarizing key information
    - Presenting data in clear, informative ways
    """)

    st.subheader("2. Inferential Statistics")
    st.write("""
    Inferential statistics involves:
    - Making conclusions about a population based on sample data
    - Predicting population characteristics using sample information
    """)

    st.header("Data Types")

    st.subheader("1. Qualitative Data (Categorical)")
    st.write("""
    Non-numeric data describing attributes or properties:
    - **Nominal Data:** Categories without order (e.g., colors, animal species)
    - **Ordinal Data:** Ordered categories without consistent intervals (e.g., rankings, satisfaction levels)
    """)

    st.subheader("2. Quantitative Data")
    st.write("""
    Numeric data representing quantities or amounts:
    - **Discrete Data:** Countable, often whole numbers (e.g., number of students, cars)
    - **Continuous Data:** Measurable values within a range (e.g., height, weight)
      - **Interval Data:** Numeric with meaningful intervals, no true zero (e.g., temperature in °C or °F)
      - **Ratio Data:** Numeric with meaningful intervals and a true zero point (e.g., height, weight, age, income)
    """)

    st.header("Key Statistics Concepts")
    
    st.subheader("1. Population and Parameters")
    st.write("""
    - Population: The entire group of interest in a statistical study
    - Parameters: Numerical characteristics of a population (often unknown)
    - Populations can be very large or even infinite
    """)

    st.subheader("2. Sample and Statistics")
    st.write("""
    - Sample: A subset of the population used for study
    - Statistics: Numerical characteristics of a sample (used to estimate population parameters)
    - Samples are typically smaller than the population and often randomly selected for fairness
    """)

    st.subheader("3. Confidence and Significance Levels")
    st.write("""
    - **Confidence Level:** The probability that an estimate is correct
      Example: 95% confidence level means the estimate is likely correct 95% of the time
    - **Significance Level:** The probability of drawing an incorrect conclusion
      Example: 5% significance level means the conclusion may be wrong 5% of the time
    """)

    st.header("Variables and Domain")
    st.write("""
    - Variable: A characteristic of interest in a population or sample
    - Domain: The set of all possible values for a variable
    - Data: The actual observed values of a variable
    """)

    st.header("Frequency Distribution")
    st.write("""
    - A summary table showing categories and their counts
    - **Relative Frequency Distribution:** Shows the proportion of each category in the data
    """)

    st.header("Data Distribution Shapes")
    st.write("""
    Common distribution shapes:
    - **Negatively Skewed:** Tail extends to the left
    - **Positively Skewed:** Tail extends to the right
    - **Approximately Normal:** 
      - Symmetric bell-shaped curve
      - Mean = Median = Mode
      - Follows specific empirical rules
    """)

    st.subheader("Skewness Interpretation:")
    st.write("""
    - Highly skewed: Skewness < -1 or > 1
    - Moderately skewed: -1 < Skewness < -0.5 or 0.5 < Skewness < 1
    - Approximately symmetric: -0.5 < Skewness < 0.5
    """)

    st.header("Exploring Relationships")
    st.write("""
    Scatter plots visualize relationships between two variables:
    - X-axis: Independent variable
    - Y-axis: Dependent variable
    """)

    st.subheader("Covariance")
    st.write("""
    Covariance indicates the direction of variable relationships:
    - Positive: Variables increase together
    - Negative: One variable increases as the other decreases
    - Zero: No linear relationship
    """)

    st.subheader("Correlation Coefficient")
    st.write("""
    Measures the strength and direction of linear relationships:
    - Range: -1 to 1
    - 1: Perfect positive linear relationship
    - -1: Perfect negative linear relationship
    - 0: No linear relationship
    """)

if __name__ == "__main__":
    main()
