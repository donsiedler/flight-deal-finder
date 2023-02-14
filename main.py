from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

for row in sheet_data:
    if row["iataCode"] == "":
        flight_search = FlightSearch()
        row["iataCode"] = flight_search.get_destination_code(city_name=row["city"])

print(f"Sheet data: {sheet_data}")
print(f"Destination data: {data_manager.destination_data}")