# One-Score Heartbreaks: Close Games in College Football

This is the public repository for our **Erdos Institute Data Science Bootcamp** team project (Summer 2025).

**Team Members:** Lawrence Seminario-Romero, Alan Curtin, Jeremy Naredo  

---

## Table of Contents  
- [Introduction](#introduction)  
- [Data Set](#data-set)  
- [Data Collection Process](#data-collection-process)  
- [Project Goals](#project-goals)  
- [Key Performance Indicators (KPIs)](#key-performance-indicators-kpis)  
- [Stakeholders](#stakeholders)  

---

## Introduction
American football (or simply *football*) is a team sport in which two teams compete to score points by advancing the ball into the opponent's end zone or through kicking the ball through the goalposts (also known as the *uprights*). Points are scored in the following ways:
- **Touchdown (6 points):** When a player carries or catches the ball in the opponent's end zone.
- **Extra Point (1 point):** After a touchdown, the team may attempt to kick the ball through the uprights from the 3-yard line. The team gets only one extra point attempt per touchdown. 
- **Two-Point Conversion (2 points):** After a touchdown, the team may attempt a single play from the 3-yard line to run or pass the ball into the end zone.
- **Field Goal (3 points):** When the team attempts to kick the ball through the uprights. This is typically done on a 4th down scenario and the ball is placed within reasonable range from the uprights (often under 40 yards).
- **Safety (2 points):** When the defense tackles an offensive player with the ball in their own end zone, or an offensive penalty occurs there.

A football game is typically considered *close* if the point differential is **8 points or fewer**. These games are sometimes called *one-score games*, and often deliver the most dramatic moments of a season, as well as be stressful for players, coaches, and fans alike.

**Examples of final scores in one-score games:**
- 28–21  
- 10–13  
- 20–14  

---

## Data Set

We are analyzing one-score games in **Division I FBS college football**. The dataset includes in-game team stats such as:
- 3rd down efficiency  
- Completion attempts  
- Turnovers  
- Yards gained  
- And more  

---

## Data Collection Process

Our data collection involved:
1. **Downloading Game IDs and final scores** from [CollegeFootballData.com](https://collegefootballdata.com/) for FBS seasons in 2018, 2019, and 2021–2024.  
   - We excluded 2020 due to COVID-19’s impact on team schedules and data reliability.
2. **Filtering games** where the final point differential was 8 points or fewer.
3. **Scraping team stats** for these games from the ESPN website using Python scripts and the filtered Game IDs.
4. **Storing the data** in Excel files for further analysis and predictive modeling.

---

## Project Goals

1. **Identify which team stats are most predictive of winning a one-score game**  
   - We applied hypothesis testing (two-sample t-tests) to identify statistically significant differences between winning and losing teams.

2. **Predict the winner of a one-score game**  
   - We built predictive models using logistic regression and random forest classifiers.
   - Our features included 3rd down efficiency, completion attempts, turnovers, and more.

---

## Data Analysis
We obtained data for 17 different types of team stats. We had the data corresponding to these team stats for winning and losing teams of each one-score game. Since we are interested in determining which of these team stats were statistically significant between the winning and losing teams, we carried out the following a right-tailed two-sample t-test at the 5% significance level. The results of the hypothesis test suggested that there are 10 types of team stats that significantly mattered for teams that won a one-score game. See the screenshot below for the corresponding test statistic and p-value.



---

## Key Performance Indicators (KPIs)

We focused on KPIs related to situational execution, including:
- 3rd down conversion rate  
- Completion attempts  
- Yards per pass  
- Rushing yards  
- Time of possession  

---

## Stakeholders

- **Coaching Staff:** Insights to improve decision-making and situational strategies.  
- **Athletic Departments:** Metrics for evaluating coaching effectiveness and team performance in close games.  
- **Players:** Deeper understanding of team and individual execution under high-pressure conditions.  
