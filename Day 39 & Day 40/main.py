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

# Fill IATA codes if missing
for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = fs.get_iataCode(row["city"])
        time.sleep(2)
        dm.transfer(iataCode=row["iataCode"], row_num=sheet_data.index(row) + 2)

# Retrieve customer emails
sheet_email_data = dm.retrieve_customer_emails()
customer_email_list = [row["whatIsYourEmail?"] for row in sheet_email_data]

# Check flights
for row in sheet_data:
    flights = fs.check_flights(ORIGIN_CITY, row["iataCode"], tomorrow, six_months)

    if not flights or not flights.get('data'):
        flights = fs.check_flights(ORIGIN_CITY, row["iataCode"], tomorrow, six_months, is_direct=False)

    if flights:
        cheapest_flight = find_cheapest_flight(flights)

        if cheapest_flight.price != "N/A" and cheapest_flight.price < float(row["lowestPrice"]):
            if cheapest_flight.stops == 0:
                message = (
                    f"Low price alert! Only ₹{cheapest_flight.price} to fly direct "
                    f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                    f"departing {cheapest_flight.out_date} and returning {cheapest_flight.return_date}."
                )
            else:
                message = (
                    f"Low price alert! Only ₹{cheapest_flight.price} to fly "
                    f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                    f"with {cheapest_flight.stops} stop(s), "
                    f"departing {cheapest_flight.out_date} and returning {cheapest_flight.return_date}."
                )

            print(f"✅ Check your email. Lower price flight found to {row['city']}!")
            # Send SMS
            nm.send(message)
            # Send Emails
            nm.send_emails(email_list=customer_email_list, email_body=message)
        else:
            print(f"ℹ️ No cheaper flights found for {row['city']}. Cheapest available: ₹{cheapest_flight.price}")
    else:
        print(f"❌ No flights found at all for {row['city']}.")
