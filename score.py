from turtle import Turtle

# Determine the font, size and style of the scoreboard
FONTS = ("Arial", 20, "normal")
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
        # high score of game
        self.high_score = 0
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
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONTS)

    # def game_over(self):
    #     """Game over function which is called when the user crashes into the wall
    #     or becomes to long and crashes into itself."""
    #     # set the position to the top of the screen
    #     self.setposition(0, 0)
    #     self.write("Game Over", align=ALIGNMENT, font=FONTS)

    def reset(self):
        """This function is responsible for updating the high score based on the
        on what the user scored in the current game."""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score_data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update()

    def increase_score(self):
        """this function is responsible for incrementing the score
        updating then clearing the previous score"""
        self.score += 1
        self.update()
