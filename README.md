# One-Score Heartbreaks: Analyzing Narrow Losses in College Football

This is the public repository for our Erdos Institute Data Science Bootcamp team project.

## Data Set

We are analyzing *one-score* games in college football — games where the final point differential is **8 points or fewer**.

**Examples of final scores in one-score games:**
- 21–28  
- 13–10  
- 14–20  

One-score games occasionaly occur in college football and these can sometimes provide the most dramatic moments of the season. However, they can be particularly stressful for players, coaches, and fans alike.

Our dataset includes:
- **Team Stats:** 3rd down efficiency, completion attempts, turnovers, rushing yards, time of possession, and more.

## Data Collection Process

We gathered data using the following steps:
1. Downloaded Game IDs for multiple FBS seasons from [CollegeFootballData.com](https://collegefootballdata.com/).
2. Filtered for one-score games and saved the relevant Game IDs into a CSV file.
3. Used Python scripts to scrape team stats from ESPN using these Game IDs.
4. Saved the extracted data into Excel files for further analysis.

## Project Goals

1. **Identify which team stats are most predictive of winning a one-score game**  
   - Apply logistic regression to assess feature importance.

2. **Predict the winner of a one-score game**  
   - Build predictive models using in-game team stats.
   - Focus on features like 3rd down efficiency, completion attempts, etc.

## Key Performance Indicators (KPIs)

We are focusing on situational execution KPIs, including:
- 3rd down conversion rates
- Completion attempts
- Yards per pass
- Rushing yards
- Time of possession

## Stakeholders

- **Coaching Staff:** Gain insights to improve in-game decision-making and situational awareness.
- **Athletic Departments:** Evaluate coaching effectiveness and team performance in close games.
- **Football Players:** Better understand individual and team execution under high-pressure situations.
