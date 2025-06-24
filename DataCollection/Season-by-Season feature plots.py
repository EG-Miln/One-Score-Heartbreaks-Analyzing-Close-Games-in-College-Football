#Season-by-Season analysis

#Shows our chosen factors year-by-year

import pandas as pd
import matplotlib.pyplot as plt
from Functions.TimeConverter import *


feature_cols = [ 
    'Final Score', 
    'firstDowns', 
    'thirdDownEff', 
    'totalYards',  
    'completionAttempts', 
    'yardsPerPass',  
    'rushingYards', 
    'rushingAttempts', 
    'yardsPerRushAttempt', 
    'possessionTime',
    'turnovers'
]

seasonsList = [2018, 2019, 2020, 2021, 2022, 2023, "past_seasons"]

for f in ['_close_games_team_stats_summary']:#['_close_games_team_stats_summary', '_close_games_team_stats_winners', '_close_games_team_stats_losers']: #

    dfMeans = list()


    for season in seasonsList:
        filename = "NewDataFiles/" + str(season) + f + ".csv"

        df = pd.read_csv(filename)

        df['possessionTime'] = df.apply(lambda row: time_to_seconds(row.possessionTime), axis = 1)   #convert possession time to seconds to find mean

        seasonMeans = df[feature_cols].mean(axis=0)

        dfMeans.append(seasonMeans)
        

    df = pd.DataFrame(dfMeans, index= seasonsList)
    pastSeasons = df.iloc[len(seasonsList)-1]

    centered_df = (df - pastSeasons).drop(["past_seasons"])


    for feature in df.columns:

        chart_centered = centered_df[feature].plot(kind = 'bar', title = feature + " centered", rot = 45, )
        plt.show()
        plt.savefig("Plots/" + feature + " centered.png")

        chart = df[feature].plot(kind = 'bar', title = feature, rot = 45)
        plt.savefig("Plots/" + feature + ".png")
        plt.show()

        

    

    
