from turtle import Turtle, Screen
from move_paddle import Paddle
from ball import Ball
from scorebored import ScoreBored
import time
import random


screen=Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("YINGWEI'S PING PONG GAME")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
score_bored = ScoreBored()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # detect colision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.vertical_bounce()
    # detect ball collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and l_paddle.xcor()<-340:
        ball.horizontal_bounce()
    # detect ball cross the paddle
    if ball.xcor() > 380:
        ball.reset_position()
        score_bored.r_increase_score()
    if ball.xcor() < -380:
        ball.reset_position()
        score_bored.l_increase_score()
        


screen.exitonclick()
