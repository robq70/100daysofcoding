from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 80, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.update_scoreboard()
        self.screen_line()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(f"{self.r_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_l_score(self):
        self.l_score += 1
        self.update_scoreboard()

    def increase_r_score(self):
        self.r_score += 1
        self.update_scoreboard()

    def screen_line(self):
        self.penup()
        self.goto(0, -300)
        self.pendown()
        self.color('white')
        self.setheading(90)
        self.pensize(5)
        for _ in range(15):
            self.forward(20)
            self.penup()
            self.forward(20)
            self.pendown()
