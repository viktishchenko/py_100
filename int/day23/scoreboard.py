from turtle import Turtle

ALIGNMENT_GAME = 'center'
ALIGNMENT_LEVEL = 'left'
FONT = ('Courier',16,'normal')

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.level = 0
    self.hideturtle()
    self.color('white')
    self.pu()
    self.goto(-270,260)
    self.update_level()

  def game_over(self):
    self.goto(0,0)
    self.write(f'THE GAME OVER', False, align=ALIGNMENT_GAME, font=FONT)

  def update_score(self):
    self.level += 1
    self.clear()
    self.update_level()

  def update_level(self):
    self.write(f'Level: {self.level}', False, align=ALIGNMENT_LEVEL, font=FONT)


