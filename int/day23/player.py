from turtle import Turtle


STARTING_POSITION = (0,-240)
DIRECTION = 90
MOVE_DISTANCE = 10
FINISH_LINE_Y = 200

class Player(Turtle):
  def __init__(self):
    super().__init__()
    self.color('white')
    self.shape('turtle')
    self.pu()
    self.setheading(DIRECTION)
    self.starting_position()

  def go_up(self):
    self.forward(MOVE_DISTANCE)

  def starting_position(self):
    self.goto(STARTING_POSITION)

  def finish_line(self):
    if self.ycor() > FINISH_LINE_Y:
      return True
    else: return False

