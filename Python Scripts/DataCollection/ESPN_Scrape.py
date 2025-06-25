#Obtains details of each game from ESPN and saves it for further use

import requests
import pandas as pd
import json

path = 'CSV and Excel Files for Python Scripts/NewDataFiles/'
for year in [2018, 2019, 2020, 2021, 2022, 2023, 2024]:
    input_file = path + str(year) + "_games.csv"  # File containing game IDs


    # --- LOAD GAME IDS ---
    df = pd.read_csv(input_file)


    for game_id in df['id']:
        print(f"Processing Game ID: {game_id}")
        try:
            url = f'https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event={game_id}'
            response = requests.get(url)
            data = response.json()

            with open(path + "ESPN/" + str(game_id) + ".json", 'w') as json_file:
                json.dump(data, json_file)
            
            


        except Exception as e:
            print(f"Error processing Game ID {game_id}: {e}")

