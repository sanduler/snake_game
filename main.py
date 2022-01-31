# Name: Ruben Sanduleac
# Date: January 31st, 2022
# Description: The main goal of the game is to create a fully functional snake game.
import time
from turtle import Turtle, Screen

# create the screen for the game.
import black as black

screen = Screen()
# set up the size for the screen.
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# create a tuple for the position of the three snake objects
start_pos = [(0, 0), (-20, 0), (-40, 0)]

snake = []
# use a for loop to create three snake object and set them to correct position form the start_pos
for position in start_pos:
    new_snake = Turtle("square")
    new_snake.color("White")
    new_snake.penup()
    new_snake.goto(position)
    snake.append(new_snake)

# screen.update()

# TODO: Create animation and key controls on the screen.
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for snk in snake:
        snk.forward(20)

# screen doesn't close automatically
screen.exitonclick()