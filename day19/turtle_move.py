from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()

def move_forvards():
  tim.forward(10)

def move_backwards():
  tim.backward(10)

def turn_right():
  tim.setheading(tim.heading() - 10)

def turn_left():
  tim.left(10)

def clear_screen():
  tim.clear()
  tim.pu()
  tim.home()
  tim.pd()

screen.listen()
screen.onkey(move_forvards, 'w')
screen.onkey(move_backwards, 's')
screen.onkey(turn_left, 'a')
screen.onkey(turn_right, 'd')
screen.onkey(clear_screen, 'z')
screen.exitonclick()