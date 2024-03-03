import turtle as t
import random

t.colormode(255)
tim = t.Turtle()


def random_color():
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    color = (r, g, b)
    return color


direction = [0, 90, 180, 270]
tim.speed("fastest")

for _ in range(50):
    tim.pensize(7)
    tim.forward(30)
    tim.color(random_color())
    tim.setheading(random.choice(direction))

screen = t.Screen()
screen.exitonclick()
