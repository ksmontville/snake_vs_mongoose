import time
from snake import Snake
from mongoose import Mongoose
from food import Food
from scoreboard import Scoreboard
from turtle import Screen, textinput

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


screen.listen()
for keystroke, direction in snake.directions.items():
    screen.onkey(key=keystroke, fun=direction)

if players.lower() == 'multi':
    for keystroke, direction in mongoose.directions.items():
        screen.onkey(key=keystroke, fun=direction)

game_on = True
while game_on:
    screen.update()
    time.sleep(.1)

    snake.forward()
    if snake.detect_collision():
        scoreboard.show_game_over()
        game_on = False
        break

    if snake.head.distance(food) <= 15:
        scoreboard.increment_score()
        scoreboard.show_score()
        snake.create_segment(1)
        food.create_food()

    mongoose.forward()
    mongoose.detect_collision()
    if players.lower() == 'single':
        mongoose.change_direction()

    if mongoose.head.distance(food) <= 15:
        scoreboard.decrement_score()
        scoreboard.show_score()
        food.create_food()

    for mongoose_segment in mongoose.segments:
        for snake_segment in snake.segments:
            if mongoose_segment.distance(snake_segment) < 15:
                scoreboard.show_game_over()
                game_on = False
                break

screen.exitonclick()
