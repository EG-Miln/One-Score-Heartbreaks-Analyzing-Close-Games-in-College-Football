
#Reads in close games then all games files and outputs play-by-plays by the season

import requests
import pandas as pd
import json



for year in [2018, 2019, 2020, 2021, 2022, 2023, 2024]:

    input_file = "NewDataFiles/" + str(year) + "_closeGames.csv"  # File containing game IDs
    base_output_path = "NewDataFiles/"

    # --- LOAD GAME IDS ---
    df = pd.read_csv(input_file)

    # --- INIT STORAGE ---
    all_play_by_plays = []
    all_team_stats = []

    # --- PROCESS EACH GAME ---
    for game_id in df['id']:
        print(f"Processing Game ID: {game_id}")

        with open("NewDataFiles/ESPN/" +str(game_id) + '.json', 'r') as f:
            data = json.load(f)
        

        plays = data.get('drives', {}).get('previous', [])
            
        for drive in plays:
            for play in drive.get('plays', []):
                play_data = {
                    'game_id': game_id,
                    'quarter': play.get('period', {}).get('number'),
                    'clock': play.get('clock', {}).get('displayValue'),
                    'downDistance': play.get('start', {}).get('downDistanceText'),
                    'yardLine': play.get('start', {}).get('yardLineText'),
                    'text': play.get('text'),
                }
                all_play_by_plays.append(play_data)

    df_pbp = pd.DataFrame(all_play_by_plays)
    df_pbp.to_csv(base_output_path + str(year) + '_close_games_Play-by-Plays.csv')

for year in [2018, 2019, 2020, 2021, 2022, 2023, 2024]:

    input_file = "NewDataFiles/" + str(year) + "_games.csv"  # File containing game IDs
    base_output_path = "NewDataFiles/"

    # --- LOAD GAME IDS ---
    df = pd.read_csv(input_file)

    # --- INIT STORAGE ---
    all_play_by_plays = []
    all_team_stats = []

    # --- PROCESS EACH GAME ---
    for game_id in df['id']:
        print(f"Processing Game ID: {game_id}")

        with open("NewDataFiles/ESPN/" +str(game_id) + '.json', 'r') as f:
            data = json.load(f)
        

        plays = data.get('drives', {}).get('previous', [])
            
        for drive in plays:
            for play in drive.get('plays', []):
                play_data = {
                    'game_id': game_id,
                    'quarter': play.get('period', {}).get('number'),
                    'clock': play.get('clock', {}).get('displayValue'),
                    'downDistance': play.get('start', {}).get('downDistanceText'),
                    'yardLine': play.get('start', {}).get('yardLineText'),
                    'text': play.get('text'),
                }
                all_play_by_plays.append(play_data)


    df_pbp = pd.DataFrame(all_play_by_plays)
    df_pbp.to_csv(base_output_path + str(year) + '_all_games_Play-by-Plays.csv')
