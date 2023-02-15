from datetime import datetime, timedelta
import requests

from flight_search import KIWI_ENDPOINT, API_HEADERS


class FlightData:
    def __init__(self, city_code):
        self.fly_from = "LON"
        self.fly_to = city_code,
        self.date_from = (datetime.today() + timedelta(days=1)).strftime("%d/%m/%Y")  # Tomorrow
        self.date_to = (datetime.today() + timedelta(days=180)).strftime("%d/%m/%Y")  # In 6 months time
        self.nights_in_dst_from = 7
        self.nights_in_dst_to = 21
        self.ret_from_diff_city = False
        self.ret_to_diff_city = False
        self.curr = "GBP"
        self.limit = 1

        # Set after successful response from API
        self.price = None
        self.origin_city = None
        self.origin_airport = None
        self.destination_city = None
        self.destination_airport = None
        self.out_date = None
        self.return_date = None

    def get_cheapest_flight(self):
        params = {
            "fly_from": self.fly_from,
            "fly_to": self.fly_to,
            "date_from": self.date_from,
            "date_to": self.date_to,
            "nights_in_dst_from": self.nights_in_dst_from,
            "nights_in_dst_to": self.nights_in_dst_to,
            "ret_from_diff_city": self.ret_from_diff_city,
            "ret_to_diff_city": self.ret_to_diff_city,
            "curr": self.curr,
            "limit": self.limit,
        }

        response = requests.get(f"{KIWI_ENDPOINT}/v2/search", headers=API_HEADERS, params=params)
        response.raise_for_status()
        data = response.json()

        try:
            flight = data["data"][0]
            print(flight)
            self.price = flight["price"]
            self.origin_city = flight["cityFrom"]
            self.origin_airport = flight["route"][0]["flyFrom"]
            self.destination_city = flight["cityTo"]
            self.destination_airport = flight["route"][0]["flyTo"]
            self.out_date = flight["route"][0]["utc_departure"].split("T")[0]
            self.return_date = flight["route"][1]["utc_departure"].split("T")[0]

        except IndexError:
            print(f"No flights found for {self.fly_to}")
            return None

        return self
