#!/bin/bash

# Removing Duplicates 
sort data/raw/pl_dataset_2526_gkstats.csv | uniq > temp.csv 

# Removing empty rows 
grep -v '^$' temp.csv > data/processed/gkstats_clean.csv 

# Remove temp file 
rm temp.csv 

echo "Cleaning complete!"
