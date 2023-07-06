from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key="Up", fun=r_paddle.goo_up)
screen.onkeypress(key="Down", fun=r_paddle.go_down)
screen.onkeypress(key="w", fun=l_paddle.goo_up)
screen.onkeypress(key="s", fun=l_paddle.go_down)


game_on = True
while game_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() < -380:
        ball.reset_pos()
        scoreboard.r_point()

    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.l_point()

    if scoreboard.l_score >= 2:
        game_on = False
        scoreboard.game_over("LEFT SIDE")

    if scoreboard.r_score >= 2:
        game_on = False
        ball.hideturtle()
        scoreboard.game_over("RIGHT SIDE")

        
screen.exitonclick()
