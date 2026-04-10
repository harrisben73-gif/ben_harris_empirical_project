# Combining stats and wage data for goalkeepers using python, which is more efficient 

import pandas as pd 

wages = pd.read_csv('goalkeeper_analysis/data/processed/gk_wages.csv')
stats = pd.read_csv('goalkeeper_analysis/data/processed/gkstats_clean.csv')

# Merging the two datasets on the 'Player' column to create a combined dataset that includes both stats and wage information for each goalkeeper

combined = pd.merge(stats, wages, on='Player', how='left')
combined.to_csv('goalkeeper_analysis/data/clean/gk_combined.csv', index=False)

# Dropping unwanted columns 
combined = combined.drop(columns=['Rank_y', 'Nation_y', 'Position_y', 'Squad_y', 'Age_y'])

# Modifying the wage columns so that it just shows it in GBP or £
combined['Weekly Wages'] = (combined['Weekly Wages'].astype(str).str.extract(r'£\s*([\d,]+)').iloc[:, 0].str.replace(',', '', regex = False).astype(float))
combined['Annual Wages'] = (combined['Annual Wages'].astype(str).str.extract(r'£\s*([\d,]+)').iloc[:, 0].str.replace(',', '', regex = False).astype(float))


# Cleaning the age column as some are strings at the moment, to just the age in years
combined['Age_clean'] = combined['Age_x'].str.split('-').str[0].astype(int)

# Cleaning the minutes column to just show the number of minutes played as an integer, as some of the values are strings at the moment
combined['Minutes'] = combined['Minutes'].str.replace(',', '').astype(int)

combined.to_csv('goalkeeper_analysis/data/clean/gk_combined.csv', index=False)

# Data is now cleaned and combined, I will be using this dataset for my analysis in the gk_data_analysis.py file