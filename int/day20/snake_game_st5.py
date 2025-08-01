from turtle import Screen
import time

import snake_st5 as s

screen = Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.tracer(0)

snake = s.Snake()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True

while game_is_on:
  screen.update()
  time.sleep(0.5)

  snake.move()


screen.exitonclick()


