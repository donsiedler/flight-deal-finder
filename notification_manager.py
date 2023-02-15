import os
from twilio.rest import Client


class NotificationManager:
    example_message = "Low price alert! Only 63 GBP to fly from London-STN to Berlin-SFX, from 2023-02-15 to " \
                      "2023-02-28."

    account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    twilio_number = os.environ.get("TWILIO_NUMBER")
    my_number = os.environ.get("MY_NUMBER")

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_=f"whatsapp:+{twilio_number}",
        body=f"{example_message}",
        to=f"whatsapp:+{my_number}"
    )

    print(message.sid)
