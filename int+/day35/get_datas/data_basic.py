import os
import requests
from dotenv import load_dotenv
from requests.exceptions import RequestException

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

def get_data():
  try:
    response = requests.get(ENDPOINT, params=parameters)
    response.raise_for_status()
    return response.json()
  except RequestException  as e:
    print(f'Ошибка запроса>>> {e}')
    return None
  except ValueError as e:
    print(f"Ошибка парсинга JSON: {e}")
    return None

result = get_data()
if result:
    print(result)
else:
    print("Не удалось получить данные")


