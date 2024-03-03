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


tim.speed("fastest")
draws = 96
angle = 360 / draws
for _ in range(draws):
    tim.color(random_color())
    tim.circle(120)
    # tim.setheading(tim.heading()+angle)
    tim.left(angle)

screen = t.Screen()
screen.exitonclick()
