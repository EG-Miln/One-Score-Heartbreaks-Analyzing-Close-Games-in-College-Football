## 2024 FBS Team Stats

import requests
import pandas as pd

# --- CONFIGURATION (YOU MAY NEED TO UPDATE ON YOUR COMPUTER) ---
input_file = "C:/Users/lseminario/Downloads/all_close_game_ids.csv"  # File containing game IDs
base_output_path = "C:/Users/lseminario/Downloads/"

summary_output = base_output_path + "all_games_team_stats_summary.xlsx"
winners_output = base_output_path + "all_games_team_stats_winners.xlsx"
losers_output = base_output_path + "all_games_team_stats_losers.xlsx"

# --- LOAD GAME IDS ---
df_ids = pd.read_csv(input_file, encoding='latin1')
game_ids = df_ids['Id'].astype(str).tolist()

# --- INIT STORAGE ---
all_team_stats = []

# --- PROCESS EACH GAME ---
for game_id in game_ids:
    print(f"Processing Game ID: {game_id}")
    try:
        url = f'https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event={game_id}'
        response = requests.get(url)
        data = response.json()

        # Build team lookup from "competitors"
        competitors = data.get("header", {}).get("competitions", [{}])[0].get("competitors", [])
        team_lookup = {
            int(team['id']): {
                'Final Score': int(team.get('score', 0)),
                'Result': 'winner' if team.get('winner', False) else 'loser'
            }
            for team in competitors
        }

        # Extract team stats
        teams = data.get('boxscore', {}).get('teams', [])
        for team_data in teams:
            team_info = team_data.get('team', {})
            stats = team_data.get('statistics', [])
            team_id = int(team_info.get('id', -1))

            team_dict = {
                'Game ID': game_id,
                'Team': team_info.get('shortDisplayName', 'Unknown Team'),
                'Team ID': team_id,
                'Result': team_lookup.get(team_id, {}).get('Result'),
                'Final Score': team_lookup.get(team_id, {}).get('Final Score')
            }

            for stat in stats:
                name = stat.get('name')
                value = stat.get('displayValue')

                if name in ['thirdDownEff', 'fourthDownEff']:
                    try:
                        made, attempts = value.split('-')
                        made = int(made)
                        attempts = int(attempts)
                        team_dict[name] = made / attempts if attempts != 0 else 0
                    except Exception:
                        team_dict[name] = None

                elif name == 'completionAttempts':
                    try:
                        completed, attempted = value.split('/')
                        completed = int(completed)
                        attempted = int(attempted)
                        team_dict[name] = completed / attempted if attempted != 0 else 0
                    except Exception:
                        team_dict[name] = None

                elif name == 'totalPenaltiesYards':
                    try:
                        penalties, yards = value.split('-')
                        team_dict['Penalties'] = int(penalties)
                        team_dict['Penalty Yards'] = int(yards)
                    except Exception:
                        team_dict['Penalties'] = None
                        team_dict['Penalty Yards'] = None

                else:
                    team_dict[name] = value

            # Convert numeric-looking fields (except possession time)
            for key, value in team_dict.items():
                if isinstance(value, str) and key.lower() not in ['possession', 'possessiontime']:
                    try:
                        team_dict[key] = float(value.replace(',', ''))
                    except:
                        pass

            all_team_stats.append(team_dict)

    except Exception as e:
        print(f"❌ Error processing Game ID {game_id}: {e}")
        continue

# --- BUILD DATAFRAME ---
df_all = pd.DataFrame(all_team_stats)
df_winners = df_all[df_all['Result'] == 'winner']
df_losers = df_all[df_all['Result'] == 'loser']

# --- EXPORT TO EXCEL ---
with pd.ExcelWriter(summary_output) as writer:
    df_all.to_excel(writer, index=False, sheet_name='Summary')

with pd.ExcelWriter(winners_output) as writer:
    df_winners.to_excel(writer, index=False, sheet_name='Winners')

with pd.ExcelWriter(losers_output) as writer:
    df_losers.to_excel(writer, index=False, sheet_name='Losers')

