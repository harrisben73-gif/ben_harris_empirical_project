#!/bin/bash

sed -i 's/\r$//' cleaningstats.sh

# Set working directory 
cd /mnt/c/Users/linds/OneDrive/Documents/GitHub/ben_harris_empirical_project/goalkeeper_analysis

# Removing Duplicates
awk '!seen[$0]++' data/raw/pl_dataset_2526_gkstats.csv > temp.csv 

# Removing empty rows 
grep -v '^$' temp.csv > data/processed/gkstats_clean.csv 

# Remove temp file 
rm temp.csv

echo "Cleaning complete!"

