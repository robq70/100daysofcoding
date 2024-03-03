from turtle import Turtle, Screen

tim = Turtle()
for _ in range(15):
    tim.forward(10)
    tim.color("white")
    tim.forward(10)
    tim.color("black")

""" Second way
tim = Turtle()
for _ in range(15):
    tim.forward(10)
    tim.penup(10)
    tim.forward(10)
    tim.pendown(10)
"""


screen = Screen()
screen.exitonclick()
