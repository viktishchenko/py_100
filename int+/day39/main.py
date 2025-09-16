from datetime import datetime, timedelta
import time as t
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

from flight_data import FlightData

datas22 = [
  {
    "city": "Paris",
    "iataCode": "PAR",
    "prices": 54
  },
  {
    "city": "Frankfurt",
    "iataCode": "FRA",
    "prices": 230
    # "prices": 42
  },
  {
    "city": "Tokyo",
    "iataCode": "HND",
    "prices": 485
  },
  {
    "city": "Hong Kong",
    "iataCode": "HKG",
    "prices": 551
  },
  {
    "city": "Istanbul",
    "iataCode": "IST",
    "prices": 95
  },
  {
    "city": "Kuala Lumpur",
    "iataCode": "KUL",
    "prices": 414
  },
  {
    "city": "New York",
    "iataCode": "NYC",
    "prices": 240
  },
  {
    "city": "San Francisco",
    "iataCode": "SFO",
    "prices": 260
  },
  {
    "city": "Dublin",
    "iataCode": "DUB",
    "prices": 378
  }
]

data_manager = DataManager()
sheet_data = datas22
# sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LON"


# for row in sheet_data:
#     if row["iataCode"] == '':
#         row["iataCode"] = flight_search.get_destination_data(row["city"])
#         # slowing down requests to avoid rate limit
#         t.sleep(2)
#         data_manager.destination_data = sheet_data
#         data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )


    cheapest_flight = flight_search.find_cheapest_flight(flight)
    print(f"{destination['city']}: { cheapest_flight.lowest_price if type(cheapest_flight.lowest_price) == str else ('£ ' + str(cheapest_flight.lowest_price))}")
    # Slowing down requests to avoid rate limit
    t.sleep(2)