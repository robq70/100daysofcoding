from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        # Create paddles
        self.color('white')
        self.shape('circle')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        # Jeśli koordynaty y są dodatnie lub ujemne to poprzez ich przemnożenie przez -1 uzyskamy odwrotność i zmianę kierunku po odbiciu od górnej lub dolnej ścianki
        self.y_move *= -1

    def bounce_x(self):
        # Jeśli koordynaty x są dodatnie lub ujemne to poprzez ich przemnożenie przez -1 uzyskamy odwrotność i zmianę kierunku po odbiciu od paletki
        self.x_move *= -1
        self.move_speed *= 0.2

    def reset_position(self):
        # Po kolizji ze ścianą kulka przenosi się do początkowej pozycji
        self.home()
        # resetujemy prędkość piłki
        self.move_speed = 0.1
        # Po dodatkowo rozpoczyna drugi zawodnik
        self.bounce_x()
