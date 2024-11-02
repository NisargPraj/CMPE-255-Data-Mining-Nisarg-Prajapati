# CRISP-DM Methodology Assignment: Gym Members' Exercise Tracking Analysis

## Overview
This assignment leverages the **CRISP-DM (Cross-Industry Standard Process for Data Mining)** methodology to analyze and model gym members' exercise tracking data. The goal is to identify key factors affecting members' exercise habits, such as attendance frequency and workout types, and to predict outcomes like BMI and calorie expenditure. CRISP-DM's structured, six-phase approach ensures a thorough understanding and analysis of the dataset, enabling meaningful insights and actionable outcomes.

## Methodology Phases

### 1. Business Understanding
   - **Objective**: Define the project's primary goal, which is to analyze and model exercise patterns among gym members to optimize health and fitness outcomes.
   - **Key Questions**: 
     - What factors contribute to members' regular gym attendance?
     - How do exercise types and duration impact BMI and calorie burn?

### 2. Data Understanding
   - **Dataset Overview**: The dataset includes demographic and exercise-specific attributes, such as `Age`, `Gender`, `Workout Type`, `Session Duration`, `Calories Burned`, `Workout Frequency`, and `BMI`.
   - **Exploration**: Initial exploratory data analysis (EDA) was conducted to assess distributions, detect outliers, and identify missing values.

### 3. Data Preparation
   - **Preprocessing**: Addressed missing values, encoded categorical variables, and scaled numerical data.
   - **Feature Engineering**: New features were created to capture exercise frequency patterns and variations in workout types.
   - **Final Prepared Data**: The cleaned dataset, ready for modeling, ensured comprehensive and high-quality data.

### 4. Modeling
   - **Model Selection**: Multiple models, including **Logistic Regression, Random Forest, and SVM**, were applied to predict outcomes such as calorie expenditure and BMI classification.
   - **Training and Evaluation**: Models were trained on the prepared dataset, and evaluation metrics (accuracy, precision, recall, and F1 score) were used to select the most effective model for predicting target outcomes.

### 5. Evaluation
   - **Model Performance**: The Random Forest model provided the best performance for predicting exercise-related outcomes.
   - **Insights**: Key findings included the importance of workout duration, exercise type, and workout frequency in predicting BMI and calorie burn.

### 6. Deployment
   - **Model Saving**: The best model was saved for future use, allowing for deployment in fitness tracking applications.
   - **Deliverables**: Provided Colab notebooks with code for each phase, model artifacts, a Medium article detailing the CRISP-DM application, and a research paper in LaTeX format.

## Colab Notebook and Medium Article
- [Google Colab Notebook](https://colab.research.google.com/drive/1sEZMhF6qH2surhEmtoJp5FfMJEFnsaVz?usp=sharing)
- [Medium Article](https://medium.com/@nisargprajapati281/maximizing-gym-member-engagement-a-data-mining-journey-using-the-crisp-dm-methodology-08f420930121)

## Deliverables
- **Colab Notebook**: Code implementing each CRISP-DM phase for the gym members' exercise tracking dataset.
- **Medium Article**: A comprehensive article explaining the CRISP-DM methodology as applied to this analysis.
- **Research Paper**: A detailed report in LaTeX format, summarizing methodology, results, and key insights.

## Conclusion
By following the CRISP-DM methodology, this assignment achieved a structured and effective analysis of gym members' exercise data. The resulting insights can assist gyms in tailoring their programs to better meet members' fitness goals, ultimately promoting healthier lifestyles.

