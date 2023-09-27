from turtle import Turtle
LEFT = -130
RIGHT = 130
ALIGN = 'center'
SIZE = 15
FONT = ("Verdana", SIZE, "normal")


class Boundary (Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(5)
        self.hideturtle()
        self.goto(-370, 300)
        self.pendown()
        self.color('red')
        self.width(2)
        self.make_boundary()


    def make_boundary(self):
        for i in range(4):
            if i % 2 == 0:
                self.color('green')
                self.fd(740)
            else:
                self.color('blue')
                self.fd(600)
            self.right(90)
        self.penup()
        self.fd(370)
        self.right(90)


        self.color('red')
        for i in range(30):
            if i % 2 == 0:
                self.pendown()
                self.fd(20)
            else:
                self.penup()
                self.fd(20)


class Score(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.hideturtle()
        self.position = pos
        self.penup()
        self.goto(self.position, 320)
        self.score = 0
        self.color('white')
        self.tell_score()

    def tell_score(self):
        self.write(arg=f"{self.score}", align=ALIGN, font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"{self.score}", align=ALIGN, font=FONT)

    def end_score(self, user):
        global SIZE
        self.goto(0, 20)
        SIZE += 50
        self.color('yellow')
        self.write(arg=f"user {user} won", align=ALIGN, font=FONT)
