import turtle
from turtle import Turtle, Screen
import pandas
import random

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


def get_mouse_click_cor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_cor)
turtle.mainloop()

# user_choice = screen.textinput("Enter state:", "Enter a state: ")
# states = pandas.read_csv("us_states-game.csv")
# data_states = states.to_dict()

screen.exitonclick()
