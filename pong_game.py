from turtle import Turtle, Screen
from goal_keepers import Paddle
from create_ball import Ball
from score_board import Scoreboard
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("pong game")
screen.tracer(0)
r_paddle = Paddle(x_value=370,y_value=0)
l_paddle = Paddle(x_value=-380,y_value=0)
score = Scoreboard()
ball = Ball()
screen.update()
user_aware = screen.textinput(
    title="press 'w' , 's' and 'up arrow' ,'down arrow' to make the left and the right paddle to move up and down respectively ",
    prompt="enter 'yes' to play or other not to continue")
screen.listen()
screen.onkeypress(r_paddle.up,"Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")
game_is_on = True
# sleep_speed = 0.1

while game_is_on :
    if user_aware == 'yes':
        screen.update()
        time.sleep(ball.sleep_speed)
        ball.penup()
        ball.move_ball()
        if ball.ycor() > 280 or ball.ycor() < -270:
            ball.wall_collision()
        if ball.distance(r_paddle)<50 and ball.xcor()> 350 or ball.distance(l_paddle)<50 and ball.xcor()< -360 :
            ball.paddle_collision()

            # sleep_speed *= 0.5
            # # time.sleep(0.08)

        if ball.xcor()< -390 :
            ball.reset_position()
            score.right_score_counter()
            # # ball.write("play again ", align="right")
            # ball.wall_collision()
            # ball.paddle_collision()
            # ball.goto(0, 0)
        if ball.xcor() > 380:
            ball.reset_position()
            score.left_score_counter()

screen.mainloop()