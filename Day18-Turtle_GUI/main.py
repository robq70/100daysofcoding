#####Turtle Intro######
from turtle import Turtle, Screen
import turtle as t

timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("triangle")
timmy_the_turtle.color("red")
timmy_the_turtle.forward(100)
timmy_the_turtle.backward(200)
timmy_the_turtle.right(90)
timmy_the_turtle.left(180)
timmy_the_turtle.setheading(0)

screen = Screen()
screen.exitonclick()

######## Challenge 1 - Draw a Square ############
