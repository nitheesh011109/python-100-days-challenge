from turtle import Turtle
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,260)
        self.update_score()

    def update_score(self):
        self.write(f"Score : {self.score}", align="center", font=("Courier",22,"bold"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER" , align="center", font=("Courier",22,"bold"))
