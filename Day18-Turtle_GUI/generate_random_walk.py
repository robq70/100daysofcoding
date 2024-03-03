import turtle as t
import random

tim = t.Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]

direction = [0, 90, 180, 270]
tim.speed("fastest")

for _ in range(50):
    tim.pensize(7)
    tim.forward(30)
    tim.color(random.choice(colours))
    tim.setheading(random.choice(direction))

screen = t.Screen()
screen.exitonclick()
