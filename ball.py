from turtle import Turtle
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.setposition(0, -180)
        self.x = 10
        self.y = 10
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed_ball = 0.1

    def move(self):
        time.sleep(self.speed_ball)
        new_y = self.ycor() + self.y
        new_x = self.xcor() + self.x
        self.goto(new_x, new_y)

    def restart(self):
        self.hideturtle()
        self.y_bounce()
        self.setposition(0, -180)
        self.showturtle()

    def y_bounce(self):
        self.y *= - 1

    def x_bounce(self):
        self.x *= -1



