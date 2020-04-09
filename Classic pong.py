# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 14:02:44 2020
# Classic Pong Game
@author: William
"""
import turtle
import time




wn = turtle.Screen()
wn.title("Pong Classic by William Schulz")
wn.bgcolor("black") #background colour
wn.setup(width = 800, height = 600)
wn.tracer(0) # stops window from updating

# Score
score_a = 0
score_b = 0

# Menu


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # speed of animation
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350,0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0)

# Puck
puck = turtle.Turtle()
puck.speed(0)
puck.shape("square")
puck.color("white")
puck.penup()
puck.goto(0,0)
puck.dx = 0.15
puck.dy = 0.15

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {}    Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
# Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Main game loop
while True:
    #menu_selections()
    #time.sleep(2)
    
    wn.update()
    
    #Move the puck
    #time.sleep(2)
    puck.setx(puck.xcor() + puck.dx)
    puck.sety(puck.ycor() + puck.dy)
    
    # Border Checking
    if puck.ycor() > 290:
        puck.sety(290)
        puck.dy *= -1
    elif puck.ycor() < -290:
        puck.sety(-290)
        puck.dy *= -1
    elif puck.xcor() > 390:
        puck.goto(0, 0)
        puck.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    elif puck.xcor() < -390:
        puck.goto(0, 0)
        puck.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    
    # Bounce off the paddle
    if (puck.xcor() > 340 and puck.xcor() < 350) and (puck.ycor() < paddle_b.ycor() + 40 and puck.ycor() > paddle_b.ycor() - 40):
        puck.setx(340)
        puck.dx *= -1
    
    elif (puck.xcor() < -340 and puck.xcor() > -350) and (puck.ycor() < paddle_a.ycor() + 40 and puck.ycor() > paddle_a.ycor() - 40):
        puck.setx(-340)
        puck.dx *= -1
    
    #score management
    if score_a == 11:
        pen.clear()
        pen.write("Player A is the winner!", align="center", font=("Courier", 24, "normal"))
    
    elif score_b == 11:
        pen.clear()
        pen.write("Player B is the winner!", align="center", font=("Courier", 24, "normal"))
    
    
    
        