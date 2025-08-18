class Question:
    """Модель вопроса с аннотацией типов"""
    def __init__(self, text: str, answer: str):
        self.text = text
        self.answer = answer.capitalize()  # Нормализуем ответ (True/False)