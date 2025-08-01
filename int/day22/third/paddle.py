from turtle import Turtle
from settings import *

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color(PADDLE_COLOR)
        self.shape(PADDLE_SHAPE)
        self.shapesize(stretch_len=PADDLE_STRETCH_LEN, 
                      stretch_wid=PADDLE_STRETCH_WID)
        self.penup()
        self.goto(position)
    
    def go_up(self):
        """Движение ракетки вверх с ограничением"""
        if self.ycor() < PADDLE_LIMIT:
            new_y = self.ycor() + PADDLE_SPEED
            self.goto(self.xcor(), new_y)
    
    def go_down(self):
        """Движение ракетки вниз с ограничением"""
        if self.ycor() > -PADDLE_LIMIT:
            new_y = self.ycor() - PADDLE_SPEED
            self.goto(self.xcor(), new_y)