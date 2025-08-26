# 1.Imports and Initial Setup
# This section imports all the necessary libraries for the project.
# - requests: Used to make API calls to external services.
# - pandas: The primary library for data manipulation and analysis.
# - gspread, oauth2client: Libraries for securely connecting to and interacting with Google Sheets.
# - datetime: Used to get the current date and time for timestamps.
import requests
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime

# Get the current date and time, which will be used to timestamp each workout log.
today_date = datetime.datetime.now().strftime("%x")
now_time = datetime.datetime.now().strftime("%X")

# 2.Google Sheets Connection
# Establishes a secure connection to Google Sheets using a service account.
# The `credentials.json` file contains the private key used for authentication.
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

# Opens the specific spreadsheet and worksheet where data will be stored.
# The sheet is identified by its unique key, and the worksheet by its name.
sheet_id = "1gI9MWSvG0QBWf1-SmuhvXSOhXWp-R7up6oniRa90xvw"
spreadsheet = client.open_by_key(sheet_id)
worksheet = spreadsheet.worksheet("workouts")

# 3.Nutritionix API Credentials
# These are the credentials for the Nutritionix Natural Language for Exercise API.
# Note: In a production environment, these values would be stored in
# environment variables for security, rather than hardcoded.
GENDER = "male"
WEIGHT_KG = 54
HEIGHT_CM = 170
AGE = 22
APP_ID = "efb7b2fe"
API_KEY = "c585272c6ab4d71b84aa88e3012304a6"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# 4.Sending a Natural Language Request to the API
# This section sends a text-based request to the Nutritionix API using the `requests` library.
# The API uses Natural Language Processing (NLP) to interpret the text and return structured data.
exercise_text = input("Enter your workouts: ")
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

# The `requests.post()` method posts new data to the API endpoint.
response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

# 5.Logging Data to Google Sheets
# This loop processes the structured data returned by the API.
# For each exercise identified, it appends a new row to the Google Sheet,
# The workout summaries are stored here to be printed in the final output.
workout_summaries = []
for exercise in result["exercises"]:
    # Extracts key data points to be saved.
    name = exercise["name"]
    duration = exercise["duration_min"]
    calories = exercise["nf_calories"]

    # The `append_row` method adds the data to the Google Sheet.
    row_data = [today_date, now_time, name, f"{duration:.2f}", f"{calories:.2f}"]
    worksheet.append_row(row_data)

# 6.Data Analysis with Pandas
# This section reads the data back from the sheet and using pandas to find meaningful insights.

# Reads all data from the Google Sheet and loads it into a Pandas DataFrame.
all_records = worksheet.get_all_records()
df = pd.DataFrame(all_records)

# Converts 'Calories' and 'Duration' columns to numeric values to make calculations possible.
# Any invalid or non-numeric entries are turned into NaN, which pandas can handle.
df['Calories'] = pd.to_numeric(df['Calories'], errors='coerce')
df['Duration'] = pd.to_numeric(df['Duration'], errors='coerce')

# Filters the DataFrame to only include workouts logged today.
today_df = df[df['Date'] == today_date]

# Groups the data by Exercise name and sums the duration and calories.
# This merges multiple entries of the same workout into a single row.
today_grouped = today_df.groupby('Exercise').agg({
    'Duration': 'sum',
    'Calories': 'sum'
}).reset_index()

# Creates a summary list for printing, similar to the previous style.
merged_workout_summaries = [
    f"{row['Exercise']}: {row['Duration']} min, {row['Calories']} cal 🔥"
    for _, row in today_grouped.iterrows()
]

# Calculates total calories burned and total duration for today.
total_calories_today = today_grouped['Calories'].sum()
total_duration_today = today_grouped['Duration'].sum()

# 7.Consolidated Final Output
# This final section provides a clear, single-block output for the user.
print("\nToday's Workout Log:")
print("\n".join(merged_workout_summaries))
print("\nOverall Fitness Summary:")
print(f"Spent {total_duration_today:.2f} min, burning {total_calories_today:.2f} cal today")
