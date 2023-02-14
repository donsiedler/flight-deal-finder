import os
import requests

KIWI_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
API_HEADERS = {
    "apikey": os.environ.get("KIWI_API_KEY"),
    "content-type": "application/json",
}


class FlightSearch:

    def get_destination_code(self, city_name):
        params = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(KIWI_ENDPOINT, headers=API_HEADERS, params=params)
        response.raise_for_status()
        data = response.json()
        city_code = data["locations"][0]["code"]
        return city_code
