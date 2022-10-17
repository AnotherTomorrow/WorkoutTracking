import requests
from datetime import datetime

# Constants
API_KEY = "YOUR API KEY"
APP_ID = "YOUR ID KEY"

NUTRI_ENDPOINT = "https://trackapi.nutritionix.com"
EXERCISE_ENDPOINT = "/v2/natural/exercise"

USERNAME = "YOUR USERNAME"
PROJECT_NAME = "NAME OF PROJECT NAME"
SHEET_NAME = "SHEET NAME"

# API Headers
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

# user inputs a sentence of the exercise they did.
body = {
    'query': input("What kind of exercise did you do today? ")
}

# Posts the exercise they did, and retrieves the estimated exercise data.
request = requests.post(f"{NUTRI_ENDPOINT}{EXERCISE_ENDPOINT}", data=body, headers=headers)
data = request.json()

exercise = data["exercises"][0]["user_input"]
duration = round(data["exercises"][0]["duration_min"])
calories = round(data["exercises"][0]["nf_calories"])

# Gets time and date
today = datetime.now().strftime("%d/%m/%Y")
today_time = datetime.now().strftime("%X")

sheety_endpoint = "YOUR SHEETY ENDPOINT"

header_sheety = {
    "Authorization": "Basic VG9wOmxha3Vqc25nZnRpeWI0YTIhQCMkMm4=",
    'Content-Type': 'application/json'
}

workout_info = {
    "workout":
        {
            "date": today,
            "time": today_time,
            "exercise": exercise.title(),
            "duration": duration,
            "calories": calories
        }
}

# Connects, and updates the sheet with the exercise information.
sheety_post = requests.post(sheety_endpoint, json=workout_info, headers=header_sheety)
