import smtplib
import datetime as dt
import random
from secret import my_email,my_password
# Sends a motivational quote on monday
now = dt.datetime.now()
day_of_week = now.weekday()

with open("quotes.txt") as text_file :
    quotes_list = [text.strip() for text in text_file.readlines()]
    quote = random.choice(quotes_list)

if day_of_week == 0 :
   
    receiver_email = ".......@gmail.com"
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection: 
        connection.starttls()   
        connection.login(user=my_email,password=my_password)   
        connection.sendmail(from_addr=my_email,
                            to_addrs=receiver_email,
                            msg=f"Subject:Monday Motivation \n\n {quote}") 