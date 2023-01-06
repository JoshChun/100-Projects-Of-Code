#Import libraries
import turtle

#Create screen
screen = turtle.Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=1000, height=1000)

#Create left paddle
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("white")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400,0)

#Create right paddle
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("white")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400,0)

#Create circle ball
ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 5
ball.dy = -5

#Intialise player score
player_one = 0
player_two = 0

#Create score display
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Player 1 : 0    Player 2 : 0", align="center", font=("Courier", 24, "normal"))

#Keyboard functions to control paddles
def left_pad_up():
    y = left_pad.ycor()
    y += 20
    left_pad.sety(y)

def left_pad_down():
    y = left_pad.ycor()
    y -= 20
    left_pad.sety(y)

def right_pad_up():
    y = right_pad.ycor()
    y += 20
    right_pad.sety(y)

def right_pad_down():
    y = right_pad.ycor()
    y -= 20
    right_pad.sety(y)

#Set keyboard bindings
screen.listen()
screen.onkeypress(left_pad_up, "w")
screen.onkeypress(left_pad_down, "s")
screen.onkeypress(right_pad_up, "Up")
screen.onkeypress(right_pad_down, "Down")

while True:
    screen.update()

    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    # Checking borders
    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1
 
    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1
 
    if ball.xcor() > 500:
        ball.goto(0, 0)
        ball.dy *= -1
        player_one += 1
        score.clear()
        score.write("Player 1 : {}    Player 2 : {}".format(player_one, player_two), align="center",font=("Courier", 24, "normal"))
 
    if ball.xcor() < -500:
        ball.goto(0, 0)
        ball.dy *= -1
        player_one += 1
        score.clear()
        score.write("Player 1 : {}    Player 2 : {}".format(player_one, player_two), align="center",font=("Courier", 24, "normal"))
 
	# Paddle ball collision
    if (ball.xcor() > 360 and ball.xcor() < 370) and (ball.ycor() < right_pad.ycor()+40 and ball.ycor() > right_pad.ycor()-40):
        ball.setx(360)
        ball.dx*=-1
		
    if (ball.xcor()<-360 and ball.xcor()>-370) and (ball.ycor()<left_pad.ycor()+40 and ball.ycor()>left_pad.ycor()-40):
        ball.setx(-360)
        ball.dx*=-1
