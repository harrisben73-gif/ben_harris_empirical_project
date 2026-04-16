# Importing the necessary libraries for our data analysis

from pyexpat import model

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Importing libraries necessary for a casual forest analysis
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


# Loading the cleaned datasets that we saved at the end of our data cleaning process into pandas DataFrames so that we can use them for our data analysis
merged_player_data = pd.read_csv('data_analysis/merged_player_data.csv')
merged_club_data = pd.read_csv('data_analysis/merged_club_data.csv')

# Checking the columns of the dataset 
# print(merged_player_data.columns)
# print(merged_club_data.columns)

# Starting the casual forest analysis 
Y = merged_player_data['Weekly Wages (GBP)']
X = merged_player_data[['Minutes', 'Goals (G) ', 'Assists (A) ', 'Yellow Cards ', 'Red Cards ', 'Fouls Commited ', 'Fouls Drawn ', 'Offsides', 'Crosses', 'Interceptions', 'Tackles Won ', 'Own Goals ', 'Penalties Scored (PK) ']]

# Splitting the data into training and testing sets for our casual forest analysis
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Initializing the Random Forest Regressor for our casual forest analysis
rf = RandomForestRegressor(n_estimators=100, random_state=42)

# Fitting the model to the training data
model = rf.fit(X_train, Y_train)

# Make predictions 
y_pred = model.predict(X_test)

# Evaluating the model
from sklearn.metrics import mean_squared_error, r2_score
mse = mean_squared_error(Y_test, y_pred)
r2 = r2_score(Y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"Root Mean Squared Error: {np.sqrt(mse)}")
print(f"R^2 Score: {r2}")
# Therefore model shows predictions are off by about £18,500 on average, which is reseanable given the wage scale 
# The R squared of 0.0879 is low, which means 8.79% of the variance in the weekly wages can be explained by the model, which is not very good, but it is a start and we can try to improve it by adding more features or using a different model.
