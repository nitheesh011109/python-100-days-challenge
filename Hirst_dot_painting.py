import turtle
import colorgram
from turtle import Turtle , Screen
import random
turtle.colormode(255)
tim = Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
rgb_color = []
colors = colorgram.extract('Hirst_dots.jpg',10000)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_color.append((r,g,b))
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
for dot_count in range(1 , number_of_dots + 1):
    dot_color = random.choice(rgb_color)
    tim.dot(20 , dot_color)
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = Screen()
screen.exitonclick()
