import random
import time
from turtle import Screen

from cars import Cars
from player import Player


screen = Screen()
screen.tracer(0)
screen.title('Cross Road Game')
screen.setup(600,600)
screen.bgcolor('black')

player = Player()
car = Cars()

screen.listen()
screen.onkeypress(player.go_up, 'Up')

game_is_on = True

while game_is_on:
  time.sleep(.01)
  screen.update()

  car.create_car()
  car.car_move()







screen.exitonclick()