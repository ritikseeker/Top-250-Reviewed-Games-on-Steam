# Top-250-Reviewed-Games-on-Steam

## Python Libraries used:
1. bs4
2. requests
3. openpyxl
4. pandas
5. numpy
6. matplotlib

###STEPS :
1. Run "webscrapping.py" file. It will scrape the data from Steam site and store in "Top 250 Most Reviewed Games on Steam.xlsx" Excel file.
2. "Analysing Top 250 Most Reviewed Games on Steam.xlsx" excel file contains the same data with some formatting done and pivot tables of Average Rating wrt Release Year and Release Month, Average number of Reviews wrt Release Year and Release Month in respective sheets.
3. Run "Analysing Top 250 most reviewed Games.py" python file to :-
   A. Create pandas dataframe from "Top 250 Most Reviewed Games on Steam.xlsx" Excel file, Renaming Columns of dataframe
   B. Show Top 5 Games by Rank
   C. Statistical Summary of each column, Info on dataset
   D. Games within Ranking 5-10
   E. Games with > 1,000,000 Reviews
   F. Game with > 1,000,000 Reviews and > 0.9 Ratings
   G. Top rated game released in yr 2023
   H. Least rated game released in yr 2024
   I. Grouping by Release year with avg Reviews, avg Rating, total games released
   J. Plotting the same using Matplotlib Library
