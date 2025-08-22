# logging_config.py
import logging
import logging.config
from pathlib import Path
import os

def setup_logging(log_dir: str = "int+/day35/weather_app/pro/logs"):
    """
    Расширенная конфигурация логирования
    
    Args:
        log_dir: Путь к директории для логов
    """
    
    # Создаем полный путь к директории логов
    log_path = Path(log_dir)
    
    try:
        # Создаем директорию для логов (рекурсивно, включая все родительские папки)
        log_path.mkdir(parents=True, exist_ok=True)
        print(f"Директория для логов создана: {log_path.absolute()}")
    except Exception as e:
        print(f"Ошибка создания директории логов: {e}")
        # Используем текущую директорию как запасной вариант
        log_path = Path("logs")
        log_path.mkdir(exist_ok=True)
        print(f"Используем директорию по умолчанию: {log_path.absolute()}")
    
    # Полные пути к файлам логов
    info_log = log_path / "weather_app.log"
    debug_log = log_path / "weather_debug.log"
    error_log = log_path / "weather_errors.log"
    
    log_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S"
            },
            "detailed": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s"
            },
            "simple": {
                "format": "%(levelname)s - %(message)s"
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "INFO",
                "formatter": "simple",
                "stream": "ext://sys.stdout"
            },
            "file_info": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "INFO",
                "formatter": "standard",
                "filename": str(info_log),
                "maxBytes": 10485760,  # 10MB
                "backupCount": 5,
                "encoding": "utf-8"
            },
            "file_debug": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "DEBUG",
                "formatter": "detailed",
                "filename": str(debug_log),
                "maxBytes": 10485760,
                "backupCount": 3,
                "encoding": "utf-8"
            },
            "file_error": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "ERROR",
                "formatter": "detailed",
                "filename": str(error_log),
                "maxBytes": 5242880,  # 5MB
                "backupCount": 10,
                "encoding": "utf-8"
            }
        },
        "loggers": {
            "": {  # root logger
                "handlers": ["console", "file_info", "file_debug", "file_error"],
                "level": "DEBUG",
                "propagate": True
            },
            "urllib3": {
                "level": "WARNING",
                "propagate": True
            },
            "requests": {
                "level": "WARNING",
                "propagate": True
            }
        }
    }
    
    # Применяем конфигурацию
    try:
        logging.config.dictConfig(log_config)
        logging.getLogger(__name__).info("Логирование настроено успешно")
        logging.getLogger(__name__).debug(f"Логи сохраняются в: {log_path.absolute()}")
    except Exception as e:
        print(f"Ошибка настройки логирования: {e}")
        # Базовая настройка как запасной вариант
        logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def get_logger(name: str = None):
    """
    Возвращает настроенный логгер
    
    Args:
        name: Имя логгера (обычно __name__)
    
    Returns:
        Настроенный логгер
    """
    return logging.getLogger(name)

# Автоматическая настройка при импорте
setup_logging()