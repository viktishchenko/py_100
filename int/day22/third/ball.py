from turtle import Turtle
from settings import *
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color(BALL_COLOR)
        self.shape(BALL_SHAPE)
        self.penup()
        self.speed = BALL_SPEED
        self.x_move = BALL_X_MOVE
        self.y_move = random.choice([-BALL_Y_MOVE, BALL_Y_MOVE])
        
    def move(self):
        """Движение мяча"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def bounce_y(self):
        """Отскок от верхней/нижней стенки"""
        self.y_move *= -1
    
    def bounce_x(self):
        """Отскок от ракетки с ускорением"""
        self.x_move *= -1
        self.speed *= BALL_SPEED_INCREMENT
    
    def reset_position(self):
        """Сброс позиции после гола"""
        self.goto(0, 0)
        self.bounce_x()
        self.speed = BALL_SPEED
        self.y_move = random.choice([-BALL_Y_MOVE, BALL_Y_MOVE])