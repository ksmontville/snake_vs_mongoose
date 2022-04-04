from turtle import Turtle

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
        self.high_score = 0
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
        self.score = 0
        self._show_score()

    # def show_game_over(self):
    #     """Display 'GAME OVER!' in the center of the screen."""
    #     self.home()
    #     self.write("GAME OVER!", align=ALIGNMENT, font=FONT)

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
