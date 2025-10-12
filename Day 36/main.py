import requests
import random
import os
from dotenv import load_dotenv
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
load_dotenv()
param1 = {"function" : "TIME_SERIES_DAILY","symbol" :STOCK,"apikey":os.environ.get("stock_api_key")}
response1 = requests.get("https://www.alphavantage.co/query",params=param1)
response1.raise_for_status()
data1 = response1.json()
dates = list(data1["Time Series (Daily)"].values())
stock_cp_yest = float(dates[0]["4. close"])
stock_cp_dby = float(dates[1]["4. close"])

percent_change = ((stock_cp_yest - stock_cp_dby) / stock_cp_yest) * 100
arrow = "🔺" if percent_change > 0 else "🔻"

if abs(percent_change) >=5 :

    param2 = {"q" : COMPANY_NAME,"apiKey" : os.environ.get("api_key")}
    response2 = requests.get("https://newsapi.org/v2/everything",params=param2)
    response2.raise_for_status()
    data2 = response2.json()

    news = random.sample(data2["articles"],3)

    account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    client = Client(account_sid,auth_token)

    for article in  news :
        msg = client.messages.create(
            body= f'TSLA: {arrow}{percent_change:.1f}% \nHeadline: {article["title"]}. \nBrief: {article["description"]}',
            from_=os.environ.get("MY_TWILIO_NUM"),
            to=os.environ.get("MY_PHONE_NUM"),
        )
        print(msg.status)