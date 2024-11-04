## User Interface

### Sidebar Menu

The app features a **sidebar** with grouped radio buttons, allowing you to choose the type of analysis or distribution you want to explore:
- **Discrete Distributions**
- **Continuous Distributions**
- **MOE**
- **Hypothesis Test**
- **Chi Square**
- **Theorem**
- **Machine Learning**

Once you select a topic, additional options will appear in the sidebar for further customization.

### Main Content

After selecting an option in the sidebar, the main content area dynamically updates to display the corresponding calculations, visualizations, or models. For example, choosing "Binomial" under "Discrete Distributions" will bring up a calculator for binomial distribution probabilities, while selecting "Gradient Descent" under "Machine Learning" will allow you to visualize the optimization process.

---

## Features

### 1. **Discrete Distributions**
   - **Binomial Distribution**: Calculate the probabilities of different outcomes in a binomial setting (e.g., number of successes in a series of trials).
   - **Probability**: General probability calculations for discrete events.

### 2. **Continuous Distributions**
   - **Normal Distribution**: Generate and analyze the bell curve of a normal distribution, often used in statistical analyses.
   - **Triangular Distribution**: Analyze data with known minimum, maximum, and mode values.
   - **Uniform Distribution**: Explore uniform distribution scenarios where all outcomes are equally likely.

### 3. **Margin of Error**
   - Calculate the margin of error for survey or sampling results, providing insights into the accuracy and precision of your data.

### 4. **Hypothesis Testing**
   - Perform hypothesis testing on different datasets to validate or reject statistical assumptions.

### 5. **Chi-Square Test**
   - Perform Chi-Square tests for **Goodness of Fit** or **Test of Independence** based on categorical data.

### 6. **Theorems**
   - **Central Limit Theorem (CLT)**: Demonstrate the CLT by analyzing the distribution of sample means.
   - **Law of Large Numbers (LLN)**: Illustrate the LLN by exploring the convergence of sample averages to the expected value as sample sizes increase.

### 7. **Machine Learning**
   - **Gradient Descent**: Visualize and understand how gradient descent works for continuous data optimization.
   - **Linear Regression**: Apply linear regression models to find the best-fit line and predict outcomes based on input features.

---

## Folder Structure

- **distributions**: Contains modules for handling different distributions (discrete and continuous).
  - `discrete`: Includes binomial and probability functions.
  - `continuous`: Includes normal, triangular, and uniform distributions.
- **hypothesis_test**: Contains modules for hypothesis testing and Chi-Square tests.
- **moe**: Contains the margin of error calculations.
- **theorem**: Handles statistical theorems like the Central Limit Theorem and Law of Large Numbers.
- **ml**: Includes machine learning models such as gradient descent and linear regression.

---