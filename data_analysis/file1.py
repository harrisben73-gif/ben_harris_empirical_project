# Importing necessary libraries

import pandas as pd
import numpy as np

# Loading the cleaned datasets that we saved at the end of our data cleaning process into pandas DataFrames so that we can use them for our data analysis
merged_player_data = pd.read_csv('data_analysis/merged_player_data.csv')
merged_club_data = pd.read_csv('data_analysis/merged_club_data.csv')

# Checking the first few rows of each dataset to verify that they have been loaded correctly and to understand their structure
print(merged_player_data.head())
print(merged_club_data.head())