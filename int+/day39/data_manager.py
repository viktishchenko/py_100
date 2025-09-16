import os
import requests
from dotenv import load_dotenv

load_dotenv()

SHEETY_PRICES_ENDPOINT = os.getenv('SHEETY_PRICES_ENDPOINT')
AUTH_TOKEN = f"{os.getenv('SHEETY_TOKEN')}"
HEADER_AUTH = {"Authorization": f"{os.getenv('SHEETY_TOKEN')}"}

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT,  headers=HEADER_AUTH)
        response.raise_for_status()
        data = response.json()
        # print(f'data>>> {data}')
        # data>>> {'price': [{'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 2}, {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 3}]}
        self.destination_data = data['price']
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=HEADER_AUTH
            )
            print(response.text)
            # {
            #   "price": {
            #     "iataCode": "NYC",
            #     "id": 2
            #   }
            # }
            # {
            #   "price": {
            #     "iataCode": "SFO",
            #     "id": 3
            #   }
            # }