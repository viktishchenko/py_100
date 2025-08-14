# py -m pip install requests

# 1xx hold on
# 2xx here you go
# 3xx go away
# 4xx you screwed up
# 5xx i screwed up

import requests

ENDPOINT = 'http://api.open-notify.org/iss-now.json'

response = requests.get(url=ENDPOINT)
# print(response) # <Response [200]>
# print(response.status_code) # 200
  # _______BASIC_______
# if response.status_code != 200:
#   raise Exception('Bad response from ISS API.') # Exception: Bad response from ISS API.
# if response.status_code == 404:
#   raise Exception('This resource does not exist.')
  # _______REUQESTS LIB_______
  # _______raise_for_status()_______
response.raise_for_status() # requests.exceptions.HTTPError: 404 Client Error: Not Found for url: http://api.open-notify.org/iss1-now.json

  # _______json()_______
data = response.json() # {'timestamp': 1755152780, 'iss_position': {'longitude': '-86.6135', 'latitude': '-42.3749'}, 'message': 'success'}

longitude = data['iss_position']['longitude'] # -79.4050
latitude = data['iss_position']['latitude'] # -79.4050

  # _______https://www.latlong.net/_______
iss_position = (longitude,latitude) # ('-64.9375', '-26.2193')
data['iss_position'] # {'longitude': '-61.0635', 'latitude': '-22.0500'}


