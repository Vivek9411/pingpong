from turtle import Turtle


class Pedal(Turtle):

    def __init__(self, xcor):
        super().__init__()
        self.x_coordinate = xcor
        self.penup()
        self.shape("square")
        self.color('white')
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setx(self.x_coordinate)





    def move_up(self):
        if self.ycor() <= 230:
            self.fd(30)
        else:
            pass

    def move_down(self):
        if self.ycor() >= -230:
            self.bk(30)


