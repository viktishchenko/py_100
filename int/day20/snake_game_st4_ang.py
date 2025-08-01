from turtle import Screen
import time

import snake_st4_ang as s

screen = Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.tracer(0)

snake = s.Snake()

game_is_on = True

while game_is_on:
  screen.update()
  time.sleep(0.1)

  snake.move()


screen.exitonclick()


