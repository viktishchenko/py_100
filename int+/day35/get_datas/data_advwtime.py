import requests
from requests.exceptions import RequestException
import time

import os
from dotenv import load_dotenv

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

def get_data_with_retry(max_retries=3, delay=2):
    for attempt in range(max_retries):
        try:
            response = requests.get(ENDPOINT, params=parameters, timeout=10)
            response.raise_for_status()
            return response.json()
            
        except RequestException as e:
            print(f"Попытка {attempt + 1}/{max_retries} не удалась: {e}")
            if attempt < max_retries - 1:
                time.sleep(delay)
            else:
                print("Все попытки завершились ошибкой")
                return None
        except ValueError as e:
            print(f"Ошибка парсинга JSON: {e}")
            return None

result = get_data_with_retry()
print(result)