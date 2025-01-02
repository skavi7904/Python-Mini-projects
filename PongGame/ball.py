from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 0.1  # Starting speed

    def move(self):
        new_x = self.xcor() + self.x_move * 2
        new_y = self.ycor() + self.y_move * 2
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.increase_speed()  # Increase speed when ball bounces

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1  # Reset speed
        self.bounce_x()

    def increase_speed(self):
        self.move_speed *= 0.5  # Gradually increase speed as the ball bounces
