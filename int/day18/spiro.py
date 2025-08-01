import turtle as t
import random


tim = t.Turtle()
screen = t.Screen()
t.colormode(255)
tim.pensize(5)

def random_color():
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  return (r,g,b)

def direction():
  return random.choice([0,90,180,270])

for _ in range(100):
  tim.forward(30)
  tim.pencolor(random_color())
  tim.setheading(direction())
  
screen.exitonclick()