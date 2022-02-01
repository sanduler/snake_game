from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        # inherit the turtle class
        super().__init__()
        # change the shape of the turtle to a circle
        self.shape("circle")
        # pick up the pen so the circle does not draw
        self.penup()
        # shrinks the circle to the size of a dot
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        # change the color of the turtle
        self.color("red")
        # set speed to fastest
        self.speed("fastest")
        # generate a random point on x and y-axis
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        # move the Food to the random point
        self.goto(rand_x, rand_y)

