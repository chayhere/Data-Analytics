# 💪🏼Workout Logger

## Overview / What I Did
A Python project that logs daily workouts (fetching details via API), stores all data automatically in Google Sheets, calculates calories burned and time spent, tracks exercises in real time, and summarizes daily activity.

## How & Impact
- Took user-inputted workouts and sent them to the Nutritionix API to retrieve structured exercise data.
- Extracted relevant details (duration, calories, exercise name) from the API response.
- Appended this data structurally into Google Sheets for storage and organization.
- Loaded the sheet into pandas DataFrame, cleaned and aggregated the data for analysis.
- Produced daily insights summarizing total calories burned and exercise duration, providing actionable fitness tracking.

## Tools / Skills Used
- **Python:** requests, pandas, datetime
- **APIs:** Nutritionix API (exercise data), Google Sheets API (data storage)
- **Cloud / Storage:** Google Sheets for structured data logging and aggregation
- **Data Handling:** cleaning, aggregation, summarization with pandas
- **Environment:** Local IDE (Pycharm) / Google Colab 

## Demo
![Code Demo](../../gifs/WorkoutLogger.gif)
