#abandoned logistic regression model with 0.6666 accuracy and 0.7129 ROC AUC

from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score

from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline


from TrainingDataForSplits import *




path = 'CSV and Excel Files for Python Scripts/NewDataFiles/'

winner_file = path + 'past_seasons_close_games_team_stats_winners.csv'
loser_file = path + 'past_seasons_close_games_team_stats_losers.csv'

feature_cols = ['thirdDownEff','yardsPerPass', 'rushingAttempts', 'turnovers']
X,y = GetXy(winner_file, loser_file, feature_cols)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=216)



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
#print("Accuracy:", accuracy_score(y_test, y_pred))
#print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
#print("Classification Report:\n", classification_report(y_test, y_pred))
#print("ROC AUC:", roc_auc_score(y_test, y_prob))

# --- FEATURE IMPORTANCE 
#importances = pd.Series(model.coef_[0], index=feature_cols)
#print("\n Logistic Regression Coefficients:")
#print(importances.sort_values(ascending=False))

print("outputting final test results")

df_test = pd.read_csv(path + '2024_close_games_team_stats_summary.csv')
if df_test['Result'].dtype == object:
    df_test['Result'] = df_test['Result'].map({'winner': 1, 'loser': 0})

X_test = df_test[feature_cols]
y_test = df_test['Result']
X_test_scaled = scaler.transform(X_test)

#training data and model are already created above

y_pred = model.predict(X_test_scaled)
y_prob = model.predict_proba(X_test_scaled)[:,1]

# --- EVALUATION
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
print("ROC AUC:", roc_auc_score(y_test, y_prob))


importances = pd.Series(model.coef_[0], index=feature_cols)
print("\n Logistic Regression Coefficients:")
print(importances.sort_values(ascending=False))
