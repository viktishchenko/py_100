from turtle import Turtle

class Paddle(Turtle):
  def __init__(self,cor):
    super().__init__()
    self.shape('square')
    self.color('white')
    self.shapesize(stretch_len=1,stretch_wid=5)
    self.pu()
    self.goto(cor)


  def go_up(self):
    new_y = self.ycor() + 20
    self.goto(self.xcor(), new_y)

  def go_down(self):
    new_y = self.ycor() - 20
    self.goto(self.xcor(), new_y)