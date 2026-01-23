# Statistics Calculator

Interactive statistics and machine learning playground built with **Streamlit** for exploring probability, distributions, hypothesis testing, confidence intervals, and ML models.

**[🌐 Live App](https://stats-calculator.streamlit.app/)** | **Tech Stack:** Python, Streamlit, NumPy, pandas, SciPy, scikit-learn, Matplotlib, Plotly

---

## Features

### 📖 Theory & Probability
Statistical vocabulary, chart principles, probability rules, Central Limit Theorem, Law of Large Numbers, and Monty Hall simulation.

![Theory Page](images/theory.png)

### 📊 Distributions
**Discrete:** Binomial, Poisson, custom probability distributions  
**Continuous:** Normal (with inverse), Triangular, Uniform, Exponential

![Distributions Page](images/distributions.png)

### 🎯 Confidence Intervals & Margin of Error
Calculate margin of error and inverse calculations for sample size determination.

![Confidence Interval Page](images/confidence_interval.png)

### 🧪 Hypothesis Testing
Z-tests, t-tests, proportion tests, Chi-Square tests with visualizations and automatic p-value calculations.

![Hypothesis Test Page](images/hypothesis_test.png)

### 🤖 Machine Learning
**Supervised:** Linear regression, gradient descent  
**Unsupervised:** K-means clustering

![Machine Learning Page](images/machine_learning.png)

### 🔍 Data Exploration
Exploratory data analysis tools for uploaded datasets.

![Data Exploration Page](images/data_exploration.png)

---

## Quick Start

**Prerequisites:** Python 3.9+, [`uv`](https://github.com/astral-sh/uv)

```bash
# Clone repository
git clone https://github.com/<your-username>/Stats-Calculator.git
cd Stats-Calculator

# Create virtual environment
uv venv .venv

# Activate (Windows)
.venv\Scripts\activate
# Activate (macOS/Linux)
source .venv/bin/activate

# Install dependencies
uv sync

# Run app
uv run streamlit run Introduction.py
```

---

## Project Structure

```
Stats-Calculator/
├── Introduction.py          # Home page
├── pages/                   # Streamlit pages
│   ├── 1_Theory.py
│   ├── 2_Distribution.py
│   ├── 3_Confidence_Interval.py
│   ├── 4_Hypothesis_Test.py
│   ├── 5_Machine_Learning.py
│   └── 6_Data_Exploration.py
├── distributions/           # Distribution calculators
├── hypothesis_test/        # Hypothesis testing tools
├── moe/                     # Margin of error calculators
├── ml/                      # Machine learning models
├── probability/             # Probability concepts
├── theorem/                 # Statistical theorems
├── theory/                  # Chart gallery & vocabulary
├── utils.py                 # Shared UI components
└── images/                  # Screenshots and assets
```

---

## Authors

- **Minh (Mark) Pham** – [LinkedIn](https://www.linkedin.com/in/minhbphamm/)
- **Hoan Nguyen** – [LinkedIn](https://www.linkedin.com/in/hoanng15/)

---

## License

See `LICENSE` file for details.
