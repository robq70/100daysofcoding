import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("us_states-game.csv")
data_dict = data.to_dict()
numbers_states = len(data_dict["state"])
score = 0
guess_list = []

game_is_on = True
while len(guess_list) < 50:
    answer_state = screen.textinput(f"{score}/{numbers_states} States Correct", "What's another state's name: ").title()
    if answer_state == "Exit":
        break
    for _ in range(0, numbers_states - 1):
        if data_dict["state"][_] == answer_state:
            if answer_state in guess_list:
                game_is_on = True
            else:
                score += 1
                name = data_dict["state"][_]
                x_cor = data_dict["x"][_]
                y_cor = data_dict["y"][_]
                name_of_state = turtle.Turtle()
                name_of_state.hideturtle()
                name_of_state.penup()
                name_of_state.goto(x=x_cor, y=y_cor)
                name_of_state.write(name, align="center")
                guess_list.append(name)
                print(guess_list)
screen.exitonclick()
