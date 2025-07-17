from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.tracer(0) # turn turtle animation on/off

starting_position = [(0,0),(-20,0),(-40,0)]
segments = []

for position in starting_position:
  new_segment = Turtle('square')
  new_segment.color('white')
  new_segment.pu()
  new_segment.goto(position)
  segments.append(new_segment)

game_is_on = True

while game_is_on:
  '''добавил движение сегментов от последнего к начальному'''
  '''added moving segments from last to initial'''
  screen.update() # update screen w tracer(↑)
  time.sleep(0.1)
  for seg_num in range(len(segments)-1,0,-1):
    new_x = segments[seg_num-1].xcor()
    new_y = segments[seg_num-1].ycor()
    segments[seg_num].goto(new_x,new_y)

  segments[0].forward(20)
  segments[0].left(90)




screen.exitonclick()


