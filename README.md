# Ben Harris Empirical Project

Welcome, this is the repository I will be using to track work for my Data Science for Economics (BEE2041) Empirical Project. 

## Description 

![PL Image](https://e0.365dm.com/25/06/1600x900/skysports-graphic-badge-premier-league_6939799.jpg?20250612080512)

During this project I will be looking at analysing a dataset about Premier League footballers wages and statistics so far during the 2025/26 season, where most teams have played 31 out of 38 games, apart from Manchester City and Crystal Palace who have played 30 games each. 


## Installation 

git clone https://github.com/harrisben73-gif/ben_harris_empirical_project.git

For this project I will be using multiple different software systems, listed as follows on a Windows 10 operating system:  

|Software   | Versions       |
|-----------|----------------|
|Python     |3.13            |
|Pandas     |3.0.0           |
|Numpy      |2.4.2           |
|Openpyxl   |3.1.5           |
|SQLite3    |3.50.4          | 
|Linux/WSL  |Ubuntu 24.04.3  |
|Seaborn    |0.13.2          |
|Matplotlib |3.10.8          |
|EconML     |0.16.0          |
|Statsmodel |0.14.6          |

## My Data 

For this project I had to harvest data from multiple sources and combine them into one Excel spreadsheet for easier analysis. 

💷 For salary data I used the well known site Capology, which is considered a reliable source for football salary data

[View the salary data](https://www.capology.com/uk/premier-league/salaries/)

⚽️ For player statistics I used FBREF as it had the most accurate and up to date data for the 2025/26 Premier League season

[View the player statistics data](https://fbref.com/en/comps/9/stats/Premier-League-Stats)

This data was acquired on 25/03/2026, apart from the Goalkeeper Statistics, which was acquired on 05/04/2026.

# Project Structure 

ben_harris_empirical_project/ 
- data/
    - raw/
        - pl_dataset_2526_clubstats.csv/
        - pl_dataset_2526_clubwage.csv/
        - pl_dataset_2526_playerstats.csv/
        - pl_dataset_2526_playerwage.csv/
    - cleaned/ 
        - merged_club_data/ 
        - merged_player_data/
- scripts/ 
    - data_cleaning.py/ 
- README.md/ 

# Usage

