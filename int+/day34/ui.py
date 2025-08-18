from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

  def __init__(self, quiz_brain: QuizBrain):
    self.quiz = quiz_brain

    self.window = Tk()
    self.window.title('Quizler')
    self.window.config(padx=20, pady=20, bg=THEME_COLOR)

    self.score = Label(text=f'Score: 0', font=("Arial", 14, "normal"), fg='white', bg=THEME_COLOR, justify='right' )
    self.score.grid(column=1,row=0, columnspan=2)

    self.canvas = Canvas(width=300, height=250, bg='white')
    self.quiz_text = self.canvas.create_text(
      150,
      100,
      text='Halo there!', 
      width=280,
      font=("Arial", 20, "italic"),
      fill=THEME_COLOR)
    self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

    self.true_img = PhotoImage(file="int+/day34/images/true.png")
    self.true_button = Button(image=self.true_img, highlightthickness=0, command=self.true_pressed)
    self.true_button.grid(row=2, column=0, pady=20)

    self.false_img = PhotoImage(file="int+/day34/images/false.png")
    self.false_button = Button(image=self.false_img, highlightthickness=0, command=self.false_pressed)
    self.false_button.grid(row=2, column=1, pady=20)

    self.get_next_question()


    self.window.mainloop()

  def get_next_question(self):
    self.canvas.config(bg='white')    
    if self.quiz.still_has_questions():
      self.score.config(text=f'Score: {self.quiz.score}')
      q_text = self.quiz.next_question()
      self.canvas.itemconfig(self.quiz_text, text=q_text)
    else:
      self.score.config(text=f'Score: {self.quiz.score}')
      self.canvas.itemconfig(self.quiz_text, text=f"You\'v reached the end of the quiz!\nYour result: {self.quiz.score}/{len(self.quiz.question_list)}")
      self.true_button.config(state='disabled')
      self.false_button.config(state='disabled')


  def true_pressed(self):
    self.get_feedback(self.quiz.check_answer('True'))

  def false_pressed(self):
    self.get_feedback(self.quiz.check_answer('False'))

  def get_feedback(self,is_right):
    if is_right:
      self.canvas.config(bg="#88e6a4")
    else:
      self.canvas.config(bg="#f18d8d")
    self.window.after(500, self.get_next_question)