print(f"\n✅ Finished processing {len(game_ids)} games.")
print(f"📊 Summary: {summary_output}")
print(f"🏆 Winners: {winners_output}")
print(f"💔 Losers: {losers_output}")


########################################################################################

## IGNORE (THIS ONLY DOES ONE GAME, BUT IT WAS USED TO DESIGN THE GENERAL CODE)

# import requests
# import pandas as pd

# # --- CONFIGURATION ---
# game_id = '401628530'  # Single game
# base_output_path = "C:/Users/lseminario/Downloads/"

# summary_output = base_output_path + "single_game_team_stats_summary.xlsx"
# winners_output = base_output_path + "single_game_team_stats_winner.xlsx"
# losers_output = base_output_path + "single_game_team_stats_loser.xlsx"

# # --- FETCH GAME DATA ---
# url = f'https://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event={game_id}'
# response = requests.get(url)
# data = response.json()

# # --- BUILD TEAM SCORE/RESULT LOOKUP FROM COMPETITORS ---
# competitors = data.get("header", {}).get("competitions", [{}])[0].get("competitors", [])
# team_lookup = {
#     int(team['id']): {
#         'Final Score': int(team.get('score', 0)),
#         'Result': 'winner' if team.get('winner', False) else 'loser'
#     }
#     for team in competitors
# }

# # --- EXTRACT TEAM STATS ---
# teams = data.get('boxscore', {}).get('teams', [])
# summary_data = []

# for team_data in teams:
#     team_info = team_data.get('team', {})
#     stats = team_data.get('statistics', [])
#     team_id = int(team_info.get('id', -1))

#     team_dict = {
#         'Game ID': game_id,
#         'Team': team_info.get('shortDisplayName', 'Unknown Team'),
#         'Team ID': team_id,
#         'Result': team_lookup.get(team_id, {}).get('Result'),
#         'Final Score': team_lookup.get(team_id, {}).get('Final Score')
#     }

#     for stat in stats:
#         name = stat.get('name')
#         value = stat.get('displayValue')

#         if name in ['thirdDownEff', 'fourthDownEff']:
#             try:
#                 made, attempts = value.split('-')
#                 made = int(made)
#                 attempts = int(attempts)
#                 team_dict[name] = made / attempts if attempts != 0 else 0
#             except Exception:
#                 team_dict[name] = None

#         elif name == 'completionAttempts':
#             try:
#                 completed, attempted = value.split('/')
#                 completed = int(completed)
#                 attempted = int(attempted)
#                 team_dict[name] = completed / attempted if attempted != 0 else 0
#             except Exception:
#                 team_dict[name] = None

#         elif name == 'totalPenaltiesYards':
#             try:
#                 penalties, yards = value.split('-')
#                 team_dict['Penalties'] = int(penalties)
#                 team_dict['Penalty Yards'] = int(yards)
#             except Exception:
#                 team_dict['Penalties'] = None
#                 team_dict['Penalty Yards'] = None

#         else:
#             team_dict[name] = value

#     # --- Convert values to numbers where applicable (except possession time) ---
#     for key, value in team_dict.items():
#         if isinstance(value, str) and key.lower() not in ['possession', 'possessiontime']:
#             try:
#                 team_dict[key] = float(value.replace(',', ''))
#             except:
#                 pass  # Leave as is if it can't be converted

#     summary_data.append(team_dict)

# # --- CONVERT TO DATAFRAME ---
# df_summary = pd.DataFrame(summary_data)

# # --- SPLIT WINNERS AND LOSERS ---
# df_winners = df_summary[df_summary['Result'] == 'winner']
# df_losers = df_summary[df_summary['Result'] == 'loser']

# # --- EXPORT TO EXCEL ---
# with pd.ExcelWriter(summary_output) as writer:
#     df_summary.to_excel(writer, index=False, sheet_name='Summary')

# with pd.ExcelWriter(winners_output) as writer:
#     df_winners.to_excel(writer, index=False, sheet_name='Winners')

# with pd.ExcelWriter(losers_output) as writer:
#     df_losers.to_excel(writer, index=False, sheet_name='Losers')

# print(f"✅ Files saved:\n- {summary_output}\n- {winners_output}\n- {losers_output}")
