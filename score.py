from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("White")
        self.setposition(-20, 280)
        self.write("Score: ", True, font=("Arial", 16, "bold"))
