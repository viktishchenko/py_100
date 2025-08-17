import requests
import json
import os
from html import unescape
from datetime import datetime, timedelta

# Настройки кэша
CACHE_FILE = "int+/day34/quiz_cache.json"
CACHE_EXPIRE_HOURS = 12  # Через сколько часов кэш устаревает

def question_data(use_cache=True):
    """
    Получает вопросы с API или из кэша
    :param use_cache: Использовать кэшированные данные, если они актуальны
    :return: Список вопросов или None при ошибке
    """
    # Пытаемся загрузить из кэша
    if use_cache and cache_is_valid():
        try:
            print('грузим апельсины бочками')
            return load_from_cache()
        except Exception as e:
            print(f"Ошибка чтения кэша: {e}. Загружаем свежие данные...")

    # Получаем новые данные с API
    try:
        print('делаем запрос!!!!')
        response = requests.get(
            "https://opentdb.com/api.php",
            params={"amount": 10, "type": "boolean"},
            timeout=5
        )
        response.raise_for_status()
        data = response.json()
        
        if data.get("response_code") != 0:
            raise ValueError(f"API error: response_code {data.get('response_code')}")
        
        questions = data["results"]
        clean_questions(questions)
        
        # Сохраняем в кэш
        save_to_cache(questions)
        return questions
        
    except requests.exceptions.RequestException as e:
        print(f"Ошибка соединения: {e}")
        if use_cache and os.path.exists(CACHE_FILE):
            print("Используем устаревшие данные из кэша")
            return load_from_cache()
        return None
    except Exception as e:
        print(f"Ошибка обработки данных: {e}")
        return None

def clean_questions(questions):
    """Очищает HTML-сущности в вопросах и ответах"""
    for q in questions:
        q["question"] = unescape(q["question"])
        q["correct_answer"] = unescape(q["correct_answer"])

def cache_is_valid():
    """Проверяет актуальность кэша"""
    if not os.path.exists(CACHE_FILE):
        return False
        
    cache_time = datetime.fromtimestamp(os.path.getmtime(CACHE_FILE))
    return datetime.now() - cache_time < timedelta(hours=CACHE_EXPIRE_HOURS)

def save_to_cache(questions):
    """Сохраняет вопросы в кэш-файл"""
    try:
        with open(CACHE_FILE, "w") as f:
            json.dump({
                "timestamp": datetime.now().isoformat(),
                "questions": questions
            }, f, indent=2)
    except Exception as e:
        print(f"Ошибка сохранения кэша: {e}")

def load_from_cache():
    """Загружает вопросы из кэш-файла"""
    with open(CACHE_FILE, "r") as f:
        data = json.load(f)
        return data["questions"]

if __name__ == "__main__":
    # Тестирование работы модуля
    print("Тест загрузки вопросов...")
    questions = question_data()
    if questions:
        print(f"Успешно загружено {len(questions)} вопросов")
        print("Первый вопрос:", questions[0]["question"])
    else:
        print("Не удалось загрузить вопросы")