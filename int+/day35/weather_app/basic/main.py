import os
import requests
from pathlib import Path
from dotenv import load_dotenv
from requests.exceptions import RequestException

# sms sender twilio
# from twilio.rest import Client # type: ignore

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

# sms sender twilio
ACCOUNT_SID = "twilio account sid"
AUTH_TOKEN = "twilio auth token"


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

def send_rain_sms():
  # client = Client(ACCOUNT_SID, AUTH_TOKEN)

  # message = client.messages.create(
  #               body="It's going to rain today. Make sure to bring an ☂",
  #               from_='your twiilio sample number',
  #               to='your twilio verified number'
  #           )
  # print(message.status)
  print('Twilio sms was sent!')

def check_rain():
  if result:
      for data in result['list']:
        if data['weather'][0]['id'] < 700:
          return send_rain_sms()
        else:
          return print('It\'s OK, no rain today')
  else:
      print("Не удалось получить данные")

print(check_rain())
   