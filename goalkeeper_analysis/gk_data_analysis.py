# To complete my small analysis on goalkeepers I will be using SQL and Python 

import pandas as pd 
import sqlite3

# Creating a connection to the SQLite database where the data is stored
conn = sqlite3.connect('sqlite/gk_database.db')

# Reading in the data from the database into pandas dataframes for analysis
df = pd.read_csv('goalkeeper_analysis/data/clean/gk_combined.csv')
df.to_sql('gk_combinedsql', conn, if_exists='replace', index=False)

# Final bit of data cleaning before analysis, converting the "Weekly Wages" column to numeric values for easier calculations
df['weekly_wages_clean'] = (df['Weekly Wages'].str.replace(r"[£,]", "", regex=True).str.extract(r"(\d+)").astype(float))
df.to_sql('gk_combinedsql', conn, if_exists='replace', index=False)

# Printing the first 5 rows of the SQL table to verify it has been created correctly
# print(pd.read_sql_query("SELECT * FROM gk_combinedsql LIMIT 5", conn))

# Finding the average wage of all the goalkeepers in the dataset
avg_wage = pd.read_sql_query("""SELECT AVG(weekly_wages_clean) AS avg_wage FROM gk_combinedsql""", conn)
print(f"The average weekly wage of the goalkeepers in the dataset is: £{round(avg_wage['avg_wage'].iloc[0])}")

# Finding the top 10 highest paid goalkeepers in the dataset
top_paid_gks = pd.read_sql_query("""SELECT Player, Squad_x, weekly_wages_clean FROM gk_combinedsql ORDER BY weekly_wages_clean DESC LIMIT 10""", conn)
print("The top 10 highest paid goalkeepers in the dataset are:", top_paid_gks.values.tolist())

# Finding the top 10 goalkeepers by save percentage in the dataset
top_save_percentage_gks = pd.read_sql_query("""SELECT Player, Squad_x, 'Save Percentage' FROM gk_combinedsql ORDER BY 'Save Percentage' DESC LIMIT 10""", conn)
print("The top 10 goalkeepers by save percentage in the dataset are:", top_save_percentage_gks.values.tolist())

# Finding the correlation between them both 
correlation = pd.read_sql_query("""
SELECT 
    (
        COUNT(*) * SUM(weekly_wages_clean * "Save Percentage")
        - SUM(weekly_wages_clean) * SUM("Save Percentage")
    ) 
    /
    (
        SQRT(
            (COUNT(*) * SUM(weekly_wages_clean * weekly_wages_clean)
            - POWER(SUM(weekly_wages_clean), 2))
            *
            (COUNT(*) * SUM("Save Percentage" * "Save Percentage")
            - POWER(SUM("Save Percentage"), 2))
        )
    )
    AS correlation
FROM gk_combinedsql
WHERE weekly_wages_clean IS NOT NULL
AND "Save Percentage" IS NOT NULL;
""", conn)

print(f"The correlation is: {round(correlation['correlation'].iloc[0], 3)}")

