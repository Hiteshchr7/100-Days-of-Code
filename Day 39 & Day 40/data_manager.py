import os
import requests
from dotenv import load_dotenv
import time

load_dotenv()

class DataManager:
    def __init__(self):
        self.sheet_price_endpoint = os.environ.get("sheet_price_endpoint")
        self.headers = {"Authorization": f"Bearer {os.environ.get('sheety_token')}"}
        self.sheet_users_endpoint = os.environ.get("sheet_users_endpoint")

    def retrieve(self):
        response = requests.get(url=self.sheet_price_endpoint, headers=self.headers)
        response.raise_for_status()
        time.sleep(2)  # avoid hitting API too fast
        return response.json()["prices"]

    def transfer(self, iataCode, row_num):
        body = {"price": {"iataCode": iataCode}}
        response = requests.put(url=f"{self.sheet_price_endpoint}/{row_num}", headers=self.headers, json=body)
        response.raise_for_status()
        time.sleep(1)
        return response.json()

    def retrieve_customer_emails(self):
        response =  requests.get(url=self.sheet_users_endpoint, headers=self.headers)
        response.raise_for_status()
        time.sleep(1) # avoid hitting API too fast
        return response.json()["users"]

