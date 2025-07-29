import datetime as dt
import smtplib
import pandas
import random
from secret import my_email,my_password

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(row.month, row.day) : row for index,row in data.iterrows()}

today = dt.datetime.now()
today_tuple = (today.month, today.day)

if today_tuple in birthday_dict :
    birthday_person = birthday_dict[today_tuple]
    with open(f"./letter_templates/letter_{random.randint(1,3)}.txt") as letter_file :
        letter_old = letter_file.read()
        letter = letter_old.replace("[NAME]",birthday_person.name )
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection :
        connection.starttls()
        connection.login(user=my_email,password=my_password)
        connection.sendmail(from_addr=my_email,to_addrs=my_email,msg=f"Subject: Happy Birthday! \n\n {letter}")
