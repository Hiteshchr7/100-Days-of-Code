import time
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

fs = FlightSearch()
dm = DataManager()
nm = NotificationManager()
sheet_data = dm.retrieve()

ORIGIN_CITY = "DEL"
tomorrow = datetime.now() + timedelta(days=1)
six_months = datetime.now() + timedelta(days=180)

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = fs.get_iataCode(row["city"])
        time.sleep(2)
dm.transfer(iataCode=row["iataCode"], row_num=sheet_data.index(row)+2)

for row in sheet_data:
    flights = fs.check_flights(ORIGIN_CITY, row["iataCode"], tomorrow, six_months)
    if flights:
        cheapest = find_cheapest_flight(flights)
        if cheapest.price != "N/A" and cheapest.price < row["lowestPrice"]:
            message = f"Low price alert! Only ${cheapest.price} to fly from {cheapest.origin_airport} to {cheapest.destination_airport} from {cheapest.out_date} to {cheapest.return_date}."
            nm.send(message)
