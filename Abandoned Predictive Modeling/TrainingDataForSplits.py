#This file contains methods that prepares data from past seasons (excluding 2024) to be split further into testing and training data.



import pandas as pd
from sklearn.model_selection import train_test_split

    # --- CONVERT possessionTime (e.g. "30:45") TO TOTAL SECONDS (e.g. "1845")
def time_to_seconds(time_str):
    try:
        minutes, seconds = map(int, str(time_str).split(':'))
        return minutes * 60 + seconds
    except:
        return None

def features():
    #return ['thirdDownEff','completionAttempts', 'yardsPerPass', 'rushingYards', 'possessionTime']
    return ['thirdDownEff','yardsPerPass', 'rushingAttempts', 'turnovers']

def mergeWinnersLosers(winner_file, loser_file):
    df_winners = pd.read_csv(winner_file)
    df_winners['Result'] = 1

    df_losers = pd.read_csv(loser_file)
    df_losers['Result'] = 0

    df_combined = pd.concat([df_winners, df_losers])

    df_combined['possessionTime'] = df_combined['possessionTime'].apply(time_to_seconds)

    if df_combined['Result'].dtype == object:
        df_combined['Result'] = df_combined['Result'].map({'winner': 1, 'loser': 0})

    #previous cleaning attempts showed that there are no missing values to handle
    feature_col = features()
    for col in feature_col:
        median_train = df_combined[col].median()
        df_combined[col] = df_combined[col].fillna(median_train)

    return df_combined

def GetXy(winner_file, loser_file, feature_cols):
    df_combined = mergeWinnersLosers(winner_file, loser_file)
    x = df_combined[feature_cols]
    y = df_combined['Result']
    
    return (x,y)
