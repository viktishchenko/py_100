# main.py
import logging
from logging_config import setup_logging
from weather import WeatherAPI

import sys
from pathlib import Path

# Добавляем путь к модулям
current_dir = Path(__file__).parent
sys.path.append(str(current_dir))

# Импортируем настройку логирования
try:
    from logging_config import setup_logging, get_logger
    setup_logging()
except ImportError:
    # Запасной вариант если файл конфигурации не найден
    import logging
    logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')
    print("Файл конфигурации логирования не найден, используется базовая настройка")

logger = get_logger(__name__)

# Настройка логирования
setup_logging()

logger = logging.getLogger(__name__)

def main():
    logger.info("Запуск приложения погоды")
    
    try:
        weather_api = WeatherAPI()
        data = weather_api.get_weather_with_retry()
        
        if data:
            logger.info("Данные успешно получены")
            print(f'data>>> {data}')
        else:
            logger.error("Не удалось получить данные")
            
    except Exception as e:
        logger.critical("Критическая ошибка в приложении", exc_info=True)

if __name__ == "__main__":
    main()