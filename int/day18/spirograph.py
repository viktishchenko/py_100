import turtle as t
import random


tim = t.Turtle()
screen = t.Screen()
t.colormode(255)
tim.pensize(1)
tim.speed('fastest')

def random_color():
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  return (r,g,b)

def move(size):
    for _ in range(int(360/size)):
      tim.pencolor(random_color())
      tim.circle(100)
      tim.setheading(tim.heading() + size)

move(20)

screen.exitonclick()