from question_model import Question
from deep_data.data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface
from typing import List

def initialize_quiz():
    """Инициализация викторины"""
    try:
        questions = question_data()
        if not questions:
            raise ValueError("Failed to load questions")
            
        question_bank = [
            Question(q["question"], q["correct_answer"])
            for q in questions
        ]
        
        quiz = QuizBrain(question_bank)
        QuizInterface(quiz)
        
    except Exception as e:
        print(f"Error initializing quiz: {e}")

if __name__ == "__main__":
    initialize_quiz()