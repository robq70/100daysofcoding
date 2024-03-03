import random
import turtle as t

t.colormode(255)
tim = t.Turtle()


def random_color():
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    color = (r, g, b)
    return color


tim.pensize(2)
for sides in range(3, 10):
    tim.color(random_color())
    for _ in range(sides):
        tim.forward(100)
        tim.right(360 / sides)

screen = t.Screen()
screen.exitonclick()
