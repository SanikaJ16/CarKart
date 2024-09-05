# Import the required libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline

# Read the dataset
car = pd.read_csv('Cleaned.csv')

# Data Cleaning
# (Similar to the data cleaning process you performed for the lasso regression model)

# Define the features (X) and the target (y)
X = car.drop(columns='Price')
y = car['Price']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Perform one-hot encoding
ohe = OneHotEncoder()
ohe.fit(X[['name', 'company', 'fuel_type']])

# Define the column transformer
column_trans = make_column_transformer(
    (OneHotEncoder(categories=ohe.categories_), ['name', 'company', 'fuel_type']),
    remainder='passthrough'
)

# Create and train the Decision Tree model
decision_tree = DecisionTreeRegressor()
pipe = make_pipeline(column_trans, decision_tree)
pipe.fit(X_train, y_train)

# Make predictions
y_pred = pipe.predict(X_test)

# Calculate R-squared
r2 = r2_score(y_test, y_pred)
print(f"R-squared value: {r2}")

# Save the model to a file
import pickle
pickle.dump(pipe, open('DecisionTreeModel.pkl', 'wb'))

# Make a prediction using the saved model
# Create a DataFrame for prediction with a placeholder 'Unnamed: 0' column
prediction_df = pd.DataFrame([['Maruti Suzuki Swift', 'Maruti', 2019, 100, 'Petrol']],
                            columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'])
# Add a placeholder 'Unnamed: 0' column
prediction_df['Unnamed: 0'] = 0

# Make predictions
prediction = pipe.predict(prediction_df)
print(f"Predicted Price: {prediction}")