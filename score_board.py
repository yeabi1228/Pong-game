from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.score_update()
    def score_update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Arial", 25, "bold"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Arial", 25, "bold"))

    def right_score_counter(self):
        self.r_score += 1
        self.score_update()

    def left_score_counter(self):
        self.l_score += 1
        self.score_update()
