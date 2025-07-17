from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier',16,'normal')

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.score = 0
    self.pu()
    self.color('white')
    self.goto(0,270)
    self.hideturtle()
    self.update_score_board()

  def update_score_board(self):
    self.write(f'Score: {self.score}', False, align=ALIGNMENT, font=FONT)

  def game_over(self):
    self.goto(0,0)
    self.write(f'GAME OVER', False, align=ALIGNMENT, font=FONT)



  
  def scorenum(self):
    self.score +=1
    self.clear()
    self.update_score_board()

