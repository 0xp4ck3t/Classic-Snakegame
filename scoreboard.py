from turtle import Turtle
font = ("Courier", 15, "bold")
new_font = ("Courier", 50, "bold")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.clear()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 275)
        self.write(f"Score: {self.score}", align="center", font=font)

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=font)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!", align="center", font=new_font)
