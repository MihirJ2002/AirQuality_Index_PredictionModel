# 🌍 Air Quality Prediction Using Machine Learning

An end-to-end **Machine Learning Regression Project** focused on analyzing air-quality sensor data and predicting **Relative Humidity (RH)** using multiple regression algorithms.

The project demonstrates a complete data science workflow including **data preprocessing, exploratory data analysis, statistical analysis, outlier treatment, feature analysis, model development, model comparison, and prediction evaluation**.

---

## 📌 Project Overview

Air-quality monitoring systems generate large volumes of environmental and sensor data. Extracting meaningful relationships from these measurements can support environmental monitoring and predictive analytics.

In this project, I developed a machine learning pipeline to analyze air-quality data and predict **Relative Humidity (RH)** based on available sensor measurements.

The project focuses on:

* Exploratory Data Analysis (EDA)
* Descriptive Statistical Analysis
* Outlier Detection and Treatment
* Feature Correlation Analysis
* Data Preprocessing
* Machine Learning Regression
* Model Comparison
* Residual Analysis
* Actual vs Predicted Analysis

---

## 🎯 Project Objective

The primary objective is to build a machine learning regression model capable of predicting **Relative Humidity (RH)** from air-quality sensor measurements.

The project also aims to:

* Identify important relationships among environmental variables.
* Detect and control extreme observations.
* Compare multiple machine learning algorithms.
* Evaluate model performance on unseen data.
* Analyze prediction errors through residual analysis.

---

## 🛠️ Tech Stack

| Category                | Technologies                    |
| ----------------------- | ------------------------------- |
| Programming             | Python                          |
| Data Manipulation       | Pandas, NumPy                   |
| Visualization           | Matplotlib, Seaborn             |
| Machine Learning        | Scikit-learn                    |
| Statistical Processing  | SciPy                           |
| Development Environment | Google Colab / Jupyter Notebook |
| Version Control         | Git & GitHub                    |

---

## 🔄 Machine Learning Workflow

```text
Data Collection
      ↓
Data Ingestion
      ↓
Data Cleaning
      ↓
Exploratory Data Analysis
      ↓
Descriptive Statistics
      ↓
Outlier Detection
      ↓
Winsorization
      ↓
Correlation Analysis
      ↓
Feature / Target Separation
      ↓
Train-Test Split
      ↓
Min-Max Scaling
      ↓
Model Training
      ↓
Model Comparison
      ↓
Prediction
      ↓
Residual Analysis
      ↓
Actual vs Predicted Analysis
```

---

## 📊 Exploratory Data Analysis

The dataset was explored using descriptive statistical measures including:

* Minimum and Maximum
* Mean
* Median
* Quartiles
* Standard Deviation
* Skewness
* Kurtosis
* Missing Values
* Unique Values
* Outlier Counts

These statistics help understand the distribution and overall quality of the sensor measurements before model development.

---

## 🔍 Outlier Detection

Outliers were initially identified using the **Interquartile Range (IQR)** technique.

The standard boundaries are:

```text
IQR = Q3 - Q1

Lower Bound = Q1 - 1.5 × IQR
Upper Bound = Q3 + 1.5 × IQR
```

Observations outside these boundaries are considered potential outliers.

---

## 🧹 Outlier Treatment – Winsorization

Instead of directly deleting extreme observations, **Winsorization** was applied to cap extreme values.

```python
winsorize(df[column], limits=[0.05, 0.05])
```

This approach limits the influence of extreme observations while retaining the records in the dataset.

---

## 🔗 Correlation & Feature Analysis

A correlation matrix and heatmap were used to examine relationships between numerical variables.

Correlation with the target variable **RH** was also analyzed separately to understand how individual features relate to Relative Humidity.

---

## ⚙️ Data Preprocessing

The preprocessing pipeline includes:

### Feature and Target Separation

```python
X = df.drop(columns=['RH'])
y = df['RH']
```

### Train-Test Split

The dataset was divided into:

* **80% Training Data**
* **20% Testing Data**

### Feature Scaling

**MinMaxScaler** was applied to transform the predictor variables onto a comparable scale.

---

## 🤖 Machine Learning Models

Four regression algorithms were evaluated:

### 1. Random Forest Regressor

An ensemble learning algorithm that combines multiple decision trees to generate robust predictions.

### 2. Extra Trees Regressor

An ensemble model that introduces additional randomization while constructing decision trees.

### 3. Decision Tree Regressor

A tree-based regression algorithm that learns nonlinear decision rules from the input features.

### 4. K-Nearest Neighbors Regressor

A distance-based algorithm that predicts values using observations closest to a new data point.

---

## 📈 Model Evaluation

Model performance was evaluated using the **R² Score**.

```python
R² = 1 - (SSres / SStot)
```

A higher R² score indicates that the model explains a greater proportion of variation in the target variable.

The project compares the R² scores of:

```text
Random Forest Regressor
Extra Trees Regressor
Decision Tree Regressor
K-Nearest Neighbors Regressor
```

This allows the models to be compared on the same test dataset.

---

## 📉 Elbow Method Analysis

The project also explores **K-Means clustering inertia** for different numbers of clusters.

Values of **K from 2 to 10** are evaluated and plotted using the Elbow Method.

This analysis helps identify how the structure of the feature space changes as the number of clusters increases.

---

## 🔬 Residual Analysis

Residuals were calculated as:

```text
Residual = Actual Value - Predicted Value
```

The distribution of residuals was visualized to inspect prediction errors and determine whether they are concentrated around zero.

---

## 🎯 Actual vs Predicted Analysis

Actual Relative Humidity values were compared with the predictions generated by the regression model.

A regression plot and reference line were used to visually evaluate how closely predictions correspond to the actual observations.

Predictions closer to the reference line indicate stronger predictive performance.

---

## 📂 Suggested Repository Structure

```text
Air-Quality-Prediction-ML/
│
├── README.md
├── airquality_index_predictionmodel.py
├── AirQualityUCI.xlsx
├── requirements.txt
│
├── images/
│   ├── correlation_heatmap.png
│   ├── target_correlation.png
│   ├── elbow_method.png
│   ├── residual_distribution.png
│   └── actual_vs_predicted.png
│
└── LICENSE
```

---

## 💡 Key Skills Demonstrated

This project demonstrates practical knowledge of:

* Python Programming
* Data Cleaning
* Exploratory Data Analysis
* Descriptive Statistics
* Outlier Detection
* Winsorization
* Feature Analysis
* Data Visualization
* Feature Scaling
* Machine Learning Regression
* Ensemble Learning
* Model Evaluation
* Residual Analysis
* Scikit-learn
* Pandas
* NumPy
* Matplotlib
* Seaborn

---

## 🚀 Future Improvements

The project can be extended by:

* Adding MAE, MSE and RMSE evaluation metrics.
* Performing cross-validation.
* Implementing hyperparameter tuning using GridSearchCV or RandomizedSearchCV.
* Adding feature importance analysis.
* Comparing baseline and optimized models.
* Creating a reusable Scikit-learn preprocessing pipeline.
* Deploying the final model through Streamlit or FastAPI.

---

## ⭐ Project Summary

This project demonstrates an **end-to-end machine learning regression workflow**, transforming raw air-quality sensor data into a predictive modeling pipeline through statistical analysis, outlier treatment, preprocessing, model comparison, and prediction diagnostics.

It highlights the practical application of **Python, statistical analysis, data visualization, and machine learning** to an environmental analytics problem.
