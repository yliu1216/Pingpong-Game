from turtle import Turtle
ALIGNMENT="center"
FONT=("Arial", 21, "normal")


class ScoreBored(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score1 = 0
        self.score2 = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f" {self.score1} ", align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(f" {self.score2} ", align=ALIGNMENT, font=FONT)

    def l_increase_score(self):
        self.score1 += 1
        self.update_scoreboard()

    def r_increase_score(self):
        self.score2 += 1
        self.update_scoreboard()