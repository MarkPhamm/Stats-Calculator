import streamlit as st

def main():
    # Title of the app
    st.title("Statistics Overview")

    # Introduction to Statistics
    st.header("What is Statistics")
    st.write("""
    - Statistics is a way to get information from data.
    - It is a tool for creating new understanding from a set of numbers.
    """)

    # Types of Statistics
    st.header("Types of Statistics")
    
    st.subheader("1. Descriptive Statistics")
    st.write("""
    - Descriptive statistics deals with methods of:
        - Organizing
        - Summarizing
        - Presenting data in a convenient and informative way.
    """)

    st.subheader("2. Inferential Statistics")
    st.write("""
    - Inferential statistics involves:
        - Drawing conclusions about the characteristics of a population based on a sample.
        - Making predictions or inferences about the population.
    """)

   # Data Types
    st.header("Data Types")

    st.subheader("1. Qualitative Data (Categorical)")
    st.write("""
    - Descriptive, non-numeric data that characterizes attributes or properties.
        - **Nominal Data:** Categories with no inherent order (e.g., colors, types of animals).
        - **Ordinal Data:** Categories with a meaningful order, but without consistent differences between ranks (e.g., rankings, satisfaction levels).
    """)

    st.subheader("2. Quantitative Data")
    st.write("""
    - Numeric data representing quantities or amounts.
      - **Discrete Data**: Countable values, often integers (e.g., number of students, cars).
      - **Continuous Data**: Measurable values that can take any number within a range (e.g., height, weight).
        - **Interval Data**: Numeric values with meaningful intervals but no true zero point (e.g., temperature in Celsius or Fahrenheit).
        - **Ratio Data**: Numeric values with meaningful intervals but has true zero point (e.g., height, weight, age, and income""")

    # Key Statistics Concepts
    st.header("Key Statistics Concepts")
    
    st.subheader("1. Population - Parameter")
    st.write("""
    - A population is the group of all items of interest to a statistics practitioner.
    - Populations can be very large, sometimes infinite.
    """)

    st.subheader("2. Sample - Statistic")
    st.write("""
    - A sample is a subset of the population.
    - Samples are typically smaller than the population and are often selected randomly to ensure equal chances for everyone.
    """)

    st.subheader("3. Confidence and Significance Levels")
    st.write("""
    - **Confidence Level**: Proportion of times that estimates will be correct.
      - E.g., a 95% confidence level means that estimates will be correct 95% of the time.
    - **Significance Level**: Measures how frequently the conclusion will be wrong in the long run.
      - E.g., a 5% significance level means the conclusion will be wrong 5% of the time.
    """)

    # Variables and Domain
    st.header("Variables and Domain")
    st.write("""
    - A variable represents some characteristic of a population or sample.
    - The domain or value set of the variable refers to the range of possible values for a variable.
    - Data are the observed values of a variable.
    """)

    # Frequency Distribution
    st.header("Frequency Distribution")
    st.write("""
    - We can summarize data in a table that presents the categories and their counts.
    - **Relative Frequency Distribution**: Lists categories and the proportion with which each occurs.
    """)

    # Data Distribution
    st.header("Data Distribution")
    st.write("""
    Data can have different shapes:
    - **Negatively Skewed**
    - **Positively Skewed**
    - **Approximately Normal**: 
      - A normal distribution where the mean = median = mode. 
      - 100% of data lies within the bell curve.
      - Empirical rules apply.
    """)

    st.subheader("Skewness Rules:")
    st.write("""
    - If skewness is less than -1 or greater than 1: Highly skewed distribution.
    - If skewness is between -1 and -0.5 or between 0.5 and 1: Moderately skewed distribution.
    - If skewness is between -0.5 and 0.5: Approximately symmetric.
    """)

    # Scatter Plot and Correlation
    st.header("Exploring Relationships")
    st.write("""
    To explore relationships, we use a scatter diagram that plots two variables against each other:
    - The independent variable is placed on the horizontal axis (X).
    - The dependent variable is placed on the vertical axis (Y).
    """)

    st.subheader("Covariance")
    st.write("""
    Covariance tells us the direction of the relationship between variables:
    - Positive Relationship
    - Negative Relationship
    - No Relationship
    """)

    st.subheader("Correlation Coefficient")
    st.write("""
    - The correlation coefficient measures the strength and direction of the relationship between two variables.
    - The correlation coefficient ranges from -1 to 1:
      - **1** indicates a perfect positive linear relationship.
      - **-1** indicates a perfect negative linear relationship.
      - **0** indicates no linear relationship.
    """)

if __name__ == "__main__":
    main()

