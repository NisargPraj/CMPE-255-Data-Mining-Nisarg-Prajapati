# KDD Methodology Assignment: Diabetes Prediction Using Data Mining

## Overview
This assignment applies the **KDD (Knowledge Discovery in Databases)** methodology to analyze a diabetes dataset with the goal of predicting diabetes onset based on key health indicators. The KDD process allows for a systematic approach to discovering patterns and relationships within the dataset, following a sequence of well-defined phases: **Selection, Preprocessing, Transformation, Data Mining, and Interpretation/Evaluation**.

## Methodology Phases

### 1. Selection
   - **Objective**: Identify relevant data to predict diabetes onset.
   - **Dataset Overview**: The dataset includes attributes relevant to diabetes diagnosis, such as `Age`, `BMI`, `Blood Pressure`, `Glucose Level`, and `Insulin Level`.
   - **Target Variable**: The `Outcome` variable indicates whether the patient is diabetic (1) or non-diabetic (0).

### 2. Preprocessing
   - **Handling Missing Values**: Filled missing values using mean imputation to ensure data completeness.
   - **Encoding Categorical Variables**: Encoded any categorical features for use in the models.
   - **Scaling**: Standardized numerical features such as `BMI`, `Glucose Level`, and `Blood Pressure` to improve model performance.

### 3. Transformation
   - **Dimensionality Reduction**: Applied **Principal Component Analysis (PCA)** to reduce feature space dimensionality while retaining 95% of the variance.
   - **Feature Engineering**: Created transformed components that minimized redundancy in the data, improving efficiency and accuracy in modeling.

### 4. Data Mining
   - **Model Selection**: Tested several classification models, including **Logistic Regression, Random Forest, and Support Vector Machine (SVM)**, to predict diabetes onset.
   - **Training and Evaluation**: Evaluated models based on accuracy, precision, recall, and F1 score, selecting the model with the highest predictive performance.

### 5. Interpretation/Evaluation
   - **Model Performance**: The Random Forest Classifier achieved the best performance, providing balanced metrics and accuracy in predicting diabetes onset.
   - **Insights**: Important features identified include `Glucose Level`, `BMI`, and `Age`, which align with known diabetes risk factors.

## Colab Notebook and Medium Article
- [Google Colab Notebook](https://colab.research.google.com/drive/133zR9SCQmnILrJjTGP0yXZyM9z3JJuFO?usp=sharing)
- [Medium Article](https://medium.com/@nisargprajapati281/predicting-diabetes-with-data-mining-a-deep-dive-using-the-kdd-methodology-8e3ca09efef1)


## Conclusion
By implementing the KDD methodology, this assignment achieved accurate and interpretable results in predicting diabetes onset. The systematic approach helped reveal critical health indicators affecting diabetes, supporting healthcare professionals in developing preventive measures and personalized treatments.


