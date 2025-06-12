# One-Score Heartbreaks: Analyzing Narrow Losses in College Football
Public repository for an Erdos Institute Data Science Bootcamp team project.

## Data Set
We are examining "one-score" games in college football. For the scope of this project, a "one-score" game is defined as a football game in which the final point differential is 8 points or fewer.

**Examples of Final Scores in a One-Score Game in College Football:**
- 21–28  
- 13–10  
- 14–20

Our dataset consists of the following components:
- **Team Stats**: 3rd down efficiency, completions and attempts, turnovers, etc.
- **Play-by-Play Information**: Detailed sequences of game events.

## Data Scraping Process
We collected the data using the following steps:

1. Downloaded Game IDs from multiple FBS seasons from [CollegeFootballData.com](https://collegefootballdata.com/).
2. Filtered for one-score games and saved the relevant Game IDs into a CSV file.
3. Used Python scripts to scrape Team Stats and Play-by-Play data from the ESPN website using the filtered Game IDs.
4. Saved the extracted data into separate Excel files for data analysis.

---

## Project Goals

1. **Identify Stats Most Predictive of Winning (or Losing) Close Games**
   - Use logistic regression or decision trees to assess feature importance.
   - Focus on situational stats: 3rd/4th down conversion rates, turnover margin, etc.

2. **Predict the Winner of a One-Score Game**
   - Build a predictive model using in-game and/or pre-game statistics.
   - Consider features like yards per play, turnover margin, etc.

---

## Key Performance Indicators (KPIs)
We have grouped our KPIs into the following categories:

### Game-Level KPIs
- Win-loss record in one-score games
- Average scoring margin in one-score games
- Number of comeback wins or blown leads

### Situational Execution KPIs
- 3rd and 4th down conversion rates
- Turnovers (overall and 4th quarter-specific)
- Time of possession in the 4th quarter
- Penalties (frequency and yardage)

### Coaching and Decision-Making KPIs
- 4th down decision analysis (actual vs. optimal decisions)
- Kicking decisions (field goal attempts vs. go-for-it situations)

## Stakeholders

1. **Coaching Staff**
   - Improve in-game decision-making and situational awareness.

2. **Athletic Departments**
   - Evaluate coaching effectiveness and team performance in tight contests.

3. **Football Players**
   - Understand individual and team execution under high-pressure situations.
