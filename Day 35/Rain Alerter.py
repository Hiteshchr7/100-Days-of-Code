import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client
from datetime import datetime
load_dotenv()
with open(r"C:\Users\Hitesh Chahar\OneDrive\Desktop\python\100-Days-of-Code\Day 35\run_log.txt", "a") as f:
    f.write("Script ran successfully at " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
api_key = os.environ.get("OpenWeatherMap_API_KEY")

api_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
param = {
    "lat": 31.769014,        
    "lon": 76.980997,                  
    "appid" : api_key,
    "units" : "metric",
    "cnt" : 4
}

response = requests.get(api_endpoint,params=param)
response.raise_for_status()
weather_data = response.json()

will_rain =  False
clouds_present = False
for data in weather_data["list"]:
    weather_id = data["weather"][0]["id"]
    if weather_id< 700 :
        will_rain = True

client = Client(account_sid,auth_token)
if will_rain :
    message = client.messages.create(
    body="It's going to rain. Bring an umbrella with you.☔",
    from_=os.environ.get("MY_TWILIO_NUM"),
    to=os.environ.get("MY_PHONE_NUM"),
    )
    print(message.status)


