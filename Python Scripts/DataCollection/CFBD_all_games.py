#Obtained an overview of each FBS game from the 2018-2024 seasons via https://api.collegefootballdata.com/#/games/GetGames 



import requests
import pandas as pd
from Functions.cfbdkey import * #CFBDKey() returns a string to be filled with a working API key to collegefootballdata.com

path = 'CSV and Excel Files for Python Scripts/NewDataFiles/'

for year in [2018, 2019, 2020, 2021, 2022, 2023, 2024]:
    
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

    gamesDF.to_csv(path + str(year) + '_games.csv')







