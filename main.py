from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

WIDTH = 800
HEIGHT = 600
BACKGROUND_COLOR = "black"
TITLE = "Pong Game"
KEY_UP = "Up"
KEY_DOWN = "Down"

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor(BACKGROUND_COLOR)
screen.title(TITLE)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(l_paddle.move_up, "a")
screen.onkey(l_paddle.move_down, "z")
screen.onkey(r_paddle.move_up, KEY_UP)
screen.onkey(r_paddle.move_down, KEY_DOWN)

x_shift = 10
y_shift = 10

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect Collision with top or bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect Collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect when right paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect when left paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
