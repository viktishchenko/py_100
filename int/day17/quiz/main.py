from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


def questions(data):
  question_bank = []
  for item in data:
    tmp = (Question(item['text'], item['answer']))
    question_bank.append(tmp)
  return question_bank

quiz = QuizBrain(questions(question_data))

while quiz.still_has_questions():
  quiz.next_question()
print('You\'ve completed the quiz!')
print(f'Your final score was: {quiz.score}/{len(question_data)}')