from turtle import Turtle
# import turtle as t
import random
# py -m pip install heroes // add heroes
# import heroes

def line(num):
  for _ in range(num):
    tim.pd()
    tim.forward(num)
    tim.pu()
    tim.forward(num)

def turn(derection, angle):
  if derection == 'left':
    tim.left(360/angle)
  else:
    tim.right(360/angle)

# def random_color():
#   r = random.randint(0,255)
#   g = random.randint(0,255)
#   b = random.randint(0,255)
#   tuple = (r,g,b)
#   return tuple

def colorize():
  colors = ['red','yellow', 'green', 'pink','orange', 'black', 'purple']
  color = random.choice(colors)
  return color
  



tim = Turtle()
tim.goto(-100,-180)
# t.colormode(255)

num = 2
while num < 7:
  # print(f'num>>> {num}')
  tim.shape('turtle')
  tim.color('gray')
  tim.pensize(5)
  num += 1  
  # tim.pencolor(random_color())
  tim.pencolor(colorize())
  for _ in range(num):
    line(10)
    turn('left', num)

