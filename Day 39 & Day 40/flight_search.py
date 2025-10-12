import requests
from datetime import datetime
import os
from dotenv import load_dotenv
import time

load_dotenv()

IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

class FlightSearch:
    def __init__(self):
        self._api_key = os.environ.get("amadeus_api_key")
        self._api_secret = os.environ.get("amadeus_api_secret")
        self._token = self._get_new_token()

    def _get_new_token(self):
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)
        time.sleep(1)
        return response.json()['access_token']

    def get_iataCode(self, city_name):
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {"keyword": city_name, "max": "2", "include": "AIRPORTS"}
        response = requests.get(url=IATA_ENDPOINT, headers=headers, params=query)
        time.sleep(1)
        try:
            return response.json()["data"][0]['iataCode']
        except (IndexError, KeyError):
            return "N/A"

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time,is_direct=True):
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true" if is_direct else "false",
            "currencyCode": "INR",
            "max": "10",
        }
        response = requests.get(url=FLIGHT_ENDPOINT, headers=headers, params=query)
        time.sleep(1)
        if response.status_code != 200:
            return None
        return response.json()
