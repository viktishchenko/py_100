from turtle import Turtle


class DrawStartingLine(Turtle):
  def __init__(self, x1, y1, x2, y2, color="red", width=1):
    super().__init__()
    self.color('white')
    self.hideturtle()
    self.pen(pencolor=color,pensize=width)
    self.pu()
    self.goto(x1,y1)
    self.pd()
    self.goto(x2,y2)