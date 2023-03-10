#Import libraries
import turtle

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

#Create screen
screen = turtle.Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

#Create top line
top_line = turtle.Turtle()
top_line.shape("square")
top_line.color("white")
top_line.shapesize(stretch_wid=1, stretch_len=50)
top_line.penup()
top_line.goto(0,300)

#Create bottom line
bottom_line = turtle.Turtle()
bottom_line.shape("square")
bottom_line.color("white")
bottom_line.shapesize(stretch_wid=1, stretch_len=50)
bottom_line.penup()
bottom_line.goto(0,-300)

#Create dividing line
div_line = turtle.Turtle()
div_line.penup()
div_line.goto(0,300)
div_line.seth(270)
div_line.hideturtle()

for i in range(11):
    div_line.penup()
    div_line.forward(50)
    div_line.dot(10,"white")
    div_line.pendown()

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
score.goto(0,180)
score.write("0    0", align="center", font=("Arial", 100, "bold"))

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
        score.write("{}    {}".format(player_one, player_two), align="center",font=("Arial", 100, "bold"))
 
    if ball.xcor() < -500:
        ball.goto(0, 0)
        ball.dy *= 1
        player_two += 1
        score.clear()
        score.write("{}    {}".format(player_one, player_two), align="center",font=("Arial", 100, "bold"))
 
	# Paddle ball collision
    if (ball.xcor() > 360 and ball.xcor() < 370) and (ball.ycor() < right_pad.ycor()+40 and ball.ycor() > right_pad.ycor()-40):
        ball.setx(360)
        ball.dx*=-1
		
    if (ball.xcor()<-360 and ball.xcor()>-370) and (ball.ycor()<left_pad.ycor()+40 and ball.ycor()>left_pad.ycor()-40):
        ball.setx(-360)
        ball.dx*=-1