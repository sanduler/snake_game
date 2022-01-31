from turtle import Turtle


START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIS = 20

# direction
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Create a three segment snake and all the functionality"""
    def __init__(self):
        """Function prototype uses to create a blank list and intilize the creation of the snake"""
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        """create_snake uses a for loop to create three snake object
        and set them to correct position form the start_pos"""
        for position in START_POS:
            new_snake = Turtle("square")
            new_snake.color("White")
            new_snake.penup()
            new_snake.goto(position)
            self.snake.append(new_snake)

    def movement(self):
        """movement function uses a for loop that gives
        the ability for the snake to turn. Start = -2, stop = 0,
        step = 1 (length = 3 - 1) = start = 2, the stop is
        located at position 0 and the snake moves one step at time"""
        for snake_num in range(len(self.snake) - 1, 0, -1):
            # get the new x and y location by looking into the list sub 1
            # by moving the snake block the next position.
            new_x = self.snake[snake_num - 1].xcor()
            new_y = self.snake[snake_num - 1].ycor()
            # set the new location of the snake
            self.snake[snake_num].goto(new_x, new_y)
        # move the snake forward by 20 pixels
        self.head.forward(MOVE_DIS)
        # turn the snake by 20 pixels
        # self.snake[0].right(90)

    def up(self):
        """Set the direction of the snake to UP and check so
        the snake can't go back DOWN
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Set the direction of the snake to DOWN and check so
        the snake can't go back UP
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Set the direction of the snake to LEFT and check so
        the snake can't go back RIGHT
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Set the direction of the snake to RIGHT and check so
        the snake can't go back LEFT
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


