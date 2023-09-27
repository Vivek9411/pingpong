from turtle import Turtle
from random import choice
STARTING_ANGEL = [45, 60, -45, -60]



class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.create_ball()

    def create_ball(self):
        self.penup()
        self.shape('circle')
        self.color('white')
        self.setangel()


    def move(self):
        self.fd(10)



    def bounce(self):
        y = self.ycor()
        if y >= 290 or y <= -290:
            angel = self.heading()
            self.setheading(-angel)


    def bouncex(self):
        angel = self.heading()
        self.setheading(180 - angel)
        self.fd(20)


    def setangel(self):
        self.setheading(choice(STARTING_ANGEL))
