#This file contains methods that prepares data from past seasons (excluding 2024) to be used as training data and data from the 2024 season to be used as testing data for our final model.
#These methods were used in creating our final model without calling this file.

import pandas as pd

    # --- CONVERT possessionTime (e.g. "30:45") TO TOTAL SECONDS (e.g. "1845")
def time_to_seconds(time_str):
    try:
        minutes, seconds = map(int, str(time_str).split(':'))
        return minutes * 60 + seconds
    except:
        return None

def features():
    return ['thirdDownEff', 
                    'completionAttempts', 
                    'yardsPerPass', 
                    'rushingYards', 
                    'possessionTime']

def GetTrainingData(winner_file, loser_file, test_file):

    # --- LOAD TRAINING DATA (FBS SEASONS FROM 2018, 2019, AND 2021-2023)
    df_winners = pd.read_csv(winner_file)
    df_winners['Result'] = 1

    df_losers = pd.read_csv(loser_file)
    df_losers['Result'] = 0

    df_train = pd.concat([df_winners, df_losers])


    # --- LOAD TESTING DATA (2024 FBS SEASON)
    df_test = pd.read_csv(test_file)
    # --- MAP THE TESTING RESULT COLUMN (e.g. Winner -> 1 ; Loser -> 0)
    if df_test['Result'].dtype == object:
        df_test['Result'] = df_test['Result'].map({'winner': 1, 'loser': 0})

    # --- KEY FEATURES 
    feature_cols = features()



    # --- APPLY TIME CONVERSION 
    df_train['possessionTime'] = df_train['possessionTime'].apply(time_to_seconds)
    df_test['possessionTime'] = df_test['possessionTime'].apply(time_to_seconds)


    #previous cleaning attempts showed that there are no missing values to handle
    for col in feature_cols:
        median_train = df_train[col].median()
        median_test = df_test[col].median()
        df_train[col] = df_train[col].fillna(median_train)
        df_test[col] = df_test[col].fillna(median_test)

    # --- SET X AND y 
    X_train = df_train[feature_cols]
    y_train = df_train['Result']

    X_test = df_test[feature_cols]
    y_test = df_test['Result']

    return [X_train, y_train, X_test, y_test]
