from turtle import Turtle
from settings import *

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(SCORE_POSITION)
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
    
    def update_scoreboard(self):
        """Обновление счета на экране"""
        self.clear()
        self.write(f"{self.l_score} | {self.r_score}", 
                  align=ALIGNMENT, font=SCORE_FONT)
    
    def l_point(self):
        """Гол левому игроку"""
        self.l_score += 1
        self.update_scoreboard()
    
    def r_point(self):
        """Гол правому игроку"""
        self.r_score += 1
        self.update_scoreboard()
    
    def game_over(self, winner):
        """Сообщение о победе"""
        self.goto(GAME_OVER_POSITION)
        self.write(f"{winner} PLAYER WINS!", 
                  align=ALIGNMENT, font=GAME_OVER_FONT)