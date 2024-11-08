from turtle import Turtle
class Ball(Turtle):
    dy = -1
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.sleep_speed = 0.1
        self.x_move = 10
        self.y_move = 10
        # self.shapesize(stretch_wid=2,stretch_len=2)

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def wall_collision(self):
            self.y_move *= -1

    def paddle_collision(self):
        self.x_move *= -1
        self.sleep_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.sleep_speed = 0.1
        self.wall_collision()
        self.paddle_collision()




