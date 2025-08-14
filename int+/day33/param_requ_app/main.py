import requests
import datetime as dt


ENDPOINT = 'https://api.sunrise-sunset.org/json'
MY_LAT = 54.989811
MY_LNG = 73.374413


parameters = {
  'lat': MY_LAT,
  'lng': MY_LNG,
  'formatted': 0
}

response = requests.get(ENDPOINT, params=parameters)
# https://api.sunrise-sunset.org/json?lat=54.989811&lng=73.374413
response.raise_for_status()
data = response.json()
# ______PRINT DATA______
# data>>> {'results': {'sunrise': '11:37:38 PM', 'sunset': '2:44:44 PM', 'solar_noon': '7:11:11 AM', 'day_length': '15:07:06', 'civil_twilight_begin': '10:57:34 PM', 'civil_twilight_end': '3:24:47 PM', 'nautical_twilight_begin': '10:01:28 PM', 'nautical_twilight_end': 
# '4:20:54 PM', 'astronomical_twilight_begin': '8:44:30 PM', 'astronomical_twilight_end': '5:37:52 PM'}, 'status': 'OK', 'tzid': 'UTC'}
  # &formatted=1
# sunrise = data['results']['sunrise'] # 11:37:38 PM
  # sunrise.split('T') # ['2025-08-13', '23:37:38+00:00']
  # sunrise.split('T')[1] # 23:37:38+00:00
  # sunrise.split('T')[1].split(':') # ['23', '37', '38+00', '00']
  # sunrise.split('T')[1].split(':')[0] # 23
  # &formatted=0
# sunset = data['results']['sunset'] # 2025-08-14T14:44:44+00:00
# now = dt.datetime.now() # 2025-08-14 14:04:26.321699
sunrise = data['results']['sunrise'].split('T')[1].split(':')[0] # 23
sunset = data['results']['sunset'].split('T')[1].split(':')[0] # 14
now = dt.datetime.now().hour # 14
