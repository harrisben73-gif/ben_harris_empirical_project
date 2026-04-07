# Combining stats and wage data for goalkeepers using python, which is more efficient 

import pandas as pd 

wages = pd.read_csv('data/processed/gk_wages.csv')
stats = pd.read_csv('data/processed/gkstats_clean.csv')

# Merging the two datasets on the 'Player' column to create a combined dataset that includes both stats and wage information for each goalkeeper

combined = pd.merge(stats, wages, on='Player', how='inner')
combined.to_csv('data/clean/gk_combined.csv', index=False)

