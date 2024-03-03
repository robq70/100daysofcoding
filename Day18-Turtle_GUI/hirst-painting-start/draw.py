# import package and making object
import turtle as t
import random

t.colormode(255)

tim = t.Turtle()
tim.speed("fastest")
# hide lines
tim.penup()
# hide the turtle
tim.hideturtle()
tim.setheading(145)
tim.forward(300)
tim.setheading(0)
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40),
              (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71),
              (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74),
              (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97),
              (176, 192, 209)]


# method to draw square with dots
# space --> distance between dots
# x	 --> side of square
def draw(space, x):
    for _ in range(x):
        for _ in range(x):
            # dot
            tim.dot(20, random.choice(color_list))

            # distance for another dot
            tim.forward(space)
        tim.backward(space * x)

        # direction
        tim.right(90)
        tim.forward(space)
        tim.left(90)

    # Main Section


tim.penup()
draw(50, 10)

screen = t.Screen()
screen.exitonclick()
