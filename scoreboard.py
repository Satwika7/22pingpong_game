from turtle import Turtle,Screen
ALIGNMENT = "center"
FONT = ('arial', 12, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.leftscore = 0
        self.rightscore = 0

    def create_score_left(self):
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-150,280)
        self.write("A score = 0",align=ALIGNMENT,font=FONT)

    def create_score_right(self):
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(150,280)
        self.write("B score = 0",align=ALIGNMENT,font=FONT)

    def update_right(self):
        self.clear()
        self.goto(150, 280)
        self.rightscore+=1
        self.write(f"B score = {self.rightscore}",align=ALIGNMENT,font=FONT)
        self.goto(-150, 280)
        self.write(f"A score = {self.leftscore}",align=ALIGNMENT,font=FONT)

    def update_left(self):
        self.clear()
        self.goto(-150, 280)
        self.leftscore+=1
        self.write(f"A score = {self.leftscore}",align=ALIGNMENT,font=FONT)
        self.goto(150, 280)
        self.write(f"B score = {self.rightscore}",align=ALIGNMENT,font=FONT)
