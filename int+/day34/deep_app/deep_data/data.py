import requests
import json
import os
from html import unescape
from datetime import datetime, timedelta
from pathlib import Path  # Добавлено для работы с путями

CACHE_DIR = Path("int+/day34/deep_app/deep_data/cache")  # Используем Path для кросс-платформенности
CACHE_FILE = CACHE_DIR / "quiz_cache.json"
CACHE_EXPIRE_HOURS = 12

def ensure_cache_dir():
    """Создает директорию для кэша, если её нет"""
    CACHE_DIR.mkdir(parents=True, exist_ok=True)

def question_data(use_cache=True):
    """Основная функция получения вопросов"""
    try:
        if use_cache and cache_is_valid():
            return load_from_cache()
        
        print('Делаем запрос к API...')
        questions = fetch_questions_from_api()
        if questions:
            save_to_cache(questions)
            return questions
            
        raise ValueError("Не удалось получить вопросы")
        
    except Exception as e:
        print(f"Ошибка: {e}")
        if use_cache and os.path.exists(CACHE_FILE):
            print("Используем кэш как запасной вариант")
            return load_from_cache()
        return []

def fetch_questions_from_api():
    """Выносим запрос к API в отдельную функцию"""
    response = requests.get(
        "https://opentdb.com/api.php",
        params={"amount": 10, "type": "boolean"},
        timeout=5
    )
    response.raise_for_status()
    data = response.json()
    
    if data.get("response_code") != 0:
        raise ValueError(f"API error: {data.get('response_code')}")
    
    questions = data["results"]
    clean_questions(questions)
    return questions
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

# Остальные функции (clean_questions, cache_is_valid, save_to_cache, load_from_cache) 
# остаются без изменений, но добавляем ensure_cache_dir() в save_to_cache:

def save_to_cache(questions):
    ensure_cache_dir()
    try:
        with open(CACHE_FILE, "w", encoding='utf-8') as f:
            json.dump({
                "timestamp": datetime.now().isoformat(),
                "questions": questions
            }, f, indent=2, ensure_ascii=False)  # ensure_ascii для корректного UTF-8
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