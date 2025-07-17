from turtle import Screen

from paddle import Paddle
from ball import Ball
import time

from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('PONG game')
screen.tracer(0)


r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up, 'Up')
screen.onkeypress(r_paddle.go_down, 'Down')
screen.onkeypress(l_paddle.go_up, 'w')
screen.onkeypress(l_paddle.go_down, 's')

game_is_on = True

while game_is_on:
  time.sleep(ball.ball_speed)
  screen.update()
  ball.move()

  # detect wall collision
  if ball.ycor() > 280 or ball.ycor() < -280 :
    ball.bounce_y()

  # detect r_paddle collision
  if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
    ball.bounce_x()


  # detect r paddle misses
  if ball.xcor() > 430:
    ball.reset_position()
    scoreboard.l_point()

  # detect l paddle misses
  if ball.xcor() < -430:
    ball.reset_position()
    scoreboard.r_point()

  if scoreboard.l_score == 5:
    game_is_on = False
    scoreboard.game_over('LEFT')

  if scoreboard.r_score == 5:
    game_is_on = False
    scoreboard.game_over('RIGHT')

    

  


screen.exitonclick()