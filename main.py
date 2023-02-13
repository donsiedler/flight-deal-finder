from data_manager import DataManager
from flight_data import FlightData

data_manager = DataManager()
sheet_data = data_manager.get_sheet_data()
print(sheet_data)

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = FlightData.get_flight_data(row["city"])

print(sheet_data)
