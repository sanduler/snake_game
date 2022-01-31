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


# while the game is on the while loop will continue to work
game_is_on = True

while game_is_on:
    # set the screen to update after the movement has been run
    screen.update()
    # create a small delay
    time.sleep(0.1)
    # for loop that give the ability for the snake to turn.
    # start = -2, stop = 0, step = 1
    # (length = 3 - 1) = start = 2, the stop is located at position 0 and the snake moves one step at time
    for snake_num in range(len(snake)-1, 0, -1):
        # get the new x and y location by looking into the list sub 1
        # by moving the snake block the next position.
        new_x = snake[snake_num - 1].xcor()
        new_y = snake[snake_num - 1].ycor()
        # set the new location of the snake
        snake[snake_num].goto(new_x, new_y)
    # move the snake forward by 20 pixels
    snake[0].forward(20)
    # turn the snake by 20 pixels
    snake[0].right(90)

# screen doesn't close automatically
screen.exitonclick()