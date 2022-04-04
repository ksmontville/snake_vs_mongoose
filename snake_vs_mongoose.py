import time
from snake import Snake
from mongoose import Mongoose
from food import Food
from scoreboard import Scoreboard
from turtle import Screen, textinput


def refresh():
    screen.listen()
    screen.update()
    time.sleep(.1)


def play_again():
    """Prompts the user to play the game again, or to exit the program."""
    prompt = textinput(
        title="Game over!",
        prompt="Type 'c' to continue and play again, or any other character to exit.")
    if prompt.lower() == 'c':
        return True
    else:
        return False


def reset_game():
    """Resets the game to its initial state."""
    snake.reset()
    mongoose.reset()
    scoreboard.reset()


screen = Screen()
screen.cv._rootwindow.resizable(False, False)
screen.setup(width=800, height=800)
screen.tracer(0)
screen.bgcolor('black')
screen.title('Snake vs. Mongoose')

players = textinput(prompt="Select number of players:\n\nSingle\nMulti", title="Player Select")

snake = Snake()
mongoose = Mongoose()
food = Food()
scoreboard = Scoreboard()

for keystroke, direction in snake.directions.items():
    screen.onkey(key=keystroke, fun=direction)

if players.lower() == 'multi':
    for keystroke, direction in mongoose.directions.items():
        screen.onkey(key=keystroke, fun=direction)

game_on = True
while game_on:
    refresh()
    snake.forward()

    if snake.detect_collision():
        if play_again():
            reset_game()
        else:
            screen.bye()
            break

    if snake.head.distance(food) <= 15:
        scoreboard.increment_score()
        snake.create_segment(1)
        food.create_food()

    mongoose.forward()
    mongoose.detect_collision()
    if players.lower() == 'single':
        mongoose.change_direction()

    if mongoose.head.distance(food) <= 15:
        scoreboard.decrement_score()
        food.create_food()

    for mongoose_segment in mongoose.segments:
        for snake_segment in snake.segments:
            if mongoose_segment.distance(snake_segment) < 15:
                if play_again():
                    reset_game()
                else:
                    screen.bye()
                    break
