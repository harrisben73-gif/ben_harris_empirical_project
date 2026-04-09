# To complete my small analysis on goalkeepers I will be using SQL, Pandas, Matplotlib and Seaborn to analyze the data and find any interesting insights about the goalkeepers in the dataset. I will be looking at the average wages of the goalkeepers, the top 10 highest paid goalkeepers, and the correlation between the weekly wages of the goalkeepers and their save percentage. I will also be plotting a scatter plot of the weekly wages of the goalkeepers against their save percentage to visually inspect the relationship between the two variables.

import pandas as pd 
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns


# Creating a connection to the SQLite database where the data is stored
# Reading in the data from the database into pandas dataframes for analysis
df = pd.read_csv('goalkeeper_analysis/data/clean/gk_combined.csv')
df = df.dropna()
conn = sqlite3.connect('goalkeeper_analysis/sqlite/gk_database.db')
df.to_sql('gk_combinedsql', conn, if_exists='replace', index=False)


# Printing the first 5 rows of the SQL table to verify it has been created correctly
# print(pd.read_sql_query("SELECT * FROM gk_combinedsql LIMIT 5", conn))

# Finding the average wage of all the goalkeepers in the dataset
avg_wage = pd.read_sql_query("""SELECT AVG("Weekly Wages") AS avg_wage FROM gk_combinedsql""", conn)
print(f"The average weekly wage of the goalkeepers in the dataset is: £{round(avg_wage['avg_wage'].iloc[0])}")


# Finding the top 10 highest paid goalkeepers in the dataset
# top_paid_gks = pd.read_sql_query("""SELECT Player, Squad_x, "Weekly Wages" FROM gk_combinedsql ORDER BY "Weekly Wages" DESC LIMIT 10""", conn)
# print("The top 10 highest paid goalkeepers in the dataset are:", top_paid_gks.values.tolist())


# Finding the top 10 goalkeepers by save percentage in the dataset
# stats_df = pd.read_csv('goalkeeper_analysis/data/processed/gkstats_clean.csv')
# print(stats_df.columns)
# print(stats_df.head())


# Checking that Saves and Save Percantage columns are numeric and not strings, if they are strings I will need to convert them to numeric values before I can perform any calculations on them
print(df[['Player', 'Saves', 'Save Percentage ']].head(26))


# Trying to find a correlation between the weekly wages of the goalkeepers and their save percentage, I will use the Pearson correlation coefficient for this
correlation = df['Weekly Wages'].corr(df['Save Percentage '])
print(f"The correlation between weekly wages and save percentage is: {correlation}")
# We can see that there is a very weak positive correlation between the two variables, which suggests that there is not a strong relationship between the weekly wages of the goalkeepers and their save percentage
# But none the less still a correlation 

# Further developing this analysis by plotting a scatter plot of the weekly wages of the goalkeepers against their save percentage to visually inspect the relationship between the two variables
plt.figure(figsize=(10, 6))
sns.regplot(data=df, x='Weekly Wages', y='Save Percentage ')
plt.title('Relationship between Weekly Wages and Save Percentage')
plt.xlabel('Weekly Wages (£)')
plt.ylabel('Save Percentage (%)')
plt.show()

