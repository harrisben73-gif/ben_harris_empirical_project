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

# For our first but of data analysis we will be looking at the relationship between weekly wages and position 
# We will use a boxplot to visualize the distribution of weekly wages for each position in the dataset
plt.figure(figsize=(12, 6))
sns.boxplot(data=merged_player_data, x='Position_x', y='Weekly Wages (GBP)', order=['GK', 'DF', 'MF', 'FW'], showfliers=False)
plt.title('Distribution of Weekly Wages by Position')
plt.xlabel('Position')
plt.ylabel('Weekly Wages (GBP)')
plt.xticks(rotation=45)
plt.savefig('data_analysis/wages_by_position_boxplot.png')
plt.show()

# Can see that as positions get higher up the pitch on average wages do rise 
print('=' * 40)
print('Average Weekly Wages by position:')
print('=' * 40)
positions = merged_player_data.groupby('Position_x')['Weekly Wages (GBP)'].mean().round(2).sort_values(ascending=False).rename_axis(None)
for pos, wage in positions.items():
    print(f' {pos:<6} £{wage:>10,.2f}')
print('=' * 40)
# This point is further reinforced by looking at the average weekly wages for each position, we can see that on average goalkeepers earn the least, followed by defenders, then midfielders and finally forwards who earn the most on average. This is likely due to the fact that forwards are often the most high profile players in a team and are responsible for scoring goals, which is often seen as the most important aspect of the game. Goalkeepers on the other hand are often seen as less glamorous and are not involved in scoring goals, which may explain why they earn less on average.

