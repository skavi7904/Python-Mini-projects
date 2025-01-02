from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


def restart_game():
    global snake, food, scoreboard, game_is_on
    screen.clear()  # Clear the screen for a fresh start
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

    # Reinitialize the objects
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    # Rebind the controls
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    # Start the game loop again
    game_loop()


def game_loop():
    global game_is_on
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food.
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Detect collision with wall.
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_is_on = False
            scoreboard.reset()
            scoreboard.game_over()
            screen.onkey(restart_game, "Return")  # Bind "Enter" to restart

        # Detect collision with tail.
        for segment in snake.segments:
            if segment == snake.head:
                pass
            elif snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.reset()
                scoreboard.game_over()
                screen.onkey(restart_game, "Return")  # Bind "Enter" to restart


# Initial setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_loop()

screen.exitonclick()
