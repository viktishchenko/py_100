from html import unescape
from typing import List  # Добавляем аннотации типов
from question_model import Question

class QuizBrain:
    def __init__(self, q_list: List[Question]):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    @property
    def total_questions(self) -> int:
        return len(self.question_list)

    def still_has_questions(self) -> bool:
        return self.question_number < self.total_questions

    def next_question(self) -> str:
        if not self.still_has_questions():
            raise IndexError("No more questions")
            
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        return f"Q.{self.question_number}: {unescape(self.current_question.text)}"

    def check_answer(self, user_answer: str) -> bool:
        if not self.current_question:
            raise ValueError("No current question")
            
        is_correct = user_answer.lower() == self.current_question.answer.lower()
        if is_correct:
            self.score += 1
        return is_correct