import requests
import datetime as dt
import smtplib
import time
from secret import my_email,my_password
my_lat = 31.769014
my_lng = 76.980997

def iss_is_overhead():
    URL = "http://api.open-notify.org/iss-now.json"
    response = requests.get(URL)
    data = response.json()
    iss_longitude =float(data["iss_position"]["longitude"])
    iss_latitude =float(data["iss_position"]["latitude"])
    position = (iss_latitude,iss_longitude)
    if  my_lat - 5 <= iss_latitude <= my_lat + 5 and my_lng - 5 <= iss_longitude <= my_lng +5 :
        return True

# Checking for dark so that we can know to view iss when it's visible
def is_nighttime():
    parameters = {
        "lat": my_lat ,
        "lng": my_lng ,
        "formatted": 0,
        }
    response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    current_hour = dt.datetime.now().hour

    if  sunset <= current_hour or current_hour <= sunrise :
        return True


while True :
    time.sleep(60)
    if is_nighttime() and iss_is_overhead() :
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(my_email,my_password)
        connection.sendmail(from_addr=my_email,to_addrs=my_email,msg="Subject: LOOK UP☝🏻 \n\n The ISS is above you in the sky.")