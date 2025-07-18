from turtle import Turtle,Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Welcome to a Snake Game!')
screen.tracer(0)

starting_position = [(0,0),(-20,0),(-40,0)]

segments = []

for position in starting_position:
  segment = Turtle('square')
  segment.color('white')
  segment.pu()
  segment.goto(position)
  segments.append(segment)

game_is_on = True

while game_is_on:
  screen.update()
  time.sleep(0.1)

  for seg_num in range(len(segments)-1,0,-1):
    new_x = segments[seg_num-1].xcor()
    new_y = segments[seg_num-1].ycor()
    print(f'segments>>> {segments}')
    print(f'new_x>>> {seg_num}→{new_x} | new_y>>> {seg_num}→{new_y}')
    segments[seg_num].goto(new_x,new_y)

  segments[0].forward(20)
  # segments[0].left(90)














screen.exitonclick()

