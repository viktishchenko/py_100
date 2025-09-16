from datetime import datetime, timedelta
import os
import requests
from flight_data import FlightData

AMADEUS_TOKEN_ENDPOINT = os.getenv("AMADEUS_TOKEN_ENDPOINT")
AMADEUS_ENDPOINT = os.getenv("AMADEUS_ENDPOINT")
AMADEUS_API_KEY = os.getenv("AMADEUS_API_KEY")
AMADEUS_API_SECRET = os.getenv("AMADEUS_API_SECRET")
AMADEUS_IATA_ENDPOINT = os.getenv("AMADEUS_IATA_ENDPOINT")

# curl "https://test.api.amadeus.com/v1/security/oauth2/token" \
#      -H "Content-Type: application/x-www-form-urlencoded" \
#      -d "grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}"



class FlightSearch:

    def __init__(self):
        self._api_key = os.getenv("AMADEUS_API_KEY")
        self._api_secret = os.getenv("AMADEUS_API_SECRET")
        # Getting a new token every time program is run. Could reuse unexpired tokens as an extension.
        self.expiration_time = datetime.now()
        # self.expiration_time = "2023-11-01"
        self._token = self._get_new_token()


        print(f'self._token>>> {self._token}')

    def _get_new_token(self):
        """
        Generates the authentication token used for accessing the Amadeus API and returns it.
        This function makes a POST request to the Amadeus token endpoint with the required
        credentials (API key and API secret) to obtain a new client credentials token.
        Upon receiving a response, the function updates the FlightSearch instance's token.
        Returns:
            str: The new access token obtained from the API response.
        """
        # Header with content type as per Amadeus documentation
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }
        data = requests.post(url=AMADEUS_TOKEN_ENDPOINT, headers=header, data=body, verify=False).json()
        # return requests.post(url=AMADEUS_TOKEN_ENDPOINT, headers=header, data=body, verify=False).json()#['access_token']
        data = requests.post(url=AMADEUS_TOKEN_ENDPOINT, headers=header, data=body, verify=False)
        data.raise_for_status()

        response = data.json()
        # print(f'response>>> {response}')
        # response>>> {'type': 'amadeusOAuth2Token', 'username': 'goyappirightnow@gmail.com', 'application_name': 'Flight_Deals', 'client_id': 'Ultb2qAOGVnMxBoZxlfk46zEYz2rgwtn', 'token_type': 'Bearer', 'access_token': 'xdPUCVIOj0FdYjPaWk3K514PgLIV', 'expires_in': 1799, 'state': 'approved', 'scope': ''}
        if response["state"] == "approved":
            self.expiration_time = self.expiration_time + timedelta(seconds=int(response["expires_in"]))

        return response['access_token']
    

    def get_destination_data(self, city_name):
        location_endpoint = f"{AMADEUS_IATA_ENDPOINT}"
        header = {"Authorization": f"Bearer {self._token}"}
        query = {"keyword": city_name, "max": "2", "include": "AIRPORTS"}
        response = requests.get(url=location_endpoint, headers=header, params=query)
        # print(f"Status code {response.status_code}. Airport IATA: {response.text}")
        try:
            code = response.json()["data"][0]['iataCode']
            # print(f'code>>> {code}')
            # code>>> NYC
            # code>>> SFO
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        header = {"Authorization": f"Bearer {self._token}"}
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": "10",
        }

        response = requests.get(
            url=f"{AMADEUS_ENDPOINT}",
            headers=header,
            params=query,
        )

        data = response.json()
        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
            "For details on status codes, check the API documentation:\n"
            "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
            "-reference")
            print("Response body:", response.text)
            return None
        return data
    
    def find_cheapest_flight(self,data):

        # Handle empty data if no flight or Amadeus rate limit exceeded
        if data is None or not data['data']:
            print("No flight data")
            return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")
        
        flight = data['data'][0]
        lowest_price = float(flight["price"]["grandTotal"])
        origin_airport = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
        destination_airport = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
        out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
        return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
        flight_data = FlightData(lowest_price, origin_airport,destination_airport,out_date,return_date)

        for flight in data["data"]:
            price = float(flight["price"]["grandTotal"])
            if price < float(lowest_price):
                flight_data = FlightData(
                lowest_price = price,
                origin = flight["itineraries"][0]["segments"][0]["departure"]   ["iataCode"],
                destination = flight["itineraries"][0]["segments"][0]["arrival"]    ["iataCode"],
                out_date = flight["itineraries"][0]["segments"][0]["departure"] ["at"].split("T")[0],
                return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0])
                print(f"Lowest price to {flight_data.destination} is £{flight_data.lowest_price}")

        return flight_data


        
        
            


