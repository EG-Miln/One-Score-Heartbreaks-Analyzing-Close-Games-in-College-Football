#Saves the list of close games each season to a separate csv from the list of all games.


import pandas as pd

path = 'CSV and Excel Files for Python Scripts/NewDataFiles/'

for year in [2018, 2019, 2020, 2021, 2022, 2023, 2024]:

    input_file = path + str(year) + "_games.csv"  # File containing game IDs
    base_output_path = path



    gamesDF = pd.read_csv(input_file)

    #print(gamesDF.columns)
    gamesDF['pointsDifference'] = gamesDF.apply(lambda row: row.homePoints - row.awayPoints, axis = 1)

    gamesDF['closeGame'] = gamesDF.apply(lambda row: (abs(row.pointsDifference) <9), axis = 1) #a game is close if the two teams scored within 8 points of each other



    closeDF = gamesDF[gamesDF['closeGame']] #takes rows(games) for which closeGame is true



    closeDF.to_csv(base_output_path + str(year) + '_closeGames.csv')


