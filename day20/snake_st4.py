import turtle

class Snake:

  STARTING_POSITION = [(0,0),(-20,0),(-40,0)]

  SEGMENTS = []

  def __init__(self):
    self.create_snake()


  def create_snake(self,shape='square',color='white'):
    
    self.color = color
    self.shape = shape

    for position in self.STARTING_POSITION:
      new_segment = turtle.Turtle(self.shape)
      new_segment.color(self.color)
      new_segment.pu()
      new_segment.goto(position)
      self.SEGMENTS.append(new_segment)
      print(f'self.SEGMENTS>>> {self.SEGMENTS}')


  def move(self,forward=0, left=0):

    for seg_num in range(len(self.SEGMENTS)-1,0,-1):
      new_x = self.SEGMENTS[seg_num-1].xcor()
      new_y = self.SEGMENTS[seg_num-1].ycor()
      self.SEGMENTS[seg_num].goto(new_x,new_y)

    self.SEGMENTS[0].forward(forward)
    self.SEGMENTS[0].left(left)