from turtle import Turtle

FILENAME = r'c:\users\montv\python_work\100_days_of_code\snake_vs_mongoose\high_score'
ALIGNMENT = 'center'
FONT = ('Courier', 16, 'bold')


class Scoreboard(Turtle):
    """A class to manage the scoreboard in Snake Game."""
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.screen = self.getscreen()
        self.goto(0, 0.44*self.screen.window_height())
        self.high_score = self._get_high_score()
        self.score = 0
        self._show_score()

    def _show_score(self):
        """Clears the current scoreboard, then displays the score on the screen."""
        self.clear()
        self.write(f'Current score: {self.score}\nHighest score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def reset(self):
        """"""
        if self.score > self.high_score:
            self.high_score = self.score
            self._record_high_score()
        self.score = 0
        self._show_score()

    def increment_score(self):
        """Increments the score by 1."""
        self.score += 1
        self._show_score()

    def decrement_score(self):
        """Decrements the score by 1. Cannot be less than 0."""
        if self.score > 0:
            self.score -= 1
        else:
            self.score = 0
        self._show_score()

    def _record_high_score(self):
        """Write the all-time high score to a file."""
        with open(FILENAME, 'w') as f:
            f.write(f"{self.score}")

    def _get_high_score(self):
        """Read the all-time high score from a file."""
        with open(FILENAME) as f:
            return int(f.read())
