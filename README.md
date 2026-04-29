# Ben Harris Empirical Project

Welcome, this is the repository I will be using to track work for my Data Science for Economics (BEE2041) Empirical Project. 

You can find my project output using the link below 
https://harrisben73-gif.github.io/ben_harris_empirical_project

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
|HTML       |HTML5           |

## My Data 

For this project I had to harvest data from multiple sources and combine them into one Excel spreadsheet for easier analysis. 

💷 For salary data I used the well known site Capology, which is considered a reliable source for football salary data

[View the salary data](https://www.capology.com/uk/premier-league/salaries/)

⚽️ For player statistics I used FBREF as it had the most accurate and up to date data for the 2025/26 Premier League season

[View the player statistics data](https://fbref.com/en/comps/9/stats/Premier-League-Stats)

This data was acquired on 25/03/2026, apart from the Goalkeeper Statistics, which was acquired on 05/04/2026.

## Project Structure 

ben_harris_empirical_project/ 
- data/
    - raw/
        - pl_dataset_2526_clubstats.csv
        - pl_dataset_2526_clubwage.csv
        - pl_dataset_2526_gkstats.csv
        - pl_dataset_2526_playerstats.csv
        - pl_dataset_2526_playerwage.csv
    - cleaned/ 
        - merged_club_data/ 
        - merged_player_data/
- scripts/ 
    - data_cleaning.py
- goalkeeper_analysis/
    - data/
        - clean/
        - processed/
        - raw/
    - cleaningstats.sh
    - cleaningwage.sh
    - combiningstatswage.py
    - gk_data_cleaning.py
    - gk_data_analysis.py
    - gk_wages.csv 
    - pl_dataset2526_playerwage.csv 
- data_analysis/
    - clubwages_stats_analysis.py 
    - wages_position_analysis.py 
    - playerwage_randomforest_testing.py
    - merged_club_data.csv
    - merged_player_data.csv 
- README.md/ 

## Usage

1. Setup 

I have listed the software platforms/python packages and versions of these in [Installation](#installation), which would have to be downloaded to fully clean and analyse the data I have used. 

2. How to Clean the Data 

By using mainly pandas and numpy to clean my data in the 'data_cleaning.py' I was firstly able to find out the main problems with my data. This included: wage data being in multiple currencies and having symbols like $£,() included in the data, some clubs having hidden spaces in their names, the nationality column showing en ENG instead of just ENG, the minutes column being a string, and the position column showing multiple positions. Luckily, I did not find many missing values, apart from in the Nationality column, which was not essential for my analysis. 

- To fix the first issue I created a python function called extract_pounds(value), which starts out by checking for missing values then converts the data into a string and after this uses a regular expression to extract the number after the £ sign and finally removes the commas and converts this number into an integer

- To fix the fact that club names where slightly different in pl_dataset_2526_clubstats.csv and pl_dataset_2526_clubwage.csv, I had to firstly check the differences and then I could use the str.replace function to substitute the part of string I did not want with something else that matches the other dataset, therefore allowing us the merge both datasets by club name

- To fix the nationality column, we used a similar command called str.split, which allowed us to only keep the last word in each string, therefore allowing us to have a cleaner nationalities column if we needed to use it

- Turning the minutes column into a numeric value was a simple fix as we just used pandas to transform the strong into numeric, which was no problem as the values in the column where all integers already

- The position column was another simple fix by using the pandas function .replace again, where I knew the first position listed was the players primary position, so for example if there positions was listed as FW, MF the new column would show solely FW

- Then finally as I merged our datasets so I had statistics and wages all in two datasets merged_player_data.csv and merged_club_data.csv, I had to drop some columns that had duplicated or were irrelevant to my analysis. 

- In the end we can see that the only columns with missing data is minutes, but I did not want to remove players who did not have minute statistics as this would leave me with a significantly lower sample size


I also had a small sub-project where I would be analysing the goalkeepers in the league and aim to use more Linux and SQLite code. To start with the data cleaning I used two bash scripts cleaningstats.sh and cleaningwage.sh, and the terminal after going into wsl. 

- The cleaningstats.sh file checks over the datset pl_dataset_2526_gkstats.csv from the data/raw folder and checks for duplicates and empty rows and then temporarily stores them in a file and then transfers them back to a new file called gkstats_clean.csv, which is stored in the data/processed folder. 

- The cleaningwage.sh file simply uses the pl_dataset_2526_playerwage.csv file in the data/raw folder and uses the awk command to filter players whose position is a goalkeeper and creates a new file called gk_wages.csv, storing it in data/processed 

- Then to combine both these datasets I chose to use python as this was most effecient and more likely to be accurate. In the file combiningstatswage.py I firstly saved both the clean datasets and them merged them based on player name and created the new final file called gk_combined.csv ini the folder data/clean. Then I had to perform similar things as some of the data had the same issues for example the wages, minutes and age column where I just wanted age in years not years and days. 

3. How to Run the Analysis 

After cleaning all the data I had two main datasets, which I used for the analysis called merged_player_data.csv and merged_club_data.csv, which had come from merging the cleaned versions of pl_dataset_2526_playerstats.csv with pl_dataset_2526_playerwage.csv and pl_dataset_2526_clubstats.csv with pl_dataset_2526_clubwage.csv using python.

For my analysis I wanted to come up with some visual as well as some statistical insights, which meant importing specific python functions like matplotlib, seaborn, sklearn and statsmodels as this would help us get a better understanding of the data and make it easier to spot trends.

I will now go over the files I have used to analyse my data 

- Firstly, I created wages_position_analysis.py, which main aim was to analyse how playing a certain position can effect the amount PL footballers get paid. By using mainly matplotlib I was able to create a boxplot, which showed that as players do get further up the pitch they often do see higher wages. To further back this point up I created a table, which showed that on average goalkeepers and defenders had similar average weekly wages, but midfielders had on average £8,000, and forwards had on average £16,000 more. 

- Secondly, I created the file clubwages_stats_analysis.py, where my main aim was to rank clubs by certain statistics and then create a graph comparing their average rank to the total weekly wages of that club. Using the python function .rank I found the ranks from 10 statsitics and then found the mean of this and saved it as a new variable. Finally, I used matplotlib to plot this against the total weekly wage of all the players in the club. 

- Lastly, I created the file playerwage_randomforest_testing.py, where I was interested in computing a regression analysis using a random forest regressor and average treatment effects (ATE). Using the random forest regressor by setting Y to weekly wages and X to 13 statistics I was able to find the mean squared error and R^2 statistic. However, I also wanted to find the average treatment effects of individual statistics, which meant first having to split the population in 2 groups, above average and below average. After this I used statsmodels to provide my regression coefficients and p-values of the regression.

I also had to complete data analysis for my goalkeeper sub-project, where I mainly used SQLite3 and python, specifically pandas and matplotlibs.

- By using SQLite3 I was able to put my data into an SQL table and then find some simple summary statistics. I then moved onto a more detailed analysis, which involved grouping data to spot differences between certain groups when it comes to wages and statistics. Furthermore, to back up my SQL analysis I used matplotlib to show the data visually on a graphand then the .corr function in python for further analysis. 