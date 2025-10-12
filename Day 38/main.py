import dotenv
import os
import requests
from datetime import datetime 
dotenv.load_dotenv()

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
GENDER = os.environ.get("GENDER")
WEIGHT_KG = os.environ.get("WEIGHT_KG")
HEIGHT_CM = os.environ.get("HEIGHT_CM")
AGE =os.environ.get("AGE")
api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
 
body = {
    "query" : input("What exercise did you do: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

header = {
    "x-app-id" : APP_ID ,
    "x-app-key" : API_KEY
}

response = requests.post(api_endpoint,headers=header,json=body)
result  = response.json()
#print(result)
now  = datetime.now()
today = now.strftime("%d/%m/%y")
time = now.strftime("%X")

sheet_endpoint = os.environ.get("sheet_endpoint")

for exercise in result["exercises"] :
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

bearer_headers = {
"Authorization": f"Bearer {os.environ.get('YOUR_TOKEN')}"
}
#use above parameter in sheet response request to use as bearer token as header as specified in the line below
#headers=bearer_headers
sheet_response = requests.post(sheet_endpoint, json=sheet_inputs,auth=(os.environ.get("sheety_username"),os.environ.get("sheety_password")))
#print(sheet_response.text)