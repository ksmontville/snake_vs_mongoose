from random import choice
from turtle import Turtle, Screen

STARTING_SEGMENTS = 6
INCREMENT_SEGMENTS = 1
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Mongoose:
    """A class to manage the computer controlled mongoose in Snake vs. Mongoose"""
    def __init__(self):
        """Initialize the attributes of the snake."""
        self.segments = []
        self.create_segment(STARTING_SEGMENTS)
        self.head = self.segments[0]
        self.head_shape = self.head.shape('triangle')
        self.tail = self.segments[1:]
        self.screen = self.head.getscreen()
        self.directions = {
            'w': self.up,
            's': self.down,
            'a': self.left,
            'd': self.right
        }

    def create_segment(self, number_of_segments):
        """Creates a snake of length three."""
        for i in range(number_of_segments):
            segment = Turtle(shape='circle')
            segment.color('sienna')
            segment.penup()

            if number_of_segments == STARTING_SEGMENTS:
                segment.sety(200)
                segment.setx(-20 * i)
            else:
                segment.setpos(self.segments[-1].pos())
            self.segments.append(segment)

    def reset(self):
        """
        Sends the active mongoose to the graveyard.
        Creates new mongoose at its initial configuration at the center of the screen.
        """
        graveyard = (0.60 * self.screen.window_width(), 0.60 * self.screen.window_height())

        for segment in self.segments:
            segment.setpos(graveyard)
        self.segments.clear()
        self.create_segment(STARTING_SEGMENTS)
        self.head = self.segments[0]
        self.head_shape = self.head.shape('triangle')

    def forward(self):
        """Moves the snake forward."""
        i = len(self.segments) - 1
        while i >= 1:
            self.segments[i].setpos(self.segments[i - 1].pos())
            i -= 1
        self.head.forward(MOVE_DISTANCE)

    def change_direction(self):
        """Randomly chooses the mongoose's heading from cardinal directions."""
        roll = choice(range(100))
        if roll % 20 == 0:
            self.head.setheading(choice([UP, DOWN, LEFT, RIGHT]))

    def detect_collision(self):
        """Detects mongoose collision with wall and reverses direction."""
        game_screen_width = self.screen.window_width()
        game_screen_height = self.screen.window_height()
        if self.head.xcor() >= 0.45 * game_screen_width:
            self.head.setheading(LEFT)
        elif self.head.xcor() <= -0.45 * game_screen_width:
            self.head.setheading(RIGHT)
        elif self.head.ycor() >= 0.45 * game_screen_height:
            self.head.setheading(DOWN)
        elif self.head.ycor() <= -0.45 * game_screen_height:
            self.head.setheading(UP)

    def up(self):
        """Sets the heading of the snake to 90."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Sets the heading of the snake to 270"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Sets the heading of the snake to 180"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Sets the heading of the snake to 0."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)