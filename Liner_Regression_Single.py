import time
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Function to measure execution time
def measure_execution_time(func):
    start_time = time.time()
    func()
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution Time:", execution_time, "seconds")

# Function to load data and perform preprocessing in the single-threaded version
def process_data_single_threaded():
    data = pd.read_csv("Real_Estate_HW6/data_without_location.csv")
    
    # Preprocessing steps...
    data = data.dropna(subset=["Assessed Value", "Sale Amount"])

    return data

# Function to train model and evaluate in the single-threaded version
def train_model_single_threaded(data):
    # Model training and evaluation steps...
    # Split data into features (X) and target variable (y)
    X = data[['Assessed Value', 'Sale Amount', 'List Year', 'Sales Ratio']]
    y = data['Sale Amount']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)

    # Evaluate model
    mse_train = mean_squared_error(y_train, y_pred_train)
    mse_test = mean_squared_error(y_test, y_pred_test)

    r2_train = r2_score(y_train, y_pred_train)
    r2_test = r2_score(y_test, y_pred_test)
    
    print(f"Train MSE: {mse_train}")
    print(f"Test MSE: {mse_test}")
    print(f"Train R^2 Score: {r2_train}")
    print(f"Test R^2 Score: {r2_test}")

    # Visualization
    # Visualize actual vs. predicted values
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred_test, alpha=0.3)
    plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], 'r--', lw=2)
    plt.xlabel('Actual Sale Amount')
    plt.ylabel('Predicted Sale Amount')
    plt.title('Actual vs. Predicted Sale Amount (Linear Regression)')
    plt.show()

if __name__ == "__main__":
    print("Single-threaded Version:")
    data = process_data_single_threaded()
    measure_execution_time(lambda: train_model_single_threaded(data))

