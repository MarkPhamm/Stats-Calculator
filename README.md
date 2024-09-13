# Statistic Calculator App
<p align="center">
  <img src="https://github.com/user-attachments/assets/9006cf8f-1e73-4299-a713-5f5cfa06d84f" width="250"/>
  <img src="https://github.com/user-attachments/assets/bb628bdb-bbdd-4677-87a3-9e8d1b8f5e6b" width="250"/>
</p>

## Overview
[Click here to access the app](https://stats-calculator.streamlit.app/)

Welcome to the **Statistic Calculator** app! This Streamlit-powered application provides a comprehensive suite of statistical tools and models for data analysis, hypothesis testing, and machine learning. The app is divided into several sections, covering both discrete and continuous distributions, margin of error (MOE) calculations, hypothesis tests, statistical theorems, and machine learning models.

Whether you're looking to explore binomial distributions, run hypothesis tests, or apply machine-learning techniques like gradient descent, this app has you covered!

---

## Features

### 1. **Discrete Distributions**
   - **Binomial Distribution**: Calculate the probabilities of different outcomes in a binomial setting (e.g., number of successes in a series of trials).
   - **Probability**: General probability calculations for discrete events.

### 2. **Continuous Distributions**
   - **Normal Distribution**: Generate and analyze the bell curve of a normal distribution, often used in statistical analyses.
   - **Triangular Distribution**: Analyze data with known minimum, maximum, and mode values.
   - **Uniform Distribution**: Explore uniform distribution scenarios where all outcomes are equally likely.

### 3. **Margin of Error (MOE)**
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

### Layout

The layout features a **two-column design**:
- **Left Column**: Displays a resized image for visual appeal.
- **Right Column**: Shows the app title, "Statistic Calculator", and a brief description with a link to the developer’s [LinkedIn profile](https://www.linkedin.com/in/minhbphamm/).

---

## Installation & Usage

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-repository/statistic-calculator-app.git
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate the Virtual Environment**
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application**
   ```bash
   streamlit run app.py
   ```
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

## Future Enhancements

- Add support for additional distributions and hypothesis tests.
- Expand machine learning capabilities to include classification models.
- Enhance visualization for deeper insights into statistical data.

---

## Author

Developed by [Minh (Mark) Pham](https://www.linkedin.com/in/minhbphamm/), this app is designed to provide a comprehensive toolkit for both students and professionals in statistics and data science.

Feel free to reach out at minh.b.pham@tcu.edu for any questions or suggestions!
```

This updated README includes the additional details and sections you specified, providing clear instructions and information about the app.
