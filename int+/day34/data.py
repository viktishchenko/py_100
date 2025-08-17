import requests


DATA_URL = 'https://opentdb.com/api.php'
AMOUNT = 10
TYPE = 'boolean'

parameters = {
    'amount': AMOUNT,
    'type': TYPE
}

def question_data():
    """Получает вопросы с удаленного сервера"""
    try:
        response = requests.get(url="https://opentdb.com/api.php", params=parameters)
        response.raise_for_status()  # Проверяет на ошибки HTTP
        data = response.json()
        return data["results"] # Возвращаем только массив с вопросами
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении данных: {e}")
        return None