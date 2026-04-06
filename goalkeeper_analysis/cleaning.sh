#!/bin/bash

# Removing Duplicates
awk '!seen[$0]++' data/raw/pl_dataset_2526_gkstats.csv > temp.csv 

# Removing empty rows 
grep -v '^$' temp.csv > data/processed/gkstats_clean.csv 

# Remove temp file 
rm temp.csv 

echo "Cleaning complete!"
