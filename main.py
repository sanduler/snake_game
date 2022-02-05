# Name: Ruben Sanduleac
# Date: January 31st, 2022
# Description: The main goal of the game is to create a fully functional snake game.
import time
from turtle import Screen

import segment as segment

from food import Food
from score import Scoreboard
from snake import Snake

COLLISION_DISTANCE = 15

# create the screen for the game.
screen = Screen()
# set up the size for the screen.
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# create a snake object from Snake class
snake = Snake()
# create a food object on a main screen
food = Food()
# create the scoreboard to be displayed on top of the screen.
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# while the game is on the while loop will continue to work
game_is_on = True

while game_is_on:
    # set the screen to update after the movement has been run
    screen.update()
    # create a small delay
    time.sleep(0.09)
    snake.movement()

    # detect collisions with Food
    # if the snake head (first turtle) is less than 15 pixels
    # away from the food then
    if snake.head.distance(food) < COLLISION_DISTANCE:
        # function call to randomly assign the food location on the window
        food.new_location()
        snake.extend()
        # increase the score after the snake head collides with the food
        scoreboard.increase_score()

    # detect collisions with head if borders are hit then the loop breaks and the game is over
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # break the loop and end the game
        # game_is_on = False
        # call the game_over function from score.py to prompt the game_over prompt
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset_snake()
        food.new_location()

    # for loop to loop through all the parts that were added as the results of the game
    for segment in snake.snake_segment[1:]:
        # if the snake head is in the proximity of less than 10 pixels then set the game to been
        # over and print the game is over.
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            # call the message that the game is over.
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset_snake()
            food.new_location()
# screen doesn't close automatically
screen.exitonclick()