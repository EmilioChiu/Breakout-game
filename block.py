from turtle import Turtle


class Blocks:
    def __init__(self):
        self.all_blocks = []
        self.spawn()

    def spawn(self):
        x_initial = -240
        y_initial = 130
        for n in range(24):
            new_block = Turtle()
            new_block.hideturtle()
            new_block.penup()
            new_block.shape("square")
            new_block.color("white")
            new_block.shapesize(stretch_len=3, stretch_wid=1)
            self.all_blocks.append(new_block)
            new_block.goto(x_initial, y_initial)
            new_block.showturtle()
            if (n + 1) % 8 == 0:
                x_initial = -240
                y_initial -= 25
            else:
                x_initial += 65

    def destroyed(self, ball):
        for n in self.all_blocks:
            if ball.distance(n) < 60:
                self.all_blocks.remove(n)


