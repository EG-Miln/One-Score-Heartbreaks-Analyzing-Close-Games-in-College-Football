## 2024 FBS Team Stats plots

import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel files (You may need to update on your computer)
df1 = pd.read_excel('C:/Users/lseminario/Downloads/all_games_team_stats_winners.xlsx')
df2 = pd.read_excel('C:/Users/lseminario/Downloads/all_games_team_stats_losers.xlsx')

# --- Box Plot 1: Final Scores ---
winner_scores = df1['Final Score'].dropna()
loser_scores = df2['Final Score'].dropna()

plt.figure(figsize=(8, 6))
box1 = plt.boxplot([winner_scores, loser_scores], labels=['Winners', 'Losers'], patch_artist=True)

colors = ['red', 'blue']
for patch, color in zip(box1['boxes'], colors):
    patch.set_facecolor(color)

for median in box1['medians']:
    median.set_color('black')

plt.title('Final Scores: Winners vs. Losers')
plt.ylabel('Final Score')
plt.grid(True)

# --- Box Plot 2: First Downs ---
winner_1stDown = df1['firstDowns'].dropna()
loser_1stDown = df2['firstDowns'].dropna()

plt.figure(figsize=(8, 6))
box2 = plt.boxplot([winner_1stDown, loser_1stDown], labels=['Winners', 'Losers'], patch_artist=True)

for patch, color in zip(box2['boxes'], colors):
    patch.set_facecolor(color)

for median in box2['medians']:
    median.set_color('black')

plt.title('First Downs: Winners vs. Losers')
plt.ylabel('First Downs')
plt.grid(True)

# --- Box Plot 3: Third Down Efficiency ---
winner_3rdDownEff = df1['thirdDownEff'].dropna()
loser_3rdDownEff = df2['thirdDownEff'].dropna()

plt.figure(figsize=(8, 6))
box3 = plt.boxplot([winner_3rdDownEff, loser_3rdDownEff], labels=['Winners', 'Losers'], patch_artist=True)

for patch, color in zip(box3['boxes'], colors):
    patch.set_facecolor(color)

for median in box3['medians']:
    median.set_color('black')

plt.title('Third Down Efficiency: Winners vs. Losers')
plt.ylabel('Third Down Efficiency')
plt.grid(True)

# --- Box Plot 4: Fourth Down Efficiency ---
winner_4thDownEff = df1['fourthDownEff'].dropna()
loser_4thDownEff = df2['fourthDownEff'].dropna()

plt.figure(figsize=(8, 6))
box4 = plt.boxplot([winner_4thDownEff, loser_4thDownEff], labels=['Winners', 'Losers'], patch_artist=True)

for patch, color in zip(box4['boxes'], colors):
    patch.set_facecolor(color)

for median in box4['medians']:
    median.set_color('black')

plt.title('Fourth Down Efficiency: Winners vs. Losers')
plt.ylabel('Fourth Down Efficiency')
plt.grid(True)

# --- Box Plot 5: Completion Attempts ---
winner_Completion = df1['completionAttempts'].dropna()
loser_Completion = df2['completionAttempts'].dropna()

plt.figure(figsize=(8, 6))
box5 = plt.boxplot([winner_Completion, loser_Completion], labels=['Winners', 'Losers'], patch_artist=True)

for patch, color in zip(box5['boxes'], colors):
    patch.set_facecolor(color)

for median in box5['medians']:
    median.set_color('black')

plt.title('Completion Attempts: Winners vs. Losers')
plt.ylabel('Completion Attempts')
plt.grid(True)

# --- Box Plot 6: Turnovers ---
winner_turnovers = df1['turnovers'].dropna()
loser_turnovers = df2['turnovers'].dropna()

plt.figure(figsize=(8, 6))
box6 = plt.boxplot([winner_turnovers, loser_turnovers], labels=['Winners', 'Losers'], patch_artist=True)

for patch, color in zip(box6['boxes'], colors):
    patch.set_facecolor(color)

for median in box6['medians']:
    median.set_color('black')

plt.title('Turnovers: Winners vs. Losers')
plt.ylabel('Turnovers')
plt.grid(True)

# Show all plots
plt.show()

