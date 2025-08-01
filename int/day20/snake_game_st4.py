from turtle import Screen
import time

import snake_st4 as s

screen = Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.tracer(0) # turn turtle animation on/off

snake = s.Snake()

game_is_on = True

while game_is_on:
  screen.update() # update screen w tracer(↑)
  time.sleep(0.1)

  snake.move(20, 90)


screen.exitonclick()


