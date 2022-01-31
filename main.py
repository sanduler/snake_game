# Name: Ruben Sanduleac
# Date: January 31st, 2022
# Description: The main goal of the game is to create a fully functional snake game.

from turtle import Turtle, Screen

# create the screen for the game.
import black as black

screen = Screen()
# set up the size for the screen.
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

snake = Turtle("square")
snake.color("White")

# create a tuple for the position of the three snake objects
start_pos = [(0, 0), (-20, 0), (-40, 0)]

# use a for loop to create three snake object and set them to correct position form the start_pos
for position in start_pos:
    snake = Turtle("square")
    snake.color("White")
    snake.goto(position)




# screen doesn't close automatically
screen.exitonclick()