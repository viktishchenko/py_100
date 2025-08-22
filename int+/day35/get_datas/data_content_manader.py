import os
from dotenv import load_dotenv
import requests

# Загрузка переменных окружения из .env файла
load_dotenv()

ENDPOINT = os.getenv('ENDPOINT')
LATITUDE = os.getenv('LATITUDE')
LONGITUDE = os.getenv('LONGITUDE')
API_KYE = os.getenv('API_KEY2')
UNITS = os.getenv('UNITS')

parameters = {
  'lat': LATITUDE,
  'lon': LONGITUDE,
  'appid': API_KYE,
  'units': UNITS,
}

def get_data_safe():
    try:
        with requests.Session() as session:
            response = session.get(ENDPOINT, params=parameters, timeout=10)
            response.raise_for_status()
            return response.json()
    except Exception as e:
        print(f"Ошибка: {e}")
        return None

print(get_data_safe())