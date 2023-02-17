from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

flight_search = FlightSearch()
for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(city_name=row["city"])

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

notification_manager = NotificationManager()

for city in sheet_data:
    flight_data = FlightData(city["iataCode"])
    flight = flight_data.get_cheapest_flight()

    try:
        if flight.price <= city["lowestPrice"]:
            notification_manager.send_notification(
                message=f"Low price alert! Only £{flight.price} to fly from "
                        f"{flight.origin_city}-{flight.origin_airport} to "
                        f"{flight.destination_city}-{flight.destination_airport}, "
                        f"from {flight.out_date} to {flight.return_date}."
            )
    except AttributeError:
        pass
