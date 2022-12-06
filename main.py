from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import  Scoreboard
import random
scr = Screen()
scr.setup(600,600)
scr.bgcolor("black")
scr.title("ping-pong")




paddlel = Paddle()
paddler = Paddle()
paddlel.create_leftpaddle()
paddler.create_rightpaddle()
paddlel.speed(0.0001)
paddler.speed(0.0001)


scr.listen()
scr.onkey(key="w",fun = paddlel.move_leftpaddleup)
scr.onkey(key="s",fun = paddlel.move_leftpaddledown)
scr.onkey(key="Up",fun = paddler.move_rightpaddleup)
scr.onkey(key="Down",fun = paddler.move_rightpaddledown)



ball = Ball()
score = Scoreboard()
score.create_score_left()
score.create_score_right()
game_on = True
while game_on:

    right_angle = random.randint(1,60)
    ball.speed(2)
    not_collide_right = True
    not_collide_left = True
    while not_collide_right:

        ball.move_ball_toright(right_angle)

        #check collision with wall

        if  ball.xcor()>300:
            ball.reset_right_position()
            not_collide_right=False


        #chceck collision with paddle


        if ball.distance(paddler)<40:
            not_collide_right = False
            score.update_right()



    left_angle = random.randint(120,180)
    while not_collide_left:

        ball.move_ball_toright(left_angle)

        # check collision with wall

        if ball.xcor() < -290:
            not_collide_left = False
            ball.reset_left_position()


        # chceck collision with paddle


        if ball.distance(paddlel) < 40:
            not_collide_left = False
            score.update_left()
#ball.move_ball_toleft(left_angle)



scr.exitonclick()
