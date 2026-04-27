# To complete my small analysis on goalkeepers I will be using SQL, Pandas, Matplotlib and Seaborn to analyze the data and find any interesting insights about the goalkeepers in the dataset. I will be looking at the average wages of the goalkeepers, the top 10 highest paid goalkeepers, and the correlation between the weekly wages of the goalkeepers and their save percentage. I will also be plotting a scatter plot of the weekly wages of the goalkeepers against their save percentage to visually inspect the relationship between the two variables.

from sre_constants import IN

import pandas as pd 
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns


# Creating a connection to the SQLite database where the data is stored
# Reading in the data from the database into pandas dataframes for analysis
conn = sqlite3.connect('goalkeeper_analysis/sqlite/gk_database.db')
df = pd.read_csv('goalkeeper_analysis/data/clean/gk_combined.csv')
df.to_sql('gk_combinedsql', conn, if_exists='replace', index=False)
df = df.dropna()


# Printing the first 5 rows of the SQL table to verify it has been created correctly
# print(pd.read_sql_query("SELECT * FROM gk_combinedsql LIMIT 5", conn))

# Finding the average wage of all the goalkeepers in the dataset
avg_wage = pd.read_sql_query("""SELECT AVG("Weekly Wages") AS avg_wage FROM gk_combinedsql""", conn)
# print(f"The average weekly wage of the goalkeepers in the dataset is: £{round(avg_wage['avg_wage'].iloc[0])}")

# Finding the sum of all weekly wages of the goalkeepers in the dataset
total_wages = pd.read_sql_query("""SELECT SUM("Weekly Wages") AS total_wages FROM gk_combinedsql""", conn)
# print(f"The total weekly wages of all the goalkeepers in the dataset is: £{total_wages['total_wages'].iloc[0]:,.2f}")

# Finding the top 10 highest paid goalkeepers in the dataset
# top_paid_gks = pd.read_sql_query("""SELECT Player, Squad_x, "Weekly Wages" FROM gk_combinedsql ORDER BY "Weekly Wages" DESC LIMIT 10""", conn)
# print("The top 10 highest paid goalkeepers in the dataset are:", top_paid_gks.values.tolist())


# stats_df = pd.read_csv('goalkeeper_analysis/data/processed/gkstats_clean.csv')
# print(stats_df.columns)
# print(stats_df.head())


# Checking that Saves and Save Percantage columns are numeric and not strings, if they are strings I will need to convert them to numeric values before I can perform any calculations on them
# print(df[['Player', 'Saves', 'Save Percentage ']].head(26))


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
plt.ylabel('Save Percentage (%)')#
plt.savefig('goalkeeper_analysis/weeklywages_savepercentage.png')
# plt.show()

# Using SQL to group and aggregate goalkeepers by whether they are in a big 6 club or not 
big_6_avg_wage = pd.read_sql_query("""
    SELECT Squad_x, AVG("Weekly Wages") AS avg_wage 
    FROM gk_combinedsql 
    WHERE Squad_x IN ('Manchester City', 'Liverpool', 'Chelsea', 'Tottenham Hotspur', 'Arsenal', 'Manchester Utd')
    GROUP BY Squad_x
    ORDER BY avg_wage DESC                       
""", conn)
# print("Average weekly wages of goalkeepers in the big 6 clubs:")
# print(big_6_avg_wage)

# Now finding the overal big 6 combined average wage for goalkeepers
big_6_combined = pd.read_sql_query("""
    SELECT AVG("Weekly Wages") AS avg_wage
    FROM gk_combinedsql
    WHERE Squad_x IN ('Manchester City', 'Liverpool', 'Chelsea', 'Tottenham Hotspur', 'Arsenal', 'Manchester Utd')
""", conn)
print(f"Overall average weekly wage of goalkeepers in the big 6 clubs: £{big_6_combined['avg_wage'][0]:,.2f}")

# Now finding the overall average wage for goalkeepers in the dataset that are not in the big 6 clubs 
non_big_6_combined = pd.read_sql_query("""
    SELECT AVG("Weekly Wages") AS avg_wage
    FROM gk_combinedsql
    WHERE Squad_x NOT IN ('Manchester City', 'Liverpool', 'Chelsea', 'Tottenham Hotspur', 'Arsenal', 'Manchester Utd')  
""", conn)
print(f"Overall average weekly wage of goalkeepers not in the big 6 clubs: £{non_big_6_combined['avg_wage'][0]:,.2f}")
# we can see that the average weekly wage of goalkeepers in the big 6 clubs is significantly higher than the average weekly wage of goalkeepers not in the big 6 clubs, which suggests that being in a big 6 club has a significant impact on the wages of goalkeepers.

# Finding the youngest and oldest goalkeepers in the dataset and their respective ages
# This is so we can correlate with minutes played to see a potential relationship 
youngest_gk = pd.read_sql_query("""
    SELECT Player, Age_x
    FROM gk_combinedsql
    ORDER BY Age_x ASC
    LIMIT 1
""", conn)

oldest_gk = pd.read_sql_query("""
    SELECT Player, Age_x
    FROM gk_combinedsql
    ORDER BY Age_x DESC
    LIMIT 1
""", conn)

# Printing this output in a nice format 
print('=' * 40)
print('GOALKEEPER AGE ANALYSIS')
print('=' * 40)
print(f"Youngest: {youngest_gk['Player'][0]} (Age {youngest_gk['Age_x'][0]})")
print(f"Oldest: {oldest_gk['Player'][0]} (Age {oldest_gk['Age_x'][0]})")
print('=' * 40)

# Now creating a histogram to visualize the distribution of ages of the goalkeepers in the dataset
plt.figure(figsize=(10, 6))
plt.hist(df['Age_clean'], bins=range(18, 41, 3), color='forestgreen', edgecolor='black')
plt.title('Distribution of Goalkeeper Ages')
plt.xticks(range(18, 41))
plt.yticks(range(0, 11, 1))
plt.xlabel('Age (Years)')
plt.ylabel('Frequency of Goalkeepers')
plt.savefig('goalkeeper_analysis/goalkeeper_age_distribution.png')
plt.show()

# Now looking at finding the relationship between the age of the goalkeepers and their minutes played, to see if there is a potential relationship between the two variables
age_minutes_correlation = df['Age_clean'].corr(df['Minutes'])
print(f"The correlation between age and minutes played is: {age_minutes_correlation}")
# We can see although the histogram shows a higher density of older goalkeepers there is in fact practically zero correlation
