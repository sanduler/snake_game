# Name: Ruben Sanduleac
# Date: January 31st, 2022
# Description: The main goal of the game is to create a fully functional snake game.
import time
from turtle import Turtle, Screen
from snake import Snake

# create the screen for the game.
import black as black

screen = Screen()
# set up the size for the screen.
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# create a snake object from Snake class
snake = Snake()

# while the game is on the while loop will continue to work
game_is_on = True

while game_is_on:
    # set the screen to update after the movement has been run
    screen.update()
    # create a small delay
    time.sleep(0.1)
    snake.movement()


# screen doesn't close automatically
screen.exitonclick()