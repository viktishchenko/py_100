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
  screen.update() # update screen w tracer(↑)
  time.sleep(0.1)
  for seg in segments:
    seg.forward(20)




screen.exitonclick()


