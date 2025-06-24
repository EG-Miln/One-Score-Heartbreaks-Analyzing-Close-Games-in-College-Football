#Looks at subsets of key features and maximizes accuracy
#Looks at subsets of key features and maximizes ROC AUC


from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score

from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline

import itertools

from TrainingDataForSplits import *


winner_file = 'NewDataFiles/past_seasons_close_games_team_stats_winners.csv'
loser_file = 'NewDataFiles/past_seasons_close_games_team_stats_losers.csv'

feature_cols = ['firstDowns', 
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


bestAUC = 0
bestAUCSubset = []
bestAcc = 0
bestAccSubset = []

for r in range(1,11):
    print(r)
    for subset in itertools.combinations(feature_cols, r):
        fc = list(subset)
        X,y = GetXy(winner_file, loser_file, fc)

        


        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 243) #, stratify=y) #, random_state=216)



        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        # --- TRAIN LOGISTIC REGRESSION 
        model = LogisticRegression(max_iter=1000, solver='lbfgs')
        model.fit(X_train_scaled, y_train)

        # --- PREDICTION
        y_pred = model.predict(X_test_scaled)
        y_prob = model.predict_proba(X_test_scaled)[:,1]

        # --- EVALUATION
        Acc = accuracy_score(y_test, y_pred)
        AUC = roc_auc_score(y_test, y_prob)

        if(Acc > bestAcc):
            bestAcc = Acc
            bestAccSubset = subset
        if(AUC > bestAUC):
            bestAUC = AUC
            bestAUCSubset = subset
    print("Best AUC " + str(bestAUC))
    print(bestAUCSubset)
    print("Best Accuracy " + str(bestAcc))
    print(bestAccSubset)
        #print("Accuracy:", accuracy_score(y_test, y_pred))
        #print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
        #print("Classification Report:\n", classification_report(y_test, y_pred))
        #print("ROC AUC:", roc_auc_score(y_test, y_prob))

