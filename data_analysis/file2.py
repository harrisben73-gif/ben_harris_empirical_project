# Importing necessary libraries 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Loading the cleaned datasets that we saved at the end of our data cleaning process into pandas DataFrames so that we can use them for our data analysis
merged_player_data = pd.read_csv('data_analysis/merged_player_data.csv')
merged_club_data = pd.read_csv('data_analysis/merged_club_data.csv')

# Checking the first few rows of each dataset to verify that they have been loaded correctly and to understand their structure
# print(merged_player_data.head())
# print(merged_club_data.head())

# Checking the columns of merged_club_data to see if there are any columns that we can use for our data analysis
# print(merged_club_data.columns)

# Ranking clubs by certain stats such as goals scored, assists, points etc

# ranked_clubs_goals = merged_club_data.sort_values(by='Goals (G) ', ascending=False)
# print(ranked_clubs_goals[['Squad', 'Goals (G) ']])

merged_club_data['Rank'] = merged_club_data['Goals (G) '].rank(ascending=False, method='min').astype(int)
ranked_clubs_goals = merged_club_data.sort_values(by='Rank')
print(ranked_clubs_goals[['Squad', 'Goals (G) ', 'Rank']])

ranked_clubs_assists = merged_club_data.sort_values(by='Assists (A) ', ascending=False)
print(ranked_clubs_assists[['Squad', 'Assists (A) ']])