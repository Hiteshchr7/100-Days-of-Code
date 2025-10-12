from twilio.rest import Client
import smtplib
import os

class NotificationManager:
    def __init__(self):
        self.client = Client(os.environ.get("TWILIO_ACCOUNT_SID"), os.environ.get("TWILIO_AUTH_TOKEN"))
        self.my_email = os.environ.get("my_email")
        self.my_password = os.environ.get("my_password")

    def send(self, sms):
        message = self.client.messages.create(
            body=f"{sms}",
            from_=os.environ.get("MY_TWILIO_NUM"),
            to=os.environ.get("MY_PHONE_NUM")
        )
        print(message.status)

    def send_emails(self,email_list,email_body):
        with smtplib.SMTP("smtp.gmail.com",port=587) as connection :
            connection.starttls()
            connection.login(user=self.my_email,password=self.my_password)
            for email in email_list :
                connection.sendmail(from_addr=self.my_email,to_addrs=email,msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode("utf-8"))
