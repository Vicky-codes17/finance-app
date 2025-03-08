import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def train_model(data):
    if data.empty:
        print("No data available for training.")
        return
    
    data["Month"] = pd.to_datetime(data["Date"]).dt.month
    X = data[["Month"]]
    y = data["Amount"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    joblib.dump(model, "finance_model.pkl")
    print("Model trained and saved successfully!")
