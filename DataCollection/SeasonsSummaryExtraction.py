#Obtained game summaries from 2019, 2021, 2023, 2024 seasons via https://api.collegefootballdata.com/#/games/GetGames 





import requests
import pandas as pd
from cfbdkey import * #CFBDKey() returns a string to be filled with a working API key to collegefootballdata.com


for year in [2018, 2019, 2021, 2023, 2024]:

    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer ' + CFBDKey(),
    }

    params = {
        'year': str(year),
        'classification': 'fbs',
    }

    response = requests.get('https://api.collegefootballdata.com/games', params=params, headers=headers)

    gamesJSON = response.json()

    gamesDF = pd.DataFrame(gamesJSON)

    gamesDF.to_csv('NewDataFiles/' + str(year) + '_games.csv')







