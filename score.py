from turtle import Turtle

FONTS = ("Arial", 20, "bold")
ALIGNMENT = "center"
SCORE_COLOR = "White"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color(SCORE_COLOR)
        self.setposition(0, 270)
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONTS)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()
