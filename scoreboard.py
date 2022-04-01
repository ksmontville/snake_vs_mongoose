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
        self.goto(0, 0.45*self.screen.window_height())
        self.score = 0
        self.show_score()

    def show_score(self):
        """Displays the score on the screen."""
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def show_game_over(self):
        """Display 'GAME OVER!' in the center of the screen."""
        self.home()
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)

    def increment_score(self):
        """Clears the current score text, then increments the score by 1."""
        self.clear()
        self.score += 1

    def decrement_score(self):
        """Clears the current score text, then decrements the score by 1. Cannot be less than 0."""
        self.clear()
        if self.score > 0:
            self.score -= 1
        else:
            self.score = 0
