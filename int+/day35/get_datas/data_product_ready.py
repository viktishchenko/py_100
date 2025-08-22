import requests
import logging
from typing import Optional, Dict, Any

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

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_data(
    endpoint: str,
    params: Optional[Dict] = None,
    timeout: int = 10
) -> Optional[Dict[str, Any]]:
    """
    Безопасное получение данных с API
    
    Args:
        endpoint: URL API
        params: параметры запроса
        timeout: таймаут в секундах
        
    Returns:
        Dict с данными или None при ошибке
    """
    try:
        logger.info(f"Запрос к {endpoint} с параметрами {params}")
        
        with requests.Session() as session:
            response = session.get(
                endpoint,
                params=params,
                timeout=timeout,
                headers={'User-Agent': 'MyApp/1.0'}
            )
            response.raise_for_status()
            
            data = response.json()
            logger.info(f"Успешно получено {len(data)} элементов")
            return data
            
    except requests.exceptions.Timeout:
        logger.error("Таймаут запроса")
    except requests.exceptions.ConnectionError:
        logger.error("Ошибка подключения")
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP ошибка: {e}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Ошибка запроса: {e}")
    except ValueError as e:
        logger.error(f"Ошибка парсинга JSON: {e}")
    except Exception as e:
        logger.error(f"Неожиданная ошибка: {e}")
    
    return None

data = get_data(ENDPOINT, parameters)
if data:
    print(data)
else:
    print("Не удалось получить данные")