# Importing the necessary libraries 

import pandas as pd
import numpy as np

# Loading the cleaned datasets that we saved at the end of our data cleaning process into pandas DataFrames so that we can use them for our data analysis
merged_player_data = pd.read_csv('data_analysis/merged_player_data.csv')
merged_club_data = pd.read_csv('data_analysis/merged_club_data.csv')

# Checking the first few rows of each dataset to verify that they have been loaded correctly and to understand their structure
# print(merged_player_data.head())
# print(merged_club_data.head())

# print(merged_player_data.info())

# Summary statistics for the merged_player_data dataset - wage 
print('=' * 40)
print('Summary statistics for Weekly Wages (GBP):')
print('=' * 40) 
print(f'Mean: £{merged_player_data["Weekly Wages (GBP)"].mean():.2f}')
print(f'Median: £{merged_player_data["Weekly Wages (GBP)"].median():.2f}')
print(f'Mode: £{merged_player_data["Weekly Wages (GBP)"].mode().iloc[0]:.2f}')
print(f'Variance: £{merged_player_data["Weekly Wages (GBP)"].var():.2f}')
print(f'Standard Deviation: £{merged_player_data["Weekly Wages (GBP)"].std():.2f}')
max_row = merged_player_data.loc[merged_player_data['Weekly Wages (GBP)'].idxmax()]
print(f'Maximum: {max_row["Player"]} with £{max_row["Weekly Wages (GBP)"]} per week')
min_row = merged_player_data.loc[merged_player_data['Weekly Wages (GBP)'].idxmin()]
print(f'Minimum: {min_row["Player"]} with £{min_row["Weekly Wages (GBP)"]} per week')
print('=' * 40)


print('    ')
# Finding a couple modes for other data 
print('=' * 40)
print('Most common values:')
print('=' * 40)
print(f'Most common position: {merged_player_data["Position_x"].mode().iloc[0]}')
print(f'Most common nationality: {merged_player_data["Nation_x"].mode().iloc[0]}')
print('=' * 40)
