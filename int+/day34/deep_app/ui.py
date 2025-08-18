from tkinter import *
from quiz_brain import QuizBrain
from pathlib import Path

THEME_COLOR = "#375362"
IMAGE_DIR = Path("int+/day34/images")  # Используем Path

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title('Quizler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self._setup_ui()
        self.window.mainloop()

    def _setup_ui(self):
        """Выносим настройку UI в отдельный метод"""
        self._setup_score_label()
        self._setup_canvas()
        self._setup_buttons()
        self.get_next_question()

    def _setup_score_label(self):
        self.score_label = Label(
            text='Score: 0',
            font=("Arial", 14),
            fg='white',
            bg=THEME_COLOR
        )
        self.score_label.grid(column=1, row=0)

    def _setup_canvas(self):
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            150, 125,  # Центрируем текст
            text='',
            width=250,  # Уменьшаем ширину для лучшего переноса
            font=("Arial", 18, "italic"),  # Увеличиваем шрифт
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

    def _setup_buttons(self):
        try:
            self.true_img = PhotoImage(file=IMAGE_DIR / "true.png")
            self.false_img = PhotoImage(file=IMAGE_DIR / "false.png")
        except:
            # Запасной вариант если изображения не загрузились
            self.true_img = PhotoImage(width=100, height=100)
            self.false_img = PhotoImage(width=100, height=100)
            
        self.true_button = Button(
            image=self.true_img,
            highlightthickness=0,
            command=lambda: self.process_answer("True")
        )
        self.true_button.grid(row=2, column=0, padx=20, pady=20)
        
        self.false_button = Button(
            image=self.false_img,
            highlightthickness=0,
            command=lambda: self.process_answer("False")
        )
        self.false_button.grid(row=2, column=1, padx=20, pady=20)

    def process_answer(self, answer: str):
        """Объединяем обработку ответов"""
        self.give_feedback(self.quiz.check_answer(answer))

    def give_feedback(self, is_correct: bool):
        """Переименовано для ясности"""
        color = "#88e6a4" if is_correct else "#f18d8d"
        self.canvas.config(bg=color)
        self.score_label.config(text=f'Score: {self.quiz.score}')
        self.window.after(1000, self.get_next_question)

    def get_next_question(self):
        self.canvas.config(bg='white')
        
        if self.quiz.still_has_questions():
            try:
                q_text = self.quiz.next_question()
                self.canvas.itemconfig(self.question_text, text=q_text)
            except Exception as e:
                self.show_error(str(e))
        else:
            self.end_quiz()

    def end_quiz(self):
        """Выносим завершение викторины в отдельный метод"""
        score = self.quiz.score
        total = self.quiz.total_questions
        self.canvas.itemconfig(
            self.question_text,
            text=f"Quiz completed!\nFinal score: {score}/{total}"
        )
        self.true_button.config(state='disabled')
        self.false_button.config(state='disabled')

    def show_error(self, message: str):
        """Показываем ошибки пользователю"""
        self.canvas.itemconfig(
            self.question_text,
            text=f"Error: {message}",
            fill="red"
        )