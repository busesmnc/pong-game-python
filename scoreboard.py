from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_sb()

    def update_sb(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_sb()

    def r_point(self):
        self.r_score += 1
        self.update_sb()

    def game_over(self, winner):
        self.goto(0, 100)
        self.write("GAME OVER", align="center", font=("courier", 30, "normal"))
        self.goto(0, 50)
        self.write(f"THE WINNER IS {winner}", align="center", font=("courier", 30, "normal"))