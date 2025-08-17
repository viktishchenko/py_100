from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

  def __init__(self, quiz_brain: QuizBrain):
    self.quiz = quiz_brain

    self.window = Tk()
    self.window.title('Quizler')
    self.window.config(padx=20, pady=20, bg=THEME_COLOR)

    def get_quote() -> None:
      print('halo')
      pass


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
    self.true_button = Button(image=self.true_img, highlightthickness=0, command=get_quote)
    self.true_button.grid(row=2, column=0, pady=20)

    self.false_img = PhotoImage(file="int+/day34/images/false.png")
    self.false_button = Button(image=self.false_img, highlightthickness=0, command=get_quote)
    self.false_button.grid(row=2, column=1, pady=20)

    self.get_next_question()


    self.window.mainloop()

  def get_next_question(self):
    q_text = self.quiz.next_question()
    self.canvas.itemconfig(self.quiz_text, text=q_text)







# def get_quote():
#   print('грузим апельсины бочками')

# window = Tk()
# window.title("Quizler")
# window.config(padx=50, pady=50, bg=THEME_COLOR)
# score = 0

# score = Label(text=f'Score: {score}', font=("Arial", 18, "normal"), fg='white', bg=THEME_COLOR, justify='right' )
# score.grid(column=1,row=0, columnspan=2)

# canvas = Canvas(width=320, height=250, bg='white')
# quiz_text = canvas.create_text(200, 100, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="red")
# canvas.grid(row=1, column=0, columnspan=2, pady=30)

# true_img = PhotoImage(file="int+/day34/images/true.png")
# true_button = Button(image=true_img, highlightthickness=0, command=get_quote)
# true_button.grid(row=2, column=0)

# false_img = PhotoImage(file="int+/day34/images/false.png")
# false_button = Button(image=false_img, highlightthickness=0, command=get_quote)
# false_button.grid(row=2, column=1)

# window.mainloop()

