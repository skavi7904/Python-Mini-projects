from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Screen Setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)  # Turns off automatic screen updating

# Create paddles, ball, and scoreboard
l_paddle = Paddle((350, 0))  # Left paddle
r_paddle = Paddle((-350, 0))  # Right paddle
ball = Ball()
scoreboard = Scoreboard()

# Keybindings
screen.listen()
screen.onkey(l_paddle.go_up, "Up")  # Left paddle goes up
screen.onkey(l_paddle.go_down, "Down")  # Left paddle goes down
screen.onkey(r_paddle.go_up, "w")  # Right paddle goes up
screen.onkey(r_paddle.go_down, "s")  # Right paddle goes down

# Game loop
game_is_on = True
while game_is_on:
    screen.update()  # Update screen after each move
    ball.move()

    # Detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if (ball.distance(l_paddle) < 50 and ball.xcor() > 320) or \
       (ball.distance(r_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    time.sleep(ball.move_speed)  # Ball speed gradually increases

screen.exitonclick()
