import os
import logging
from pathlib import Path

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('day24_2_advanced/letter_generation.log')
    ]
)

# Определяем пути к файлам
BASE_DIR = Path('D:/pyAngela/day24_2_4')
INPUT_NAMES_PATH = BASE_DIR / 'Input/Names/invited_names.txt'
INPUT_LETTER_PATH = BASE_DIR / 'Input/Letters/starting_letter.txt'
OUTPUT_DIR = BASE_DIR / 'Output/ReadyToSend/Deep'

def check_paths():
    """Проверяет существование необходимых файлов и директорий."""
    if not INPUT_NAMES_PATH.exists():
        logging.error(f"Файл с именами не найден: {INPUT_NAMES_PATH}")
        return False
    
    if not INPUT_LETTER_PATH.exists():
        logging.error(f"Файл шаблона письма не найден: {INPUT_LETTER_PATH}")
        return False
    
    if not OUTPUT_DIR.exists():
        try:
            OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
            logging.info(f"Создана директория для выходных файлов: {OUTPUT_DIR}")
        except Exception as e:
            logging.error(f"Не удалось создать директорию {OUTPUT_DIR}: {e}")
            return False
    
    return True

def generate_letters():
    """Генерирует персонализированные письма."""
    if not check_paths():
        return
    
    try:
        # Читаем шаблон письма один раз перед циклом
        with open(INPUT_LETTER_PATH, 'r') as letter_file:
            letter_template = letter_file.readlines()
        logging.info("Шаблон письма успешно загружен")
        
        # Обрабатываем каждое имя
        with open(INPUT_NAMES_PATH, 'r') as names_file:
            names = [name.strip() for name in names_file if name.strip()]
            
        if not names:
            logging.warning("Файл с именами пуст или не содержит валидных имен")
            return
            
        logging.info(f"Найдено {len(names)} имен для обработки")
        
        for name in names:
            try:
                # Создаем персонализированное письмо
                personalized_letter = [line.replace('[name]', name) for line in letter_template]
                
                # Сохраняем письмо в файл
                output_path = OUTPUT_DIR / f'letter_for_{name}.txt'
                with open(output_path, 'w') as output_file:
                    output_file.writelines(personalized_letter)
                
                logging.info(f"Успешно создано письмо для {name}")
                
            except Exception as e:
                logging.error(f"Ошибка при создании письма для {name}: {e}")
                continue
                
    except Exception as e:
        logging.error(f"Критическая ошибка: {e}")
    finally:
        logging.info("Обработка завершена")

if __name__ == "__main__":
    logging.info("Запуск генерации писем")
    generate_letters()