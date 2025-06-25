# One-Score Heartbreaks: Analyzing Close Games in College Football

This is the public repository for our **Erdos Institute Data Science Bootcamp** team project (Summer 2025).

**Team Members:** Lawrence Seminario-Romero, Alan Curtin, Jeremy Naredo  

---

## Table of Contents  
- [Introduction](#introduction)  
- [Data Set](#data-set)  
- [Data Collection Process](#data-collection-process)  
- [Project Goals](#project-goals)  
- [Data Analysis](#data-analysis)  
- [Modeling Approaches](#modeling-approaches)
- [Results](#results) 
- [Stakeholders](#stakeholders)  

---

## Introduction
American football (or simply *football*) is a team sport where two teams compete to score points by advancing the ball into the opponent's end zone or by kicking the ball through the goalposts (also known as the *uprights*). Points are scored as follows:
- **Touchdown (6 points):** When a player carries or catches the ball in the opponent's end zone.
- **Extra Point (1 point):** After a touchdown, the team may attempt a kick from the 3-yard line through the uprights.
- **Two-Point Conversion (2 points):** After a touchdown, the team may attempt a single play from the 3-yard line to run or pass the ball into the end zone.
- **Field Goal (3 points):** When the team kicks the ball through the uprights, typically on 4th down within reasonable distance (often under 40 yards).
- **Safety (2 points):** When the defense tackles an offensive player with the ball in their own end zone, or an offensive penalty occurs there.

A game is typically considered *close* if the final point differential is **8 points or fewer** — the maximum possible on a single possession (touchdown + two-point conversion). These *one-score games* often feature the most dramatic moments of a season.

**Examples of one-score final scores:**
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
- Possession time  
- And more  

---

## Data Collection Process

Our data collection involved:
1. **Downloading Game IDs and final scores** from [CollegeFootballData.com](https://collegefootballdata.com/) for FBS seasons in 2018, 2019, and 2021–2024.  
   - We excluded 2020 due to COVID-19’s impact on team schedules and data reliability.
2. **Filtering games** with a final point differential of 8 points or fewer.
3. **Scraping team stats** for these games from ESPN using Python scripts and the filtered Game IDs.
4. **Storing the data** in Excel files for further analysis and modeling.

---

## Project Goals

1. **Identify which team stats are most predictive of winning a one-score game.**  
   - We applied hypothesis testing (right-tailed two-sample t-tests) to identify statistically significant differences in the team stats of a one-score game between winning and losing teams.

2. **Predict the winner of a one-score game.**  
   - We built predictive models using logistic regression and random forest classifiers.
   - Features included 3rd down efficiency, completion attempts, rushing yards, possession time, and more.

---

## Data Analysis

We collected data on 17 types of team stats for winning and losing teams in one-score games. To identify which stats were most significant, we conducted right-tailed two-sample t-tests at the 5% significance level. The results suggested that 10 team stats showed statistically significant differences between winners and losers.

<img alt="Boxplot example" src="Slides/Data Science Slides Pic 2.png">
<img alt="Boxplot example" src="Slides/Data Science Slides Pic 5.png">

We then analyzed multicollinearity to narrow down our predictors for modeling. See the figure below for feature correlations:

<img alt="Correlation matrix" src="Slides/Data Science Slides Pic 3.png">

Based on this analysis, our key performance indicators (KPIs) were:
- 3rd down efficiency
- Completion attempts
- Yards per pass
- Rushing attempts
- Yards per rush attempt
- Possession time
- Turnovers --- while this team stat was not statistically significant for teams that won a one-score game, this is a very important metric that we do want to account for because this statistic is associated with the loss of a possession, which to some degree significantly affects the outcome of a game. 

These features are most closely tied to situational execution in close games.

---

## Modeling Approaches

We used two machine learning methods:
- **Logistic Regression**
- **Random Forest Classification**

Our training data consisted of team stats from the 2018, 2019, and 2021–2023 FBS seasons. The 2024 season served as our test data.

We evaluated model performance using:
- Accuracy
- Confusion matrix
- Classification report
- ROC AUC score
- Feature importance / regression coefficients  

---

## Results

### Logistic Regression  
<img alt="Logistic Regression performance" src="Slides/Logistic Regression Info.png">  

- Accuracy: ~65.3% (modest predictive performance; better than random guessing on balanced data)

- Most influential predictors: rushing attempts, completion attempts, and yards per pass
  
- Possession time, yards per rush attempt, and 3rd down efficiency had positive effects, but were less influential

- Turnovers have a strong negative win impact, which is to be expected since this can be viewed as a loss of ball possession to the opponent
  
- ROC AUC: ~0.705 (some ability to separate wins from losses, but limited)
  
- Limitations: does not capture situational factors like red zone efficiency, strength of the opponent, or a change in game momentum caused by extreme plays or penalties  

---

### Random Forest Classification  
<img alt="Random Forest performance" src="Slides/Data Science Slides Pic 7.png">  

- Accuracy: ~64.5% (similar to logistic regression)
 
<img alt="Feature importance" src="Slides/Data Science Slides Pic 8.png">

- Strengths and weaknesses similar to logistic regression  

---

### Future Work  
Future directions for this project could include:
- Identifying features that consistently characterize teams that lose one-score games  
- Performing hyperparameter tuning using grid search  
- Applying cross-validation for more robust performance estimates  

---

## Stakeholders  

- **Coaching Staff:** Insights to improve situational strategy and decision-making  
- **Athletic Departments:** Metrics to evaluate coaching effectiveness and performance in close games  
- **Players:** Better understanding of execution in high-pressure scenarios  

---
