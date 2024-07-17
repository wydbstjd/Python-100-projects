import requests
from datetime import datetime

APP_ID = '"""'
API_KEY = '"""'

MY_KG = 60
MY_CM = 170
MY_AGE = 24

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/8aa4d80e723c57994888779f085de7e8/myWorkouts/workout"
exercise_text = input("Tell me which exercises you did: ")

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

parameter = {
    'query': exercise_text,
    'weight_kg': MY_KG,
    'height_cm': MY_CM,
    'age': MY_AGE
}

response = requests.post(url=exercise_endpoint, json=parameter, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result['exercises']:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, auth=("ID", "PASSWORD"))

    print(sheet_response.text)