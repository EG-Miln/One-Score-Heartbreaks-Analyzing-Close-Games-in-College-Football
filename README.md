# One-Score Heartbreaks: Analyzing Narrow Losses in College Football

This is the public repository for our Erdos Institute Data Science Bootcamp team project (Summer 2025).

Team Members: Lawrence Seminario-Romero, Alan Curtin, Jeremy Naredo

# Table of Contents

## Introduction
In American football, or "football" for short, points are scored in the following ways:
- Touchdown (worth 6 points): this occurs when a player has the ball in the opponent's endzone via a run or a caught pass.
- Extra Point (worth 1 point): after scoring a touchdown, the scoring team has one attempt to successfully kick the ball through the field goal post (also known as the "uprights") from the 3 yard line. 
- Two-Point ConVersion (worth 2 points): after scoring a touchdown, the scoring team can elect to have one attempt to run or pass the ball to a player in the endzone from the 3 yard line.
- Field Goal (worth 3 points): this occurs when a team elects to kick the ball through the uprights from the last place the ball was marked in a 4th down situation. Typically, these are done when the offense is in the defense's yardage territory and is no more than 40 yards from the uprights.
- Safety (worth 2 points): this is usually scoring done by the defense, and it occurs when a ball carrier is tackled in their own endzone. It can also occur when a penalty is committed by the offense in their own endzone.

A football game can be considered "close" if the difference in points is **8 points or fewer**. These games are also called *one-score* games, and they do occur occasionally. 

**Examples of final scores in one-score games:**
- 21–28  
- 13–10  
- 14–20  

When these games are played, they sometimes offer the most dramatic moments of the season. However, they can be particularly stressful for players, coahces, and fans alike. 

## Data Set

We are analyzing one-score games in college football. Specifically, we will primarily focus on Division I FBS games. The data that we will be examining and utilizing for our modeling consist of in-game team stats such as 3rd down efficiency, completion attempts, turnovers, and more. 

## Data Collection Process

We gathered data using the following steps:
1. Downloaded Game IDs and final scores for games played across multiple FBS seasons from [CollegeFootballData.com](https://collegefootballdata.com/). We primarily looked at FBS seasons played in 2018, 2019, and 2021-2024. We ignored the 2020 season since the COVID-19 Pandemic was on-going, and several of the team stats for the games that were played that year may not be fully reliable. 
2. Since we care about the final point differential to be 8 or less, we applied a filter to extract the relevant Game IDs of several one-score games into a CSV file.
3. Used Python scripts to scrape all of the team stats for each one-score game from the ESPN website using these Game IDs.
4. Saved the extracted data into Excel files for further data analysis and preditive modeling.

## Project Goals

1. **Identify which team stats are most predictive of winning a one-score game**  
   - Conducted a hypothesis testing using the two-sample t-test to see which team stats were statistically significant between winning and losing teams. 

2. **Predict the winner of a one-score game**  
   - Build predictive models via logistic regression and random forest classification using in-game team stats.
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
