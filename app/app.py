import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

# Load model
model = joblib.load(r"D:\OM\Codes And Projects\Data Science Projects\ML Model Implementations\1) Simple Linear Regression\Project 2\model\linear_regression.pkl")

st.set_page_config(page_title="Advertising Sales Predictor", layout="centered")

st.title("📊 Advertising Sales Prediction")
st.write("Predict **Sales** based on **TV Advertising Budget** using Linear Regression.")

# User input
tv_budget = st.slider(
    "Select TV Advertising Budget",
    min_value=0.0,
    max_value=300.0,
    step=1.0
)

# Prediction
prediction = model.predict([[tv_budget]])[0]

st.subheader("📈 Predicted Sales")
st.success(f"Estimated Sales: **{prediction:.2f} units**")

# Explanation
st.markdown("""
### 🧠 How this works
- The model learned a linear relationship: **Sales = m × TV + c**
- This prediction represents the **average expected sales**
- Actual sales may vary due to other factors (Radio, Newspaper, market conditions)
""")

# Visualization
st.subheader("📉 Regression Line")

# Load full dataset for visualization
df = pd.read_csv(r"D:\OM\Codes And Projects\Data Science Projects\ML Model Implementations\1) Simple Linear Regression\Project 2\data\Advertising.csv")
X = df[['TV']]
y = df['Sales']
y_pred = model.predict(X)

fig, ax = plt.subplots()
ax.scatter(X, y, label="Actual Data", alpha=0.6)
ax.plot(X, y_pred, color="red", label="Regression Line")
ax.scatter(tv_budget, prediction, color="green", s=100, label="Your Prediction")
ax.set_xlabel("TV Advertising Budget")
ax.set_ylabel("Sales")
ax.legend()

st.pyplot(fig)
