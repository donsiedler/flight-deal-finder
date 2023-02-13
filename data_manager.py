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

    @staticmethod
    def get_sheet_data():
        response = requests.get(url=SHEETY_ENDPOINT, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data["prices"]
