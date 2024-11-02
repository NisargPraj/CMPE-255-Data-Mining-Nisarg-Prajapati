# SEMMA Methodology Assignment: Analyzing and Predicting Student Sleep Quality

## Overview
This assignment utilizes the **SEMMA (Sample, Explore, Modify, Model, Assess)** methodology to analyze and predict sleep quality among students based on their habits and lifestyle factors. SEMMA provides a structured data mining approach, allowing for a systematic examination of sleep data to uncover insights into factors such as screen time, study hours, caffeine intake, and sleep duration.

## Methodology Phases

### 1. Sample
   - **Objective**: Build a representative dataset that captures sleep and lifestyle patterns of students.
   - **Dataset Overview**: The dataset includes key variables like `Sleep Duration`, `Study Hours`, `Screen Time`, `Caffeine Intake`, `Physical Activity`, and `Sleep Quality`.
   - **Sampling**: Ensured the dataset was complete and representative of the target population, providing a reliable basis for exploration and modeling.

### 2. Explore
   - **Exploratory Data Analysis**: Analyzed distributions and relationships within the dataset to uncover initial patterns.
   - **Key Observations**:
     - Positive correlation between `Sleep Duration` and `Sleep Quality`.
     - Negative relationships between `Screen Time`, `Caffeine Intake`, and `Sleep Quality`.
     - A correlation heatmap identified influential variables like `Physical Activity`, `Sleep Duration`, and `Screen Time`.

### 3. Modify
   - **Data Preparation**: Addressed missing values, created new features, and scaled numerical features.
   - **Feature Engineering**: Created the `Sleep Duration Difference` feature, capturing the variation in sleep duration between weekdays and weekends.
   - **Scaling**: Standardized all numerical features for improved comparability in model training.

### 4. Model
   - **Model Selection**: Trained multiple regression models, including **Linear Regression, Random Forest Regressor, and Support Vector Regressor (SVR)**, to predict `Sleep Quality`.
   - **Model Evaluation**: Assessed model performance using Mean Absolute Error (MAE), Mean Squared Error (MSE), and R² Score, with the Random Forest Regressor providing the best performance.

### 5. Assess
   - **Model Interpretation**: Random Forest feature importance identified `Sleep Duration`, `Screen Time`, and `Physical Activity` as key factors influencing sleep quality.
   - **Visualization**: An actual vs. predicted plot illustrated that the Random Forest model closely approximated true sleep quality scores.
   - **Key Insights**: Consistent sleep routines, reduced screen time before bed, and regular physical activity emerged as significant predictors of high sleep quality.

## Colab Notebook Link
- [Google Colab Notebook](https://colab.research.google.com/drive/1KepACOIoWJIyGTcoI3JHZ-J3_1xi245k?usp=sharing)
- [Medium Article](https://medium.com/@nisargprajapati281/unlocking-better-sleep-a-data-science-approach-using-semma-to-analyze-student-sleep-patterns-513ae2ca4765)

## Conclusion
By following the SEMMA methodology, this assignment provided a data-driven understanding of the factors impacting student sleep quality. The findings indicate that lifestyle adjustments, such as reducing screen time and maintaining consistent sleep patterns, can significantly improve sleep quality, supporting healthier habits among students.


