from turtle import Turtle, Screen

screen = Screen()
screen.setup(600,600)
screen.bgcolor('black')

starting_position = [(0,0),(-20,0),(-40,0)]
segments = []

for position in starting_position:
  new_segment = Turtle('square')
  new_segment.color('white')
  new_segment.pu()
  new_segment.goto(position)
  segments.append(new_segment)



screen.exitonclick()


