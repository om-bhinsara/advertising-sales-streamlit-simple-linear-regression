import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

# Load data
df = pd.read_csv(r"D:\OM\Codes And Projects\Data Science Projects\ML Model Implementations\1) Simple Linear Regression\Project 2\data\Advertising.csv")

X = df[['TV']]
y = df['Sales']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
joblib.dump(model, "model/linear_regression.pkl")

print("Model trained and saved successfully.")
