#! /bin/bash

# Removing all rows where position doesnt equal GK 
awk -F',' 'NR==1 || $4 == "GK"' data/raw/pl_dataset_2526_playerwage.csv > data/processed/gk_wages.csv

echo "Cleaning Complete!"
