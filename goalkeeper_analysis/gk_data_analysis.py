# To complete my small analysis on goalkeepers I will be using SQL and Python 

import pandas as pd 
import sqlite3

# Creating a connection to the SQLite database where the data is stored
conn = sqlite3.connect('sqlite/gk_database.db')

# Reading in the data from the database into pandas dataframes for analysis

df = pd.read_csv('data/clean/gk_combined.csv')
df.to_sql('gk_combinedsql', conn, if_exists='replace', index=False)


# Verifying it has worked 
print(df.head())
print(df.columns)

