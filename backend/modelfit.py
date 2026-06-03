import numpy as np 
import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib
# Load the cleaned data
data = 'cleaned_data.csv'  # Yeh tumhara cleaned data hai
df = pd.read_csv(data)
model=linear_model.LinearRegression()
# Define the features and target variable   
X=df.drop('SalePrice', axis=1)  # Features (independent variables)
y=df['SalePrice']  # Target variable (dependent variable)
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Fit the linear regression model to the training data
model.fit(X_train, y_train)
# Predict the target variable for the test set
y_pred = model.predict(X_test)
# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"R^2 Score: {r2}")
rmse = np.sqrt(mse)
print(f"Root Mean Squared Error (RMSE): {rmse}")
print("model created successfully and evaluated")
print("now we will save the model for future use")
joblib.dump(model, 'house_price_model.pkl')
print("Model successfully saved as house_price_model.pkl!")