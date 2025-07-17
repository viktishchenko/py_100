from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier',16,'normal')

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.score = 0
    self.high_score = 0
    self.pu()
    self.color('white')
    self.goto(0,270)
    self.hideturtle()
    self.update_score_board()

  def update_score_board(self):
    self.clear()
    self.write(f'Score: {self.score} High score: {self.high_score}', False, align=ALIGNMENT, font=FONT)

  def reset(self):
    if self.score > self.high_score:
      self.high_score = self.score
    self.score = 0
    self.update_score_board()
  
  def scorenum(self):
    self.score +=1
    self.update_score_board()

