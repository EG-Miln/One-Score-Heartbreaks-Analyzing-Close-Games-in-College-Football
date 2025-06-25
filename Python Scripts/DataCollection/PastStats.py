#Assembles data from individual seasons into past seasons (excluding 2020) for use as training data

import pandas as pd

path = 'CSV and Excel Files for Python Scripts/NewDataFiles/'

for filename in ['_all_games_Play-by-Plays.csv', '_all_games_team_stats_summary.csv', '_all_games_team_stats_winners.csv', '_all_games_team_stats_losers.csv']:
    df = pd.DataFrame()

    for year in [2018, 2019, 2021, 2022, 2023]:

        input_file = path + str(year) + filename
        newDF = pd.read_csv(input_file)

        df = pd.concat([df, newDF])
    print(filename)
    df.to_csv(path + "past_seasons" + filename)


for filename in ['_close_games_Play-by-Plays.csv', '_close_games_team_stats_summary.csv', '_close_games_team_stats_winners.csv', '_close_games_team_stats_losers.csv']:
    df = pd.DataFrame()
    for year in [2018, 2019, 2021, 2022, 2023]:

        input_file = path + str(year) + filename
        newDF = pd.read_csv(input_file)

        df = pd.concat([df, newDF])
    print(filename)
    df.to_csv(path + "past_seasons" + filename)
