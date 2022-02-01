from turtle import Turtle

# Determine the font, size and style of the scoreboard
FONTS = ("Arial", 20, "bold")
# Alignment of the scoreboard on the screen
ALIGNMENT = "center"
# Color of the scoreboard
SCORE_COLOR = "White"


class Scoreboard(Turtle):
    """Scoreboard class that inherits the Turtle class
    The class is responsible for displaying the Score"""
    def __init__(self):
        super().__init__()
        # start the score at 0
        self.score = 0
        # lift up the pen so it wont draw
        self.penup()
        # set the color to white
        self.color(SCORE_COLOR)
        # set the position to the top of the screen
        self.setposition(0, 270)
        # hide the turtle as we want to display only the score
        self.hideturtle()
        # update function call
        self.update()

    def update(self):
        """this function is responsible for printing the score
        and aligning and font"""
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONTS)

    def increase_score(self):
        """this function is responsible for incrementing the score
        updating then clearing the previous score"""
        self.score += 1
        self.clear()
        self.update()
