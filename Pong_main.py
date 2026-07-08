from turtle import Screen
from Pong_ball import Ball
from Pong_paddle import Paddle
from Pong_scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

right_up = False
right_down = False
left_up = False
left_down = False

def r_up_press():
    global right_up
    right_up = True

def r_up_release():
    global right_up
    right_up = False

def r_down_press():
    global right_down
    right_down = True

def r_down_release():
    global right_down
    right_down = False


def l_up_press():
    global left_up
    left_up = True

def l_up_release():
    global left_up
    left_up = False

def l_down_press():
    global left_down
    left_down = True

def l_down_release():
    global left_down
    left_down = False
screen.listen()
#r_paddle
screen.onkeypress(r_up_press, "Up")
screen.onkeyrelease(r_up_release, "Up")
screen.onkeypress(r_down_press, "Down")
screen.onkeyrelease(r_down_release, "Down")
#l_paddle
screen.onkeypress(l_up_press, "w")
screen.onkeyrelease(l_up_release, "w")
screen.onkeypress(l_down_press, "s")
screen.onkeyrelease(l_down_release, "s")

game_on = True

while game_on:
    time.sleep(ball.move_speed)
    if right_up:
        r_paddle.go_up()
    if right_down:
        r_paddle.go_down()

    if left_up:
        l_paddle.go_up()
    if left_down:
        l_paddle.go_down()
        
    ball.move()
    
    # Wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Right paddle collision
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        scoreboard.r_score_point()
    # Left paddle collision
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        scoreboard.l_score_point()
        
    # Right player missed
    if ball.xcor() > 380:
        scoreboard.l_score_point()
        ball.reset_position()
    # Left player missed
    if ball.xcor() > 380:
        scoreboard.r_score_point()
        ball.reset_position()

    screen.update()
screen.exitonclick()
