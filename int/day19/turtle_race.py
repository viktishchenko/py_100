from turtle import Turtle,Screen
import random

is_race_on = False
screen = Screen()
screen.title('Welcome to a turtles race!')
screen.setup(width=500, height=400)
user_bet = (screen.textinput(title='Make your bet', prompt='Whitch turtle will win the race? Enter a color: '))
color_list = ['red', 'orange', 'yellow', 'green', 'lightblue', 'blue', 'violet']
y_position = [-100,-70,-40,-10,20,50,80]
turtles_list = []

if user_bet:
  is_race_on = True

for turtle_idx in range(0,7):
  new_turtle = Turtle(shape='turtle')
  new_turtle.pu()
  new_turtle.color(color_list[turtle_idx])
  new_turtle.goto(x=-230,y=y_position[turtle_idx])
  turtles_list.append(new_turtle)

while is_race_on:
  for turtle in turtles_list:
    if turtle.xcor() >= 220:
      is_race_on = False
      winning_color = turtle.pencolor()
      if winning_color == user_bet:
        print(f'you win, win-color is: {winning_color}')
      else: print(f'you lose, win-color is: {winning_color}')
    rand_distance = random.randint(0,10)
    turtle.forward(rand_distance)


screen.exitonclick()