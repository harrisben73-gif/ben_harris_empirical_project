# Importing the necessary libraries for our data analysis

from pyexpat import model

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Importing libraries necessary for a casual forest analysis
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import statsmodels.api as sm


# Loading the cleaned datasets that we saved at the end of our data cleaning process into pandas DataFrames so that we can use them for our data analysis
merged_player_data = pd.read_csv('data_analysis/merged_player_data.csv')
merged_club_data = pd.read_csv('data_analysis/merged_club_data.csv')

# Removing Goalkeepers from the dataset as they have very different characteristics to outfield players and may skew our analysis
merged_player_data_noGK = merged_player_data[merged_player_data['Position_x'] != 'GK']

# Checking the columns of the dataset 
print(merged_player_data_noGK.columns)
# print(merged_club_data.columns)

# Starting the casual forest analysis 
Y = merged_player_data_noGK['Weekly Wages (GBP)']
X = merged_player_data_noGK[['Minutes', 'Goals (G) ', 'Assists (A) ', 'Yellow Cards ', 'Red Cards ', 'Fouls Commited ', 'Fouls Drawn ', 'Offsides', 'Crosses', 'Interceptions', 'Tackles Won ', 'Own Goals ', 'Penalties Scored (PK) ']]

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
# Therefore model shows predictions are off by about £56,296 on average, which is reseanable given the wage scale 
# The R squared of 0.0893 is low, which means 8.93% of the variance in the weekly wages can be explained by the model, which is not very good, but it is a start and we can try to improve it by adding more features or using a different model.

# Working on finding Average Treatment Effect (ATE) 

# Making the treatment effect binary for if their stats are above average or not 
merged_player_data_noGK['high_goals'] = (merged_player_data_noGK['Goals (G) '] > merged_player_data_noGK['Goals (G) '].mean()).astype(int)
merged_player_data_noGK['high_assists'] = (merged_player_data_noGK['Assists (A) '] > merged_player_data_noGK['Assists (A) '].mean()).astype(int)
merged_player_data_noGK['high_minutes'] = (merged_player_data_noGK['Minutes'] > merged_player_data_noGK['Minutes'].mean()).astype(int)
merged_player_data_noGK['high_fouls_drawn'] = (merged_player_data_noGK['Fouls Drawn '] > merged_player_data_noGK['Fouls Drawn '].mean()).astype(int)
merged_player_data_noGK['high_tackles_won'] = (merged_player_data_noGK['Tackles Won '] > merged_player_data_noGK['Tackles Won '].mean()).astype(int)
merged_player_data_noGK['high_interceptions'] = (merged_player_data_noGK['Interceptions'] > merged_player_data_noGK['Interceptions'].mean()).astype(int)
merged_player_data_noGK['forward'] = (merged_player_data_noGK['Position_x'] == 'FW').astype(int)

# Now we can use the Random Forest model to estimate the ATE of being a forward on weekly wages, controlling for the other features
X_ate = merged_player_data_noGK[['high_goals', 'high_assists', 'high_minutes', 'high_fouls_drawn', 'high_tackles_won', 'high_interceptions', 'forward']]
Y_ate = merged_player_data_noGK['Weekly Wages (GBP)']

model = sm.OLS(Y_ate, sm.add_constant(X_ate)).fit()
print(model.summary2())
# We can see that some stats have higher coefficients than others, showing their importance 
# This is further backed up by looking at their p values 
# But R Squared still relatively low at 0.162 




