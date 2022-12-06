from turtle import Turtle

class Paddle(Turtle):

    def __init__(self):
        super().__init__()



    def create_rightpaddle(self):
            self.hideturtle()
            self.color("white")
            self.shape("square")
            self.shapesize(stretch_wid=5,stretch_len=1)
            self.penup()
            self.goto(280,0)
            self.showturtle()


    def create_leftpaddle(self):
            self.hideturtle()
            self.color("white")
            self.shape("square")
            self.shapesize(stretch_wid=5, stretch_len=1)
            self.penup()
            self.goto(-280,0)
            self.showturtle()



    def move_rightpaddleup(self):
      y=self.ycor()
      self.goto(self.xcor(),y+20)



    def move_leftpaddleup(self):
        y = self.ycor()
        self.goto(self.xcor(), y + 20)


    def move_rightpaddledown(self):
        y = self.ycor()
        self.goto(self.xcor(), y - 20)


    def move_leftpaddledown(self):
        y = self.ycor()
        self.goto(self.xcor(), y - 20)





