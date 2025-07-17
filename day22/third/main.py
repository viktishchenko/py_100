from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from settings import *
import time

# Настройка экрана
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(BG_COLOR)
screen.title(TITLE)
screen.tracer(0)

# Создание объектов
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Управление
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

# Игровой цикл
game_is_on = True
while game_is_on:
    time.sleep(ball.speed)
    screen.update()
    ball.move()
    
    # Столкновение со стенами
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    # Столкновение с ракетками
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320 or 
        ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
    
    # Гол правому игроку
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    
    # Гол левому игроку
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
    
    # Проверка победы
    if scoreboard.l_score == WIN_SCORE:
        game_is_on = False
        scoreboard.game_over("LEFT")
    
    if scoreboard.r_score == WIN_SCORE:
        game_is_on = False
        scoreboard.game_over("RIGHT")

screen.exitonclick()