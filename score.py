from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.lives = 3
        self.level = 1
        self.score_and_lives()

    def add_score(self):
        self.score += 10
        self.score_and_lives()

    def lost_live(self):
        self.lives -= 1
        self.score_and_lives()

    def level_up(self):
        self.level += 1
        self.score_and_lives()

    def score_and_lives(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setposition(-280, 200)
        self.write(f"LEVEL: {self.level} \nSCORE: {self.score} \nLIVES: {self.lives}", align="left", font=("arial", 14, "normal"))

    def game_over(self):
        try:
            with open("high score.txt") as high_score:
                high_score = high_score.readlines()
                high_score = int(high_score[0])
        except FileNotFoundError:
            high_score = 0
        if self.score > high_score:
            with open("high score.txt", mode="w") as high_score:
                high_score.write(f"{self.score}")
            high_score = self.score

        self.home()
        self.write(f"YOUR FINAL SCORE: {self.score} \nHIGH SCORE: {high_score}", align="center", font=("arial", 14, "normal"))
