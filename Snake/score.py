from turtle import Turtle
from food import Food

ALIGNMENT = "center"
FONT = ("Arial", 26, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()  # super references the classes inheritance param
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 300)
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", align=ALIGNMENT, font=FONT)
