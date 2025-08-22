import os
import requests
import logging
from dotenv import load_dotenv
from pathlib import Path
from requests.exceptions import RequestException, Timeout, ConnectionError, HTTPError
from typing import Dict, Any, Optional
from datetime import datetime

class WeatherAPI:
    def __init__(self, env_path: Optional[str] = None):
        # Настройка логирования
        self._setup_logging()
        
        self.logger = logging.getLogger(__name__)
        self.logger.info("Инициализация WeatherAPI")
        
        self._load_environment(env_path)
        self._validate_environment()
        
        self.parameters = {
            'lat': os.getenv('LATITUDE'),
            'lon': os.getenv('LONGITUDE'),
            'appid': os.getenv('API_KEY'),
            'units': os.getenv('UNITS', 'metric'),
            'cnt': os.getenv('CNT', '4')
        }
        
        self.endpoint = os.getenv('ENDPOINT')
        self.session = requests.Session()
        self.session.timeout = 10
        
        self.logger.debug("WeatherAPI инициализирован успешно")

    def _setup_logging(self):
        """Настройка системы логирования"""
        # # Создаем директорию для логов если её нет
        # log_dir: str = "int+/day35/weather_app/pro/logs"
        log_dir = Path('int+/day35/weather_app/pro/logs')
        # log_dir = Path('logs')
        log_dir.mkdir(exist_ok=True)
        
        # Форматирование логов
        log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        date_format = '%Y-%m-%d %H:%M:%S'
        
        # Базовая конфигурация
        logging.basicConfig(
            level=logging.INFO,
            format=log_format,
            datefmt=date_format,
            handlers=[
                logging.FileHandler(
                    log_dir / f'weather_app_{datetime.now().strftime("%Y%m%d")}.log',
                    encoding='utf-8'
                ),
                logging.StreamHandler()  # Вывод в консоль
            ]
        )
        
        # Устанавливаем уровень для requests чтобы уменьшить шум
        logging.getLogger('urllib3').setLevel(logging.WARNING)

    def _load_environment(self, env_path: Optional[str] = None):
        """Загружает переменные окружения из .env файла"""
        self.logger.debug("Начало загрузки переменных окружения")
        
        if env_path:
            load_dotenv(dotenv_path=env_path)
            self.logger.info(f"Загружен .env файл по указанному пути: {env_path}")
        else:
            # Автопоиск .env файла
            current_dir = Path(__file__).parent
            possible_locations = [
                current_dir / '.env',
                current_dir.parent / '.env',
                current_dir / 'config' / '.env',
                Path.home() / '.weather_app' / '.env'
            ]
            
            for location in possible_locations:
                if location.exists():
                    load_dotenv(dotenv_path=location)
                    self.logger.info(f"Загружен .env файл: {location}")
                    return
            
            self.logger.warning(".env файл не найден, используем системные переменные")

    def _validate_environment(self):
        """Проверяет наличие обязательных переменных"""
        self.logger.debug("Валидация переменных окружения")
        
        required_vars = ['ENDPOINT', 'LATITUDE', 'LONGITUDE', 'API_KEY']
        missing_vars = []
        
        for var in required_vars:
            value = os.getenv(var)
            if not value:
                missing_vars.append(var)
            else:
                # Логируем наличие переменных (без чувствительных данных)
                masked_value = value[:3] + '***' + value[-3:] if len(value) > 6 else '***'
                self.logger.debug(f"Переменная {var}: {masked_value}")
        
        if missing_vars:
            error_msg = f"Отсутствуют обязательные переменные: {missing_vars}"
            self.logger.error(error_msg)
            raise EnvironmentError(error_msg)
        
        self.logger.info("Все обязательные переменные окружения найдены")

    def _log_request_details(self, url: str, params: Dict):
        """Логирует детали запроса (без чувствительных данных)"""
        safe_params = params.copy()
        if 'appid' in safe_params:
            safe_params['appid'] = safe_params['appid'][:3] + '***' + safe_params['appid'][-3:]
        
        self.logger.debug(f"Запрос к: {url}")
        self.logger.debug(f"Параметры запроса: {safe_params}")

    def _log_response_details(self, response: requests.Response):
        """Логирует детали ответа"""
        self.logger.debug(f"Статус ответа: {response.status_code}")
        self.logger.debug(f"Время ответа: {response.elapsed.total_seconds():.3f} сек.")
        self.logger.debug(f"Размер ответа: {len(response.content)} байт")

    def get_weather_data(self) -> Optional[Dict[str, Any]]:
        """Получает данные о погоде"""
        self.logger.info("Начало получения данных о погоде")
        
        try:
            self._log_request_details(self.endpoint, self.parameters)
            
            with self.session as session:
                response = session.get(
                    self.endpoint,
                    params=self.parameters,
                    timeout=15
                )
                
                self._log_response_details(response)
                response.raise_for_status()
                
                data = response.json()
                self.logger.info("Данные о погоде успешно получены")
                self.logger.debug(f"Получено данных: {len(str(data))} байт")
                
                return data
                
        except Timeout as e:
            self.logger.error(f"Таймаут запроса к API погоды: {e}")
            self.logger.warning("Сервер не ответил в течение 15 секунд")
            
        except ConnectionError as e:
            self.logger.error(f"Ошибка подключения к API погоды: {e}")
            self.logger.warning("Проверьте интернет-соединение")
            
        except HTTPError as e:
            self.logger.error(f"HTTP ошибка при запросе к API: {e}")
            if hasattr(e, 'response') and e.response:
                self.logger.error(f"Статус код: {e.response.status_code}")
                self.logger.error(f"Ответ сервера: {e.response.text[:200]}...")
            
        except RequestException as e:
            self.logger.error(f"Ошибка запроса к API погоды: {e}", exc_info=True)
            
        except ValueError as e:
            self.logger.error(f"Ошибка парсинга JSON ответа: {e}")
            self.logger.debug("Ответ сервера может быть в неверном формате")
            
        except Exception as e:
            self.logger.critical(f"Неожиданная ошибка: {e}", exc_info=True)
            
        return None

    def get_weather_with_retry(self, max_retries: int = 3, delay: int = 2) -> Optional[Dict[str, Any]]:
        """Получает данные о погоде с повторными попытками"""
        self.logger.info(f"Попытка получения данных с {max_retries} повторениями")
        
        for attempt in range(max_retries):
            try:
                self.logger.info(f"Попытка {attempt + 1}/{max_retries}")
                
                data = self.get_weather_data()
                if data:
                    self.logger.info("Данные успешно получены")
                    return data
                    
                if attempt < max_retries - 1:
                    self.logger.warning(f"Повторная попытка через {delay} секунд...")
                    import time
                    time.sleep(delay)
                    
            except Exception as e:
                self.logger.error(f"Ошибка в попытке {attempt + 1}: {e}")
                if attempt == max_retries - 1:
                    self.logger.error("Все попытки завершились ошибкой")
        
        return None

    def __del__(self):
        """Очистка ресурсов"""
        if hasattr(self, 'session'):
            self.session.close()
            self.logger.debug("HTTP сессия закрыта")

# Функция для тестирования
def test_weather_api():
    """Тестовая функция для демонстрации работы"""
    logger = logging.getLogger(__name__)
    logger.info("=" * 50)
    logger.info("Запуск теста WeatherAPI")
    logger.info("=" * 50)
    
    try:
        weather_api = WeatherAPI()
        
        logger.info("Получение данных о погоде...")
        data = weather_api.get_weather_with_retry()
        
        if data:
            logger.info("Тест завершен успешно!")
            # Логируем только основные данные, не весь ответ
            if 'main' in data:
                logger.info(f"Температура: {data['main'].get('temp', 'N/A')}°C")
            return True
        else:
            logger.error("Тест завершен с ошибкой")
            return False
            
    except Exception as e:
        logger.critical(f"Критическая ошибка при тестировании: {e}", exc_info=True)
        return False

if __name__ == "__main__":
    # Запуск теста
    success = test_weather_api()
    
    logger = logging.getLogger(__name__)
    if success:
        logger.info("✅ Приложение работает корректно")
    else:
        logger.error("❌ Приложение завершилось с ошибками")
    
    logger.info("Завершение работы приложения")