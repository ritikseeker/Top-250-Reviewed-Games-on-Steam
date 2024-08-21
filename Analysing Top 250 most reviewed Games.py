import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

'''The games are assigned rank based on No. of Reviews (NOT based on Rating), WHY ? well in datasource they mentioned : 
In this ranking games are sorted by number of reviews only, with complete disregard for rating. Total reviews usually have a strong correlation with total sales, so this provides a relative insight into best sellers of the year. 
'''
gameRankings = pd.read_excel("C:/Users/ritik/Documents/Projects/Web scraping project/Top-250-Reviewed-Games-on-Steam/Top 250 Most Reviewed Games on Steam.xlsx")
# print(gameRankings.head())
# print(gameRankings.tail())
# print(gameRankings.columns)

# Renaming columns
gameRankings.rename(columns = {'Reviews on Steam':'Reviews','Rating on Steam':'Rating(out of 100)','Game Rank':'Rank','Game Name':'Title'}, inplace = True)

# Top 5 Games by Rank(no. of Reviews)
print(gameRankings.head())

# Statistical Summary on dataset
print(gameRankings.describe())

# Info on dataset
print(gameRankings.info())

# Games within Ranking 5-10
# print(gameRankings.loc[4:9])

# Game with > 1,000,000 Reviews
# print(gameRankings[gameRankings["Reviews"]> 1000000])

# Game with > 1,000,000 Reviews and > 0.9 Ratings
# print(gameRankings.loc[(gameRankings['Reviews']>1000000)&(gameRankings['Rating(out of 100)']>0.9)])

# Top rated game released in yr 2023
# print(gameRankings.loc[gameRankings['Release Year'] == 2023].iloc[0])

# Least rated game released in yr 2024
# print(gameRankings.loc[gameRankings['Release Year'] == 2024].iloc[-1])

# grouping by year 
# avgGameRatingByYear = gameRankings.groupby(["Release Year"],as_index=False).agg({'Reviews':['mean'],'Rating(out of 100)':['mean'],'Title':['count']})
# avgGameRatingByYear.rename(columns={"Reviews": "Avg Reviews","Rating(out of 100)":"Avg Rating(out of 100)","Title":"Total Games Released","mean":"","count":""},inplace = True)

# Avg Review, Avg Rating, Total Games Released by Year Dataframe
# print(avgGameRatingByYear)
'''
# Initialise the subplot function using number of rows and columns 
figure, axis = plt.subplots(1, 3) 
  
X = np.array(avgGameRatingByYear["Release Year"])
Y1 = np.array(avgGameRatingByYear["Avg Reviews"])
Y2 = np.array(avgGameRatingByYear["Avg Rating(out of 100)"])
Y3 = np.array(avgGameRatingByYear["Total Games Released"])

axis[0].bar(X, Y1) 
axis[0].set_title("Avg Reviews yearwise")  

axis[1].bar(X, Y2) 
axis[1].set_title("Avg Rating yearwise")


axis[2].bar(X, Y3) 
axis[2].set_title("Total Games Released yearwise")  

# Combine all operations & display 
plt.show()
'''