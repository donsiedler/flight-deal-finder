import os
from twilio.rest import Client

TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = os.environ.get("TWILIO_NUMBER")
MY_NUMBER = os.environ.get("MY_NUMBER")


class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    def send_notification(self, message):
        message = self.client.messages.create(
            from_=f"whatsapp:+{TWILIO_NUMBER}",
            body=f"{message}",
            to=f"whatsapp:+{MY_NUMBER}"
        )
        print(message.sid)
