from turtle import Turtle

MOVE_DISTANCE = 20
TOP_LIMIT = 250
BOTTOM_LIMIT = -250

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def go_up(self):
        if self.ycor() < TOP_LIMIT:
            self.sety(self.ycor() + MOVE_DISTANCE)

    def go_down(self):
        if self.ycor() > BOTTOM_LIMIT:
            self.sety(self.ycor() - MOVE_DISTANCE)
