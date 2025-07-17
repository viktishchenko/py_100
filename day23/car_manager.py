import random
from turtle import Turtle

COLORS = ['red', 'orange','yellow','green','blue','purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
  def __init__(self):
    self.all_cars = []
    self.create_car()
    self.car_speed = STARTING_MOVE_DISTANCE


  def colorize(self):
    color = random.choice(COLORS)
    return color
  
  def level_up(self):
    self.car_speed += MOVE_INCREMENT


  def create_car(self):
    random_chance = random.randint(1,6)
    if random_chance == 1:
      new_car = Turtle()
      new_car.color(self.colorize())
      new_car.shape('square')
      new_car.shapesize(stretch_len=2,stretch_wid=1)
      new_car.pu()
      random_y = random.randint(-180,180)
      new_car.goto(200, random_y)
      self.all_cars.append(new_car)

    
  
  def car_move(self):
    for car in self.all_cars:
      car.backward(self.car_speed)
