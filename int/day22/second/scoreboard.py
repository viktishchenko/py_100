from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier',40,'bold')
FONT_2 = ('Courier',26,'bold')

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.color('white')
    self.pu()
    self.hideturtle()
    self.goto(0, 220)
    self.r_score = 0
    self.l_score = 0
    self.update_score_board()

  def r_point(self):
    self.r_score +=1
    self.clear()
    self.update_score_board()

  def l_point(self):
    self.l_score +=1
    self.clear()
    self.update_score_board()

  def update_score_board(self):
    self.write(f'{self.l_score} | {self.r_score}', False, align=ALIGNMENT, font=FONT_2)

  def game_over(self, player):
      self.goto(0,0)
      self.write(f'{player} PLAYER WIN. GAME OVER', False, align=ALIGNMENT, font=FONT_2)