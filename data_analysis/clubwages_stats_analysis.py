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


# Ranking clubs based on certain key performance statistics 
# Goals
merged_club_data['goals_rank'] = merged_club_data['Goals (G) '].rank(ascending=False, method='min').astype(int)
ranked_clubs_goals = merged_club_data.sort_values(by='goals_rank')
# print(ranked_clubs_goals[['Squad', 'Goals (G) ', 'goals_rank']])

# Assists
merged_club_data['assists_rank'] = merged_club_data['Assists (A) '].rank(ascending=False, method='min').astype(int)
ranked_clubs_assists = merged_club_data.sort_values(by='assists_rank')
# print(ranked_clubs_assists[['Squad', 'Assists (A) ', 'assists_rank']])

# Average Possession
merged_club_data['avpossession_rank'] = merged_club_data['Average Possession '].rank(ascending=False, method='min').astype(int)
ranked_clubs_possession = merged_club_data.sort_values(by='avpossession_rank')
# print(ranked_clubs_possession[['Squad', 'Average Possession ', 'avpossession_rank']])

# Yellow Cards
merged_club_data['yellow_rank'] = merged_club_data['Yellow Cards '].rank(ascending=True, method='min').astype(int)
ranked_clubs_yellow = merged_club_data.sort_values(by='yellow_rank')
# print(ranked_clubs_yellow[['Squad', 'Yellow Cards ', 'yellow_rank']])

# Red Cards
merged_club_data['red_rank'] = merged_club_data['Red Cards '].rank(ascending=True, method='min').astype(int)
ranked_clubs_red = merged_club_data.sort_values(by='red_rank')
# print(ranked_clubs_red[['Squad', 'Red Cards ', 'red_rank']])

# Fouls Commited
merged_club_data['foulscommited_rank'] = merged_club_data['Fouls Commited '].rank(ascending=True, method='min').astype(int)
ranked_clubs_foulscommited = merged_club_data.sort_values(by='foulscommited_rank')
# print(ranked_clubs_foulscommited[['Squad', 'Fouls Commited ', 'foulscommited_rank']])

# Fouls Drawn
merged_club_data['foulsdrawn_rank'] = merged_club_data['Fouls Drawn '].rank(ascending=False, method='min').astype(int)
ranked_clubs_foulsdrawn = merged_club_data.sort_values(by='foulsdrawn_rank')
# print(ranked_clubs_foulsdrawn[['Squad', 'Fouls Drawn ', 'foulsdrawn_rank']])

# Crosses
merged_club_data['crosses_rank'] = merged_club_data['Crosses'].rank(ascending=False, method='min').astype(int)
ranked_clubs_crosses = merged_club_data.sort_values(by='crosses_rank')
# print(ranked_clubs_crosses[['Squad', 'Crosses', 'crosses_rank']])

# Interceptions
merged_club_data['interceptions_rank'] = merged_club_data['Interceptions '].rank(ascending=False, method='min').astype(int)
ranked_clubs_interceptions = merged_club_data.sort_values(by='interceptions_rank')
# print(ranked_clubs_interceptions[['Squad', 'Interceptions ', 'interceptions_rank']])

# Tackles Won
merged_club_data['tackles_rank'] = merged_club_data['Tackles Won '].rank(ascending=False, method='min').astype(int)
ranked_clubs_tackles = merged_club_data.sort_values(by='tackles_rank')
# print(ranked_clubs_tackles[['Squad', 'Tackles Won ', 'tackles_rank']])


# Finding the average overall rank for these clubs with the past 10 stats and then ranking them by this average rank to see which clubs are the best overall in terms of these stats
merged_club_data['average_rank'] = merged_club_data[['goals_rank', 'assists_rank', 'avpossession_rank', 'yellow_rank', 'red_rank', 'foulscommited_rank', 'foulsdrawn_rank', 'crosses_rank', 'interceptions_rank', 'tackles_rank']].mean(axis=1).rank(ascending=True, method='min').round(2).astype(int)
ranked_clubs_average = merged_club_data.sort_values(by='average_rank')
print(ranked_clubs_average[['Squad', 'average_rank']])

# Comparing this average_rank to the total weekly wage bill of each club 
plt.figure(figsize=(12, 6))
sns.scatterplot(data=merged_club_data, x='average_rank', y='Weekly Wages (GBP)', hue='Squad', palette='tab10')
plt.title('Average Rank vs Weekly Wages')
plt.xlabel('Average Rank of Key Stats')
plt.ylabel('Weekly Wages (GBP) in millions')
plt.legend(fontsize=8, markerscale=1.5, loc='upper right', bbox_to_anchor=(1.0, 1.0))
for i, row in merged_club_data.iterrows():
    plt.annotate(row['Squad'], (row['average_rank'], row['Weekly Wages (GBP)']), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
plt.show()
# Can see a clear negative correlation between average rank and weekly wage bill 