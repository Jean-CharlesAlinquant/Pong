from turtle import Screen
from paddle import Paddle

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

screen.listen()
screen.onkey(l_paddle.move_up, "a")
screen.onkey(l_paddle.move_down, "z")
screen.onkey(r_paddle.move_up, KEY_UP)
screen.onkey(r_paddle.move_down, KEY_DOWN)

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
