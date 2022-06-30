import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = 100
HEIGHT_CM = 188
AGE = 26

APP_ID = os.environ["419abde1"]
API_KEY = os.environ["f776b019a2d103a283966819b1ae52a6"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ["https://api.sheety.co/46f72050469559c6f24d0998df4904da/myWorkouts/workouts"]

exercise_text = input("Tell me which exercises you did: ")

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

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    #Basic Auth
    sheet_response = requests.post(
        sheet_endpoint, 
        json=sheet_inputs, 
        auth=(
            os.environ["dpetkov354"],
            os.environ["960352871454Vv!"],
        )
    )

    print(sheet_response.text)
