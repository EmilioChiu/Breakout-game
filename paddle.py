from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.setposition(0, -200)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=7, stretch_wid=1)
        self.penup()

    def restart(self):
        self.hideturtle()
        self.setposition(0, -200)
        self.showturtle()

    def move_left(self):
        new_x = self.xcor() - 50
        self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + 50
        self.goto(new_x, self.ycor())


