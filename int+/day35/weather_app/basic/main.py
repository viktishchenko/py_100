import os
import requests
from pathlib import Path
from dotenv import load_dotenv
from requests.exceptions import RequestException

# Загрузка .env из папки config
current_dir = Path(__file__).parent  # Директория текущего файла
env_path = current_dir.parent / 'pro' / 'config' / '.env'  # Поднимаемся на уровень выше

if env_path.exists():
# Загрузка переменных окружения из .env файла
    load_dotenv(dotenv_path=env_path)
    print(f"Загружен .env файл: {env_path}")
else:
    print("Файл .env не найден по пути:", env_path)

ENDPOINT = os.getenv('ENDPOINT')
LATITUDE = os.getenv('LATITUDE')
LONGITUDE = os.getenv('LONGITUDE')
API_KYE = os.getenv('API_KEY')
UNITS = os.getenv('UNITS')

parameters = {
  'lat': LATITUDE,
  'lon': LONGITUDE,
  'appid': API_KYE,
  'units': UNITS,
  'cnt': 4
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