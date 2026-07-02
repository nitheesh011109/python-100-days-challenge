from turtle import Turtle , Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=600,height=500)
user_bet = screen.textinput(title = "Make your bet" , prompt = "Which turtle will win the race? Enter a color:")
colors = ["red","orange","yellow","green","blue"]
y_positions = [-100 , -50 , 0 , 50 , 100]
all_turtles = []

for turtle_index in range(len(colors)):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[turtle_index])
    turtle.penup()
    turtle.goto(x=-250 , y=y_positions[turtle_index])
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color.lower() == user_bet.lower():
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
        rand_distance = random.randint(0 , 20)
        turtle.forward(rand_distance)

screen.exitonclick()
