import os
import requests

USERNAME = os.environ.get("SHEETY_USERNAME")
PROJECT_NAME = "flightDeals"
SHEET_NAME = "prices"
SHEETY_ENDPOINT = f"https://api.sheety.co/{USERNAME}/{PROJECT_NAME}/{SHEET_NAME}"
SHEETY_AUTH_TOKEN = os.environ.get("SHEETY_AUTH_TOKEN")

headers = {
    "Authorization": f"Bearer {SHEETY_AUTH_TOKEN}"
}


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=headers)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for destination in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": destination["iataCode"],
                }
            }
            response = requests.put(
                f"{SHEETY_ENDPOINT}/{destination['id']}",
                json=new_data,
                headers=headers,
            )
            response.raise_for_status()
            print(response.text)
