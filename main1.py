from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import time
screen=Screen()
screen.setup(width=800,height=600)

screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# right paddle and left paddle

r_paddle=Paddle((350, 0))
l_paddle=Paddle((-350, 0))

# ball object and score object

ball=Ball()
score=ScoreBoard()

#listening to the keys

screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")

#Running Game

game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #bouncing the ball back if it hits the wall

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    #bouncing ball back if it hits paddles

    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()

    # checking if paddles miss ball

    if ball.xcor()>380:
        ball.resetposition()
        score.l_point()

    if ball.xcor()<-380:
        ball.resetposition()
        score.r_point()


screen.exitonclick()