from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

flight_search = FlightSearch()
for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(city_name=row["city"])

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

for row in sheet_data:
    flight_data = FlightData(row["iataCode"])
    flight_data.get_cheapest_flight()
