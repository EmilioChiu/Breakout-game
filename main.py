from turtle import Screen
from ball import Ball
from paddle import Paddle
from block import Blocks
from score import Scoreboard

screen = Screen()
screen.screensize(canvheight=500, canvwidth=600)
screen.bgcolor("black")
screen.title("break-out")

# object call
ball = Ball()
paddle = Paddle()
blocks = Blocks()
scoreboard = Scoreboard()

# events
screen.listen()
screen.onkey(paddle.move_left, "a")
screen.onkey(paddle.move_right, "d")

# game
game = True
while game:
    ball.move()
    # wall clash
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.x_bounce()
    if ball.ycor() > 250:
        ball.y_bounce()

    # paddle clash
    if ball.ycor() < -180 and paddle.distance(ball) < 70:
        ball.y_bounce()
    elif ball.ycor() < -260:
        scoreboard.lost_live()
        paddle.restart()
        ball.restart()
        if scoreboard.lives == 0:
            scoreboard.game_over()
            game = False

    # clash block
    for n in blocks.all_blocks:
        if n.distance(ball.xcor() + 30, ball.ycor()) <= 15 or n.distance(ball.xcor() - 30, ball.ycor()) <= 15:
            scoreboard.add_score()
            ball.x_bounce()
            blocks.all_blocks.remove(n)
            n.hideturtle()
        elif n.distance(ball.xcor() + 20, ball.ycor()) < 24 or n.distance(ball.xcor() - 20, ball.ycor()) < 24:
            scoreboard.add_score()
            ball.y_bounce()
            blocks.all_blocks.remove(n)
            n.hideturtle()

        # new level
        if len(blocks.all_blocks) == 0:
            scoreboard.level_up()
            blocks.spawn()
            ball.restart()
            paddle.restart()



















screen.exitonclick()
