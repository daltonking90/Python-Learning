from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()  # super references the classes inheritance param
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("purple")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-440, 440)
        random_y = random.randint(-340, 340)
        self.goto(random_x, random_y)
