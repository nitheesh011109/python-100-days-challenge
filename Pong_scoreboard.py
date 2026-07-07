from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.r_score = 0
        self.l_score = 0
        self.nothing = ":"
        self.goto(0, 210)
        self.write(self.nothing, align="center", font=("Arial", 40, "normal"))
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-50, 200)
        self.write(self.l_score, align="center", font=("Arial", 50, "normal"))
        self.goto(50, 200)
        self.write(self.r_score, align="center", font=("Arial", 50, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
