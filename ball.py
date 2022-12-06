from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()



    def create_ball(self):
         self.shape("circle")
         self.color("blue")
         self.penup()
         self.goto(0,-280)


    def move_ball_toright(self,angle):
        self.setheading(angle)
        self.forward(10)



    def move_ball_toleft(self,angle):
        self.setheading(angle)
        self.forward(20)


    def reset_right_position(self):
        self.hideturtle()
        self.goto(0,0)
        self.showturtle()
        self.move_ball_toleft(random.randint(91,270))
        #self.bounce_x()


    def reset_left_position(self):
        self.hideturtle()
        self.goto(0, 0)
        self.showturtle()
        self.move_ball_toright(random.randint(271,450))
