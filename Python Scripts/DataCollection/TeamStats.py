
#Parses ESPN game data and saves the stats we are interested in for further testing for significance

import requests
import pandas as pd
import json

path = 'CSV and Excel Files for Python Scripts/NewDataFiles/'

for year in [2018, 2019, 2020, 2021, 2022, 2023, 2024]:
    print(year)
    input_file = path + str(year) + "_closeGames.csv"  # File containing game IDs
    base_output_path = path

    # --- LOAD GAME IDS ---
    df = pd.read_csv(input_file)

    # --- INIT STORAGE ---
    all_play_by_plays = []
    all_team_stats = []

    # --- PROCESS EACH GAME ---
    for game_id in df['id']:
    #    print(f"Processing Game ID: {game_id}")

        with open(path + "ESPN/" +str(game_id) + '.json', 'r') as f:
            data = json.load(f)
        
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

    df_all = pd.DataFrame(all_team_stats)
    df_all.to_csv(base_output_path + str(year) + '_close_games_team_stats_summary.csv')

    df_winners = df_all[df_all['Result'] == 'winner']
    df_winners.to_csv(base_output_path + str(year) + '_close_games_team_stats_winners.csv')


    df_losers = df_all[df_all['Result'] == 'loser']
    df_losers.to_csv(base_output_path + str(year) + '_close_games_team_stats_losers.csv')




for year in [2018, 2019, 2020, 2021, 2022, 2023, 2024]:
    print(year)
    input_file = path + str(year) + "_games.csv"  # File containing game IDs
    base_output_path = path

    # --- LOAD GAME IDS ---
    df = pd.read_csv(input_file)

    # --- INIT STORAGE ---
    all_play_by_plays = []
    all_team_stats = []

    # --- PROCESS EACH GAME ---
    for game_id in df['id']:
    #    print(f"Processing Game ID: {game_id}")

        with open(path + "ESPN/" +str(game_id) + '.json', 'r') as f:
            data = json.load(f)
        

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


    df_all = pd.DataFrame(all_team_stats)
    df_all.to_csv(base_output_path + str(year) + '_all_games_team_stats_summary.csv')

    df_winners = df_all[df_all['Result'] == 'winner']
    df_winners.to_csv(base_output_path + str(year) + '_all_games_team_stats_winners.csv')


    df_losers = df_all[df_all['Result'] == 'loser']
    df_losers.to_csv(base_output_path + str(year) + '_all_games_team_stats_losers.csv')