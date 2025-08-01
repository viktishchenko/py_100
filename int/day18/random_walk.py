import random
from turtle import Turtle


tim = Turtle()

def random_walk():
  num = random.randint(0,1)
  if num == 0:
    return tim.backward(50)
  else:
    tim.forward(50)

def random_turn():
  num = random.choice([0,90,180,270])
  return num

def colorize():
  colors = ['red','yellow', 'green', 'pink','orange', 'black', 'purple']
  color = random.choice(colors)
  return color

num = 100

tim.shape('turtle')
tim.pensize(15)

while num:
  num -= 1
  tim.color(colorize())
  random_walk()
  tim.setheading(random_turn())

