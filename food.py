from random import randint
from turtle import Turtle


class Food(Turtle):
    """A class to manage the Food in Snake Game."""

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(0.6, 0.6)
        self.color('yellow')
        self.penup()
        self.create_food()

    def create_food(self):
        """Creates a new Food object at a random location on the screen."""
        self.goto(randint(-280, 280), randint(-280, 280))
