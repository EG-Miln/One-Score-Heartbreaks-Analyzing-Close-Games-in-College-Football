import pandas as pd

#Save 2024 close games to 2024_close_game_ids.csv

for year in [2018, 2019, 2021, 2023, 2024]:

    input_file = "NewDataFiles/" + str(year) + "_games.csv"  # File containing game IDs
    base_output_path = "NewDataFiles/"



    gamesDF = pd.read_csv(input_file)

    #print(gamesDF.columns)
    gamesDF['pointsDifference'] = gamesDF.apply(lambda row: row.homePoints - row.awayPoints, axis = 1)

    gamesDF['closeGame'] = gamesDF.apply(lambda row: (abs(row.pointsDifference) <9), axis = 1) #a game is close if the two teams scored within 8 points of each other



    closeDF = gamesDF[gamesDF['closeGame']] #takes rows(games) for which closeGame is true



    closeDF.to_csv(base_output_path + str(year) + '_closeGames.csv')


