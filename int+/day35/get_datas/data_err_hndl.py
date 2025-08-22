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


def get_data_with_error_handling():
    try:
        response = requests.get(ENDPOINT, params=parameters, timeout=10)
        response.raise_for_status()
        return {"success": True, "data": response.json()}
        
    except requests.exceptions.Timeout:
        return {"success": False, "error": "Таймаут соединения"}
    except requests.exceptions.ConnectionError:
        return {"success": False, "error": "Ошибка подключения"}
    except requests.exceptions.HTTPError as e:
        return {"success": False, "error": f"HTTP ошибка: {e}"}
    except ValueError as e:
        return {"success": False, "error": f"Ошибка формата данных: {e}"}
    except Exception as e:
        return {"success": False, "error": f"Неизвестная ошибка: {e}"}

result = get_data_with_error_handling()
if result["success"]:
    print(result["data"])
else:
    print(f"Ошибка: {result['error']}")