# 📊 Data Science & Machine Learning Course
### Delivered at [IFOA](https://www.ifoa.it/) — Bologna, Italy

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)
![Sessions](https://img.shields.io/badge/Sessions-18-6366f1?style=flat-square)
![Level](https://img.shields.io/badge/Level-Intermediate-f59e0b?style=flat-square)
![Language](https://img.shields.io/badge/Language-Python-3776AB?style=flat-square)
![Institution](https://img.shields.io/badge/Institution-IFOA%20Bologna-e11d48?style=flat-square)

---

## 🏛️ About This Course

This repository contains the complete teaching materials for a professional **Data Science and Machine Learning** course delivered at **IFOA (Istituto di Formazione Operatori Aziendali)** in Bologna, Italy — one of Italy's leading professional training institutions.

The course was designed and delivered as an intensive, hands-on programme for professionals looking to develop practical data science skills using Python. Sessions were held across several weeks, combining theoretical foundations with immediately applicable Python code — every concept was taught through a working Jupyter notebook.

The curriculum progresses from Python and data manipulation fundamentals through to machine learning model building, evaluation, and real-world application — the complete arc from raw data to actionable insight.

---

## 👨‍🏫 Instructor

**Alket Cecaj, PhD**

Data Scientist with 12+ years of experience spanning academic research, banking analytics, and credit risk modelling. PhD in Industrial Innovation Engineering with a research background in computational social science. Previously taught university-level courses in Java and data science in Italy during a postdoctoral appointment.

At the time of this course: working as a Data Scientist in the banking sector, with hands-on experience in predictive modelling, NLP, and machine learning at scale.

---

## 🎯 Course Objectives

By the end of this course, students were able to:

- Write clean, idiomatic Python for data science workflows
- Load, clean, explore, and transform structured datasets with pandas
- Produce publication-quality visualisations with Matplotlib and Seaborn
- Understand and apply core statistical concepts to real data
- Build, train, and evaluate supervised and unsupervised machine learning models
- Apply the full data science workflow — from raw data to model-driven decisions
- Interpret model outputs and communicate findings clearly

---

## 🗓️ Course Structure & Curriculum

The course was delivered across **18 sessions**, each with its own Jupyter notebook. Sessions are named by date (`DDMM` format), running from March through June.

---

### 📘 Module 1 — Python for Data Science Foundations
*Sessions: 03/05 · 04/05 · 05/05 · 06/05*

The opening module established the Python toolkit every data scientist needs. Rather than teaching Python in the abstract, concepts were introduced in the context of data problems.

**Topics covered:**
- Python data types, control flow, and functions — with a data science lens
- List comprehensions, generators, and functional patterns (`map`, `filter`, `zip`)
- NumPy: arrays, vectorised operations, broadcasting, and linear algebra basics
- Introduction to Jupyter notebooks as a scientific computing environment
- Working with files: reading CSV, JSON, and text data into Python

**Key skills developed:**
```python
import numpy as np

# Vectorised operations — no loops needed
data = np.array([2.3, 4.1, 5.6, 1.2, 8.9])
normalised = (data - data.mean()) / data.std()

# Array slicing and boolean indexing
above_mean = data[data > data.mean()]
```

---

### 📘 Module 2 — Data Manipulation with pandas
*Sessions: 10/05 · 11/05 · 12/05*

pandas is the workhorse of data science in Python. This module went deep — covering not just the API but the mental model behind tidy data and the data wrangling mindset.

**Topics covered:**
- Series and DataFrame: construction, indexing, slicing (`loc`, `iloc`)
- Loading data: `pd.read_csv()`, `read_excel()`, `read_json()`, and web sources
- Data cleaning: handling missing values (`dropna`, `fillna`), duplicates, data types
- Feature engineering: creating new columns, `apply()`, `map()`, string operations
- Grouping and aggregation: `groupby()`, `agg()`, `pivot_table()`
- Merging datasets: `merge()`, `join()`, `concat()` — and when to use each
- Working with time series: `DatetimeIndex`, resampling, rolling windows

**Key skills developed:**
```python
import pandas as pd

df = pd.read_csv('sales_data.csv', parse_dates=['date'])

# Groupby with multiple aggregations
monthly = (df.groupby(df['date'].dt.month)
             .agg({'revenue': 'sum', 'units': 'mean', 'customer_id': 'nunique'})
             .rename(columns={'customer_id': 'unique_customers'}))

# Feature engineering
df['revenue_per_unit'] = df['revenue'] / df['units']
df['is_high_value'] = df['revenue'] > df['revenue'].quantile(0.75)
```

---

### 📘 Module 3 — Data Visualisation
*Sessions: 13/05 · 17/05*

A model is only as useful as the story it tells. This module focused on building a visualisation vocabulary — from exploratory plots to presentation-ready figures.

**Topics covered:**
- Matplotlib architecture: figures, axes, subplots, and the object-oriented API
- Core chart types: line, bar, scatter, histogram, boxplot, heatmap
- Seaborn: statistical visualisation with minimal code — `pairplot`, `heatmap`, `violinplot`, `regplot`
- Colour theory for data: sequential, diverging, and qualitative palettes
- Multi-panel figures and layout control
- Visualising distributions, correlations, and group comparisons
- Saving and exporting publication-quality figures

**Key skills developed:**
```python
import matplotlib.pyplot as plt
import seaborn as sns

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Distribution comparison
axes[0].hist(group_a, bins=30, alpha=0.6, label='Group A', color='steelblue')
axes[0].hist(group_b, bins=30, alpha=0.6, label='Group B', color='coral')
axes[0].legend()
axes[0].set_title('Distribution Comparison')

# Correlation heatmap
sns.heatmap(df.corr(), annot=True, fmt='.2f', cmap='RdYlGn',
            center=0, ax=axes[1])
axes[1].set_title('Feature Correlation Matrix')

plt.tight_layout()
plt.savefig('analysis.png', dpi=150, bbox_inches='tight')
```

---

### 📘 Module 4 — Statistics for Data Science
*Sessions: 18/05 · 19/05*

Statistics is the language data science is written in. This module covered the core concepts that underpin every model: distributions, inference, and relationships between variables.

**Topics covered:**
- Descriptive statistics: mean, median, variance, skewness, kurtosis
- Probability distributions: normal, binomial, Poisson — and when each applies
- Hypothesis testing: null/alternative hypotheses, p-values, significance levels
- t-tests: one-sample, two-sample, paired
- Chi-squared test for categorical independence
- Correlation: Pearson, Spearman — and the critical difference between correlation and causation
- Introduction to linear regression as a statistical model
- Confidence intervals and their practical interpretation

**Key skills developed:**
```python
from scipy import stats
import numpy as np

# Two-sample t-test
group_a = np.array([...])
group_b = np.array([...])
t_stat, p_value = stats.ttest_ind(group_a, group_b)
print(f"t={t_stat:.3f}, p={p_value:.4f}")
print("Significant" if p_value < 0.05 else "Not significant")

# Pearson correlation with confidence
corr, p = stats.pearsonr(df['feature_1'], df['target'])
```

---

### 📘 Module 5 — Machine Learning: Supervised Learning
*Sessions: 20/05 · 24/05 · 26/05*

The heart of the course. Students built and evaluated a range of supervised learning models — understanding not just how to call the scikit-learn API but *why* each model works and when to use it.

**Topics covered:**

*Regression:*
- Linear Regression: coefficients, R², residual analysis
- Ridge and Lasso regularisation — controlling overfitting via penalty terms
- Polynomial features for non-linear relationships

*Classification:*
- Logistic Regression: log-odds, sigmoid function, decision boundary
- Decision Trees: splitting criteria (Gini, entropy), depth, pruning
- Random Forests: ensemble intuition, feature importance, out-of-bag error
- K-Nearest Neighbours: distance metrics, the curse of dimensionality
- Support Vector Machines: margin maximisation, kernel trick

*Model selection and evaluation:*
- Train/test split and cross-validation (`KFold`, `StratifiedKFold`)
- Metrics: accuracy, precision, recall, F1-score, ROC-AUC for classification; MSE, MAE, R² for regression
- Confusion matrix interpretation
- Hyperparameter tuning: `GridSearchCV` and `RandomizedSearchCV`
- The bias-variance tradeoff

**Key skills developed:**
```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# Build a pipeline: scaling + model
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('clf', RandomForestClassifier(random_state=42))
])

# Cross-validated evaluation
cv_scores = cross_val_score(pipeline, X, y, cv=5, scoring='roc_auc')
print(f"AUC: {cv_scores.mean():.3f} ± {cv_scores.std():.3f}")

# Hyperparameter search
param_grid = {'clf__n_estimators': [50, 100, 200], 'clf__max_depth': [3, 5, None]}
grid = GridSearchCV(pipeline, param_grid, cv=5, scoring='roc_auc', n_jobs=-1)
grid.fit(X_train, y_train)
print(f"Best params: {grid.best_params_}")
```

---

### 📘 Module 6 — Machine Learning: Unsupervised Learning
*Sessions: 27/05 · 31/05*

Not all problems come with labels. This module covered the techniques for finding structure in unlabelled data — clustering, dimensionality reduction, and anomaly detection.

**Topics covered:**
- K-Means clustering: the algorithm, choosing k (elbow method, silhouette score)
- Hierarchical clustering: dendrograms and linkage strategies
- DBSCAN: density-based clustering, handling irregular shapes and noise
- Principal Component Analysis (PCA): variance explained, scree plots, biplot interpretation
- t-SNE: high-dimensional visualisation
- Practical applications: customer segmentation, anomaly detection, feature reduction before supervised learning

**Key skills developed:**
```python
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Standardise before clustering
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Elbow method for k selection
inertias = []
for k in range(2, 11):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_scaled)
    inertias.append(km.inertia_)

plt.plot(range(2, 11), inertias, marker='o')
plt.xlabel('Number of clusters k')
plt.ylabel('Inertia')
plt.title('Elbow Method')

# PCA for visualisation
pca = PCA(n_components=2)
X_2d = pca.fit_transform(X_scaled)
print(f"Variance explained: {pca.explained_variance_ratio_.sum():.1%}")
```

---

### 📘 Module 7 — Applied Projects & Capstone
*Sessions: 01/06 (datascience_0106)*

The final session brought everything together. Students applied the full data science workflow to a real-world dataset — from raw data ingestion and exploratory analysis through to model building, evaluation, and results communication.

**Topics covered:**
- End-to-end project structure and best practices
- Defining a business question and translating it to a modelling problem
- Feature engineering from domain knowledge
- Model selection rationale — not just picking the best metric
- Results interpretation and stakeholder communication
- Presentation of findings

---

## 📁 Repository Structure

```
DataScienceCourse4IFOA/
│
├── datascience_0305/    # Session 1  — 03 May  │ Python & NumPy foundations
├── datascience_0405/    # Session 2  — 04 May  │ Python data structures & functions
├── datascience_0505/    # Session 3  — 05 May  │ NumPy deep dive
├── datascience_0605/    # Session 4  — 06 May  │ Intro to pandas
├── datascience_1005/    # Session 5  — 10 May  │ Data loading & cleaning
├── datascience_1105/    # Session 6  — 11 May  │ pandas wrangling
├── datascience_1205/    # Session 7  — 12 May  │ Groupby & aggregation
├── datascience_1305/    # Session 8  — 13 May  │ Data visualisation I
├── datascience_1705/    # Session 9  — 17 May  │ Data visualisation II
├── datascience_1805/    # Session 10 — 18 May  │ Descriptive statistics
├── datascience_1905/    # Session 11 — 19 May  │ Hypothesis testing
├── datascience_2005/    # Session 12 — 20 May  │ Intro to ML & regression
├── datascience_2405/    # Session 13 — 24 May  │ Classification models
├── datascience_2605/    # Session 14 — 26 May  │ Model evaluation & selection
├── datascience_2705/    # Session 15 — 27 May  │ Unsupervised learning I
├── datascience_3105/    # Session 16 — 31 May  │ Unsupervised learning II
├── datascience_0106/    # Session 17 — 01 Jun  │ Capstone project
│
├── Data Science & Machine Learning.pptx   # Full lecture slide deck
├── Index.PNG                               # Course curriculum map
└── Readme.md
```

---

## 🛠️ Tech Stack

| Library | Purpose |
|---------|---------|
| `numpy` | Numerical computing, array operations, linear algebra |
| `pandas` | Data manipulation, cleaning, and analysis |
| `matplotlib` | Core plotting and figure construction |
| `seaborn` | Statistical data visualisation |
| `scikit-learn` | Machine learning models, pipelines, and evaluation |
| `scipy` | Statistical tests and scientific computing |
| `jupyter` | Interactive notebook environment |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Jupyter Lab or Jupyter Notebook
- Basic Python knowledge (the course assumes programming familiarity)

### Setup

```bash
git clone https://github.com/alketcecaj12/DataScienceCourse4IFOA.git
cd DataScienceCourse4IFOA

pip install numpy pandas matplotlib seaborn scikit-learn scipy jupyter

jupyter lab
```

Navigate into any session folder and open the notebook. Sessions are designed to be self-contained, though following them in order gives the best experience.

---

## 📋 Target Audience

This course was designed for professionals with:

| Background | Notes |
|------------|-------|
| Programming experience | Python familiarity recommended; other languages sufficient |
| No ML background | Machine learning concepts introduced from first principles |
| Domain knowledge | Finance, business, or engineering professionals will find immediate applications |
| Goal: applied skills | Emphasis on practical code over mathematical theory |

---

## 🗺️ Learning Arc

```
Sessions  1– 4  │ Python + NumPy      ████░░░░░░░░  Foundation
Sessions  5– 8  │ pandas              ████████░░░░  Data Layer
Sessions  9–10  │ Visualisation       ██████░░░░░░  Communication
Sessions 11–12  │ Statistics          ███████░░░░░  Theory Bridge
Sessions 13–15  │ Supervised ML       ██████████░░  Core ML
Sessions 16–17  │ Unsupervised ML     █████████░░░  Advanced ML
Session      18  │ Capstone            ████████████  Integration
```

---

## 🏢 About IFOA

[IFOA](https://www.ifoa.it/) (Istituto di Formazione Operatori Aziendali) is one of Italy's leading professional training organisations, headquartered in Reggio Emilia with a strong presence in Bologna. It delivers vocational and professional development programmes across technology, business, and management, serving thousands of professionals and companies annually.

This course was part of IFOA's data science and digital transformation upskilling portfolio.

---

## 📬 Instructor Contact

**Alket Cecaj, PhD**  
Data Scientist & Quantitative Risk Analyst  
[GitHub](https://github.com/alketcecaj12) · Copenhagen, Denmark

---

*Designed and delivered with the conviction that data science is most powerful when it is taught practically — through code that runs, data that breathes, and problems that matter.*
