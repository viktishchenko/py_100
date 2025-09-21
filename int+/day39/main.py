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
    "lowestPrice": 54
  },
  {
    "city": "Frankfurt",
    "iataCode": "FRA",
    "lowestPrice": 230
    # "lowestPrice": 42
  },
  {
    "city": "Tokyo",
    "iataCode": "HND",
    "lowestPrice": 485
  },
  {
    "city": "Hong Kong",
    "iataCode": "HKG",
    "lowestPrice": 551
  },
  {
    "city": "Istanbul",
    "iataCode": "IST",
    "lowestPrice": 95
  },
  {
    "city": "Kuala Lumpur",
    "iataCode": "KUL",
    "lowestPrice": 414
  },
  {
    "city": "New York",
    "iataCode": "NYC",
    "lowestPrice": 740
    # "lowestPrice": 240
  },
  {
    "city": "San Francisco",
    "iataCode": "SFO",
    "lowestPrice": 260
  },
  {
    "city": "Dublin",
    "iataCode": "DUB",
    "lowestPrice": 378
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
    # print(f"{destination['city']}: { cheapest_flight.lowest_price if type(cheapest_flight.lowest_price) == str else ('£ ' + str(cheapest_flight.lowest_price))}")
    # Slowing down requests to avoid rate limit
    t.sleep(2)

    if cheapest_flight.lowest_price != "N/A" and cheapest_flight.lowest_price < destination["lowestPrice"]:
    #   print(f"Lower price flight found to {destination['city']}!")
      # notification_manager.send_sms(
      #     message_body=f"Low price alert! Only £{cheapest_flight.price} to fly "
      #                  f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
      #                  f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
      # )
      # SMS not working? Try whatsapp instead.
      # notification_manager.send_whatsapp(
      #     message_body=f"Low price alert! Only £{cheapest_flight.price} to fly "
      #                   f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
      #                   f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
      # )
      # Anithing not working? Try telegas instead.
      notification_manager.telegram_bot_send_text(
      f"Low price alert! Only £{cheapest_flight.lowest_price} to fly from {cheapest_flight.origin} "
      f"to {cheapest_flight.destination}, "
      f"from {cheapest_flight.out_date} to {cheapest_flight.return_date}."
      )