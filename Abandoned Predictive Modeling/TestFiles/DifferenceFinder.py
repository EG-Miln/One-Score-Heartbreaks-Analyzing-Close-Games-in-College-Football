# In the process of predictive modeling an error in the excel file was discovered. 
# This script was used to locate the error by comparing the csv and excel files used as training data for our model.

import pandas as pd

path = 'CSV and Excel Files for Python Scripts/'

n = pd.read_excel(path + "all_games_team_stats_losers_PreviousSeasons.xlsx")
m = pd.read_csv(path + "NewDataFiles/past_seasons_close_games_team_stats_losers.csv")


#feature_cols = ['Game ID']
feature_cols = ['Game ID',                'thirdDownEff',                 'completionAttempts',                 'yardsPerPass',                 'rushingYards']                 #,'possessionTime']
K = n.sort_values(by ='Game ID', ascending = False)
L = m.sort_values(by ='Game ID', ascending = False)

k = K[feature_cols]
l = L[feature_cols]

k.to_csv("Abandoned Predictive Modeling/TestFiles/sortedxl.csv")
l.to_csv("Abandoned Predictive Modeling/TestFiles/sortedcs.csv")

xl = pd.read_csv("Abandoned Predictive Modeling/TestFiles/sortedxl.csv")
cs = pd.read_csv("Abandoned Predictive Modeling/TestFiles/sortedcs.csv")

D2 = xl-cs
print(D2)
D2.to_csv("Abandoned Predictive Modeling/TestFiles/Subtracted.csv") #shows that we have the same game IDs but not the same game data