import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Type turtle will win the race. Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
y_cor = 110
# Second method
# y_cor = [-70, -40, -10, 20, 50, 80]
for turtle_idx in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_idx])
    new_turtle.penup()
    # Second method
    # new_turtle.goto(x=-230, y=y_cor[turtle_idx])
    new_turtle.goto(x=-230, y=y_cor)
    all_turtles.append(new_turtle)
    y_cor -= 40

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
