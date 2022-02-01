# Name: Ruben Sanduleac
# Date: January 31st, 2022
# Description: The main goal of the game is to create a fully functional snake game.
import time
from turtle import Screen
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
    time.sleep(0.1)
    snake.movement()

    # detect collisions with Food
    # if the snake head (first turtle) is less than 15 pixels
    # away from the food then
    if snake.head.distance(food) < COLLISION_DISTANCE:
        food.new_location()
        scoreboard.increase_score()
# screen doesn't close automatically
screen.exitonclick()