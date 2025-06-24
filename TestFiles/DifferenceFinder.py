import pandas as pd

n = pd.read_excel("all_games_team_stats_losers_PreviousSeasons.xlsx")
m = pd.read_csv("NewDataFiles/past_seasons_close_games_team_stats_losers.csv")


#feature_cols = ['Game ID']
feature_cols = ['Game ID',                'thirdDownEff',                 'completionAttempts',                 'yardsPerPass',                 'rushingYards']                 #,'possessionTime']
K = n.sort_values(by ='Game ID', ascending = False)
L = m.sort_values(by ='Game ID', ascending = False)

k = K[feature_cols]
l = L[feature_cols]

k.to_csv("TestFiles/sortedxl.csv")
l.to_csv("TestFiles/sortedcs.csv")

xl = pd.read_csv("TestFiles/sortedxl.csv")
cs = pd.read_csv("TestFiles/sortedcs.csv")

D2 = xl-cs
print(D2)
D2.to_csv("TestFiles/Subtracted.csv") #shows that we have the same game IDs but not the same game data