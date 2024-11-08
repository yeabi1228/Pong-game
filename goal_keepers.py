from turtle import Turtle,Screen
screen = Screen()
class Paddle(Turtle):
    def __init__(self,x_value,y_value):
        super().__init__()
        self.position = (x_value,y_value)
        self.player1()

    def player1(self):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(self.position)

    def up(self):
        new_y = self.ycor()+20
        self.goto(self.xcor(),new_y)
        if self.ycor() >= 255 :
            self.down()
        # Screen().update()

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)
        if self.ycor()<-240:
            self.up()
        # screen.update()
