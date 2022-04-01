from turtle import Turtle

STARTING_SEGMENTS = 3
INCREMENT_SEGMENTS = 1
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """A class to manage the behavior of the snake in Snake Game."""

    def __init__(self):
        """Initialize the attributes of the snake."""
        self.segments = []
        self.create_segment(STARTING_SEGMENTS)
        self.head = self.segments[0]
        self.tail = self.segments[1:]
        self.screen = self.head.getscreen()
        self.directions = {
            'Up': self.up,
            'Down': self.down,
            'Left': self.left,
            'Right': self.right
            }

    def create_segment(self, number_of_segments):
        """Creates a snake of length three."""
        for i in range(number_of_segments):
            segment = Turtle(shape='square')
            segment.color('green')
            segment.penup()

            if number_of_segments == STARTING_SEGMENTS:
                segment.setx(-MOVE_DISTANCE * i)
            else:
                segment.setpos(self.segments[-1].pos())

            self.segments.append(segment)

    def forward(self):
        """Moves the snake forward."""
        i = len(self.segments) - 1
        while i >= 1:
            self.segments[i].setpos(self.segments[i - 1].pos())
            i -= 1
        self.head.forward(MOVE_DISTANCE)

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

    def detect_collision(self):
        """Detects snake head collision with wall or with tail."""
        game_screen_width = self.screen.window_width()
        game_screen_height = self.screen.window_height()
        if abs(self.head.xcor()) > 0.5*game_screen_width or abs(self.head.ycor()) > 0.5*game_screen_height:
            return True

        for segment in self.segments[1:]:
            if self.head.distance(segment) < 5:
                return True
