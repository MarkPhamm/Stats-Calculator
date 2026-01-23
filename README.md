## Statistics Calculator (Streamlit)

Interactive statistics and machine‑learning playground built with **Streamlit**, designed for students and practitioners who want to explore probability, statistical theory, hypothesis testing, confidence intervals, and core ML models in a single app.

Hosted version: **[Open the app](https://stats-calculator.streamlit.app/)**  
Tech stack: **Python**, **Streamlit**, **NumPy**, **pandas**, **SciPy**, **scikit‑learn**, **statsmodels**, **Matplotlib**, **Plotly**

---

### Overview of Features

- **Theory & Probability (page `1_Theory`)**
  - Statistical vocabulary and core concepts.
  - Visual chart principles and best practices.
  - Probability rules (union, intersection, conditional probability, complements, multiplication rule).
  - Interactive demos for:
    - **Central Limit Theorem (CLT)**  
    - **Law of Large Numbers (LLN)**  
    - **Monty Hall problem** simulation.

- **Distributions (page `2_Distribution`)**
  - **Discrete distributions**
    - Binomial distribution calculator.
    - Custom discrete probability distribution table with \(E(X)\), \(\mathrm{Var}(X)\), and \(\mathrm{Std}(X)\).
    - Poisson distribution calculator.
  - **Continuous distributions**
    - Normal distribution (PDF, CDF, shaded regions, areas between points).
    - Inverse normal calculator (find \(x\) for a given tail area).
    - Triangular, uniform, and exponential distributions with interactive inputs and plots.

- **Confidence Intervals & Margin of Error (page `3_Confidence_Interval`)**
  - Margin of Error calculators for common survey / sampling settings.
  - Inverse Margin of Error tools (solve for required sample size given a desired MOE).

- **Hypothesis Testing (page `4_Hypothesis_Test`)**
  - Mean tests:
    - Z‑tests (σ known).
    - t‑tests (σ unknown) with degrees of freedom and t‑distribution.
  - Proportion tests:
    - One‑sample Z test for proportions.
  - Automatic computation of:
    - Test statistics (Z or t).
    - Critical values based on \( \alpha \) and tail type.
    - p‑values and formal decision (reject / fail to reject \(H_0\)).
  - Visualizations of rejection regions and test statistics on the relevant distribution.
  - **Chi‑Square tests** (via `chi_square.py`) for goodness‑of‑fit / independence on categorical data.

- **Machine Learning (page `5_Machine_Learning`)**
  - **Supervised learning**
    - Gradient descent visualizations for regression.
    - Linear regression from uploaded `.csv` / `.xlsx` files:
      - Column selection for target and predictors.
      - Train/test split, RMSE and \(R^2\) metrics.
      - Full OLS summary via `statsmodels` (p‑values, coefficients, etc.).
  - **Unsupervised learning**
    - K‑means clustering demo with interactive parameters.

- **Data Exploration (page `6_Data_Exploration`)**
  - Exploratory data analysis tools (EDA) for uploaded datasets  
    (profiling / summary features depending on the current implementation of this page).

- **Chart Gallery & Visual Best Practices**
  - Rich interactive gallery (`theory/chart.py`) of:
    - Histogram, line‑histogram (smoothed), box plot.
    - Bar, stacked bar, line chart.
    - Pie and donut charts.
    - Scatter and bubble charts.
  - Explanations of when to use each chart type and how to interpret them.

- **Polished UI / UX**
  - Global dark theme with cyan accents and smooth animations via `utils.add_custom_css()`.
  - Reusable UI helpers in `utils.py`:
    - Headers, info/warning/success cards, KPI cards, dividers, site‑wide footer, and logo header.

---

### Project Structure

- `Introduction.py`  
  Landing (home) page. Configures Streamlit, applies global styling, and explains how to use the app.

- `pages/` – **Streamlit multipage routes**
  - `1_Theory.py` – Navigation for theory, theorems, probability concepts, and Monty Hall.
  - `2_Distribution.py` – Navigation for discrete/continuous distributions and their calculators.
  - `3_Confidence_Interval.py` – Margin of Error and inverse MOE tools.
  - `4_Hypothesis_Test.py` – Hypothesis testing and Chi‑Square tests.
  - `5_Machine_Learning.py` – Supervised / unsupervised learning demos.
  - `6_Data_Exploration.py` – Data exploration / EDA utilities.

- `distributions/`
  - `discrete/` – Binomial, Poisson, and generic discrete probability distribution calculator.
  - `continuous/` – Normal, inverse normal, triangular, uniform, and exponential distributions.

- `hypothesis_test/`
  - `hypothesis_test.py` – Mean and proportion Z/t tests with visualizations.
  - `chi_square.py` – Chi‑Square test workflows.

- `moe/`
  - `moe.py`, `moe_inverse.py` – Margin of Error calculators.

- `ml/`
  - `supervised/regression/` – Gradient descent and linear regression (file‑based).
  - `unsupervised/` – K‑means clustering.

- `probability/`
  - `probability.py` – Explanations of core probability rules.
  - `monty_hall.py` – Monty Hall simulation.

- `theorem/`
  - `clt.py`, `llon.py` – CLT and LLN demos.

- `theory/`
  - `chart.py` – Interactive chart gallery and explanations.
  - `vocab.py` – Statistical vocabulary / definitions.

- `utils.py`  
  Global styling and shared UI components (headers, cards, footer, etc.).

- `main.py`  
  Simple placeholder script (not used as the Streamlit entry point).

- `.streamlit/config.toml`, `requirements.txt`, `LICENSE`, `style.css`, `images/`, etc.  
  Configuration, dependencies, assets, and styling.

---

### Getting Started (Local Development)

- **Prerequisites**
  - Python 3.9+ recommended.
  - [`uv`](https://github.com/astral-sh/uv) installed.

- **1. Clone the repository**

```bash
git clone https://github.com/<your-username>/Stats-Calculator.git
cd Stats-Calculator
```

- **2. Create and activate a virtual environment with `uv`**

```bash
# Create a .venv environment (if you don't already have one)
uv venv .venv

# Activate the environment
# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

- **3. Install dependencies with `uv`**

```bash
uv sync
```

- **4. Run the Streamlit app**

```bash
uv run streamlit run Introduction.py
```

Streamlit will open the app in your browser (usually at `http://localhost:8501`). Use the sidebar navigation to switch between pages like **Theory**, **Distributions**, **Confidence Interval**, **Hypothesis Test**, **Machine Learning**, and **Data Exploration**.

---

### Development Notes

- **Entry point**: The main entry for Streamlit is `Introduction.py`. Streamlit automatically discovers all scripts under `pages/` as separate app pages.
- **State & interactivity**:
  - Most calculators use Streamlit widgets for inputs (sliders, number inputs, radios) and recompute results on each interaction.
  - Some modules (like the discrete probability table and EDA tools) use `st.session_state` to persist user edits.
- **Visualization**:
  - Continuous distributions and hypothesis tests use **Matplotlib** and **SciPy** for plots and distributions.
  - The chart gallery and some EDA/visualization pages use **Plotly** for interactive graphics.

---

### Contributing

Contributions, bug reports, and feature requests are welcome.

- **Ideas to extend**:
  - Additional distributions (e.g., Student’s t, F, Beta, Gamma).
  - More hypothesis tests (two‑sample tests, ANOVA, non‑parametric tests).
  - Classification models (logistic regression, decision trees, etc.).
  - Richer EDA (automatic profiling, correlation heatmaps, missing‑value analysis).

If you open a pull request, please:

- Keep functions small and focused.
- Reuse existing helpers in `utils.py` for consistent styling.
- Add concise docstrings where you introduce new modules or major functions.

---

### License

This project is released under the terms of the license specified in `LICENSE` in this repository.

---

### Authors

- **Minh (Mark) Pham** – creator and primary author  
  LinkedIn: `https://www.linkedin.com/in/minhbphamm/`

- **Hoan Nguyen** – UI/UX and engineering contributions  
  LinkedIn: `https://www.linkedin.com/in/hoanng15/`

If you use this app in a course, project, or tutorial, a short attribution to the authors is appreciated.
