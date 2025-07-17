from turtle import Screen

from player import Player
from scoreboard import Scoreboard
from draw_line import DrawStartingLine
from car_manager import CarManager

import time

screen = Screen()
screen.setup(width=600,height=600)
screen.title('Turtle Crossing Game')
screen.bgcolor('black')
screen.tracer(0)


scoreboard = Scoreboard()
player = Player()
starting_line = DrawStartingLine(-270,-190,270,-190,'white',1)
starting_line = DrawStartingLine(-270,190,270,190,'white',1)

car_manager = CarManager()

screen.listen()
screen.onkeypress(player.go_up, 'Up')

game_is_on = True

while game_is_on:
  time.sleep(.1)
  screen.update()

  car_manager.create_car()
  car_manager.car_move()

  # Detect car collision
  for car in car_manager.all_cars:
    if car.distance(player)<20:
      game_is_on = False
      scoreboard.game_over()


  if player.finish_line():
    player.starting_position()
    scoreboard.update_score()
    car_manager.level_up()



screen.exitonclick()