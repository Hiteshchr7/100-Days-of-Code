from twilio.rest import Client
import os

class NotificationManager:
    def __init__(self):
        self.client = Client(os.environ.get("TWILIO_ACCOUNT_SID"), os.environ.get("TWILIO_AUTH_TOKEN"))

    def send(self, sms):
        message = self.client.messages.create(
            body=f"{sms}",
            from_=os.environ.get("MY_TWILIO_NUM"),
            to=os.environ.get("MY_PHONE_NUM")
        )
        print(message.status)
