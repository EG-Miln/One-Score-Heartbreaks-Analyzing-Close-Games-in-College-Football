import pandas as pd

def time_to_seconds(time_str):
    if pd.isna(time_str):
        return np.nan
    try:
        minutes, seconds = map(int, str(time_str).split(':'))
        return minutes * 60 + seconds
    except:
        return np.nan