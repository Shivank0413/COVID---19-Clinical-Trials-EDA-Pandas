

# 🧪 COVID-19 Clinical Trials EDA

This repository presents a detailed **Exploratory Data Analysis (EDA)** on a dataset of COVID-19 clinical trials. The aim is to understand trends in trial statuses, phases, age groups, gender targeting, and temporal patterns from the start dates of trials.

---

## 📂 Dataset

The dataset used in this analysis is a CSV file named **`COVID.csv`**, which contains publicly available data about clinical trials related to COVID-19.

### Key Columns:

* `Status`: Trial status (e.g., Completed, Recruiting)
* `Phases`: Clinical trial phase (e.g., Phase 1, Phase 2/3)
* `Gender`: Target gender
* `Age`: Age groups (e.g., 18–25, 60+)
* `Start Date`: When the trial began
* `Acronym`, `Results First Posted`, `Study Documents`, etc.

> 📌 **Note:** Ensure the file path (`D:\COVID.csv`) is correctly updated according to your local directory structure before running the script.

---

## 🛠️ Libraries Used

* `pandas` – Data manipulation
* `numpy` – Numerical operations
* `matplotlib` – Static data visualizations
* `seaborn` – Statistical data visualizations

---

## 📊 Analysis Steps

### ✅ Step 1: Import Libraries

All necessary libraries are imported at the beginning.

### ✅ Step 2: Load & Inspect Dataset

* View first few rows using `df.head()`
* Print dataset shape, info, and descriptive statistics
* Check and handle missing values

### ✅ Step 3: Data Cleaning

* Dropped high-null columns: `Results First Posted`, `Study Documents`
* Filled missing values in `Acronym` with `"Missing Acronym"`

### ✅ Step 4: Visualizations

* **Status Distribution** – Bar plot of trial statuses
* **Phases Distribution** – Bar plot of clinical phases
* **Gender Distribution** – Bar plot of target genders
* **Age Group Distribution** – Bar plot categorized by age
* **Status vs Phases** – Stacked bar plot of trial phase by status
* **Trials Over Time** – Line plot showing monthly number of trials started

---

## 📈 Sample Visuals

> Plots are generated using Matplotlib and Seaborn and include:

* Clinical trial status breakdown
* Trial phase distributions
* Gender-based targeting
* Age group analysis
* Time-series of trial initiations

---

## 📋 Summary of Findings

* ✅ Most trials are marked as **'Completed'**
* 👥 Majority of trials target **adult populations**
* 📈 There’s a **steady increase** in trial count over time

---

## 💾 Output

The cleaned dataset is saved as:

```
cleaned_covid_clinical_trials.csv
```

---

## ▶️ How to Use

1. Clone this repository.
2. Place `COVID.csv` in your preferred path.
3. Open the Python file or Jupyter Notebook.
4. Update the file path if needed.
5. Run all cells or execute the script to reproduce the analysis.

---

## 🔮 Future Scope

* Correlation analysis between variables
* Integration with interactive dashboards (e.g., Plotly, Dash)
* Predictive modeling on trial success status (optional)

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

* Clinical trial data is assumed to be sourced from a public COVID-19 research database.
* Special thanks to all contributors working toward pandemic-related research.

---
