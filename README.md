# 📊 Advertising Sales Prediction using Linear Regression

This project demonstrates an **end-to-end Machine Learning workflow** by predicting **product sales** based on **TV advertising budget** using **Simple Linear Regression**, and deploying the trained model using a **Streamlit web application**.

The project focuses on **correct ML methodology**, model interpretation, and practical deployment rather than only achieving high accuracy.

---

## 📌 Project Overview

- Build a **Simple Linear Regression** model
- Learn how linear regression works mathematically and visually
- Understand why feature quality matters more than algorithms
- Integrate a trained ML model with a **Streamlit frontend**
- Push a complete ML project to GitHub

---

## 🎯 Problem Statement

> Predict **Sales** given a **TV advertising budget**.

This problem is chosen because it has a **strong linear relationship**, making it ideal for understanding how linear regression behaves when assumptions are reasonably satisfied.

---

## 📊 Dataset

- **Source**: Advertising Dataset (public ML dataset)
- **Records**: 200
- **Features**:
  - `TV` – Advertising budget spent on TV
  - `Sales` – Product sales

For learning purposes, only the `TV` feature is used.

---

## 🧹 Data Preprocessing

- Verified data integrity (no missing values)
- Selected a single strong feature (`TV`)
- No feature scaling required (single-feature linear regression)
- Dataset is already clean and well-structured

---

## 🤖 Model Training

- Algorithm: **Simple Linear Regression**
- Objective: Learn a relationship of the form:

\[
Sales = m \times TV + c
\]

- Training performed using scikit-learn
- Model saved and reused in the frontend (no retraining in UI)

---

## 📈 Model Evaluation

The model was evaluated using standard regression metrics:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

The results show a **strong linear relationship**, validating the suitability of linear regression for this dataset.

---

## 📊 Visualizations

The following visualizations were used to understand model behavior:

- TV Budget vs Sales (linearity check)
- Regression Line visualization
- Actual vs Predicted Sales plot
- Residuals vs TV Budget plot

These plots help interpret **model accuracy, error patterns, and assumptions**.

---

## 🌐 Streamlit Web Application

A Streamlit app was built to:

- Take user input for **TV advertising budget**
- Predict **expected sales**
- Visualize the regression line and prediction point
- Explain how the model works in simple terms

---   

## 📁 Project Structure
📦 **advertising-sales-streamlit-simple-linear-regression**
 ┣ 📂 data
 ┃ ┗ 📄 Advertising.csv
 ┣ 📂 notebooks
 ┃ ┗ 📄 advertising_sales_analysis.ipynb
 ┣ 📂 app
 ┃ ┗ 📄 app.py
 ┣ 📂 model
 ┃ ┗ 📄 linear_regression.pkl
 ┣ 📄 train_model.py
 ┣ 📄 requirements.txt
 ┗ 📄 README.md


 ## 📁 Project Structure
📦 **student-performance-analysis**  
 ┣ 📂 data  
 ┣ 📂 notebooks  
 ┣ 📄 README.md  
 ┗ 📄 requirements.txt  

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- scikit-learn
- Matplotlib
- Streamlit
 
---

## ✅ Key Learnings

- Linear regression learns an average trend, not exact outcomes
- Feature quality impacts performance more than model choice
- Visualizations are essential for understanding model behavior
- Simple models can be powerful when assumptions are satisfied
- End-to-end ML projects include deployment, not just training
