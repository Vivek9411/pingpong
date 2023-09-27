import time
from turtle import Screen
from pedals import Pedal
from ball import Ball
from boundariesandscore import Boundary, Score
import boundariesandscore

screen = Screen()
screen.title("ping Pong")

screen.screensize(canvwidth=800, canvheight=600, bg='black')
boundary = Boundary()
boundary.make_boundary()

screen.tracer(0)
score_left = Score(boundariesandscore.LEFT)
score_right = Score(boundariesandscore.RIGHT)

left_pedal = Pedal(-350)
right_pedal = Pedal(350)

ball = Ball()
screen.update()
screen.listen()
screen.onkeypress(key="Up", fun=right_pedal.move_up)
screen.onkeypress(key='Down', fun=right_pedal.move_down)
screen.onkeypress(key='w', fun=left_pedal.move_up)
screen.onkeypress(key='s', fun=left_pedal.move_down)


points_left = 0
points_right = 0
game_on = True
speed = 0.05
screen.update()
ball.setangel()
while max(points_right, points_left) < 5:
    screen.update()
    time.sleep(speed)
    ball.move()
    ball.bounce()
    if ball.xcor() > 320:
        if abs(ball.ycor() - right_pedal.ycor()) < 51:
            ball.bouncex()
            if speed > 0.02:
                speed -= 0.004

        elif ball.xcor() > 350:
            ball.fd(20)
            score_right.update_score()
            points_right += 1
            ball.clear()
            ball.goto(0, 0)
            speed = 0.05

    if ball.xcor() < -320:
        if abs(ball.ycor() - left_pedal.ycor()) < 51:
            ball.bouncex()
            if speed > 0.02:
                speed -= 0.002
        elif ball.xcor() < -350:
            ball.fd(20)
            score_left.update_score()
            points_left += 1
            ball.clear()
            ball.goto(0, 10)
            ball.setangel()
            speed = 0.05

if points_right == 5:
    score_left.end_score(1)
else:
    score_right.end_score(2)

screen.update()
screen.exitonclick()
