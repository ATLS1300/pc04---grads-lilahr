"""
Created on Thu Sep 15 11:39:56 2020
PC04 start code
@author: Lila Hunter-Reay

********* HEY, READ THIS FIRST **********

This code draws a looping flower, followed by a looping star, followed by a square in a random position.

"""
#built from Megan Dukek's pseudocode

import turtle
import math, random

turtle.colormode(255)
# turtle.tracer(0) # uncomment this line to turn off turtle's animation. You must update the image yourself using panel.update() (line 42)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 600 # width of panel
h = 600 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 

# You must make 2 turtle variables
# You must use 2 for loops (a nested for loop counts as 2!)
# You must use at least 1 random element (something from the random library)
# Don't forget to comment your code! (what does each for loop do? What does the random function you'll use do?)

# =============== ADD YOUR CODE BELOW! =================
turtle.bgcolor("black")  #making the background black

petals = turtle.Turtle()  #creating a turtle called petals
petals.pencolor(127,0,255)
petals.pensize(2)
petals.speed(30)
petals.pendown()

#creating petals at 90 degree angles from each other that increase by 10 each time 
for i in range(50):
    petals.circle(i+10)
    petals.right(90)
petals.penup()

star = turtle.Turtle()  #creating a turtle called star
star.pencolor(255,255,0)
star.pensize(2)
star.penup()
star.goto(-2,15) #centering the star with the middle of the petals
star.speed(20)
star.pendown()

#star loops through 60 times
for i in range(60):
    star.forward(50)
    star.right(144)  #turning at 144 degree angle
    star.forward(50)
    star.right(10)
star.penup()
    
square = turtle.Turtle()  #creating a turtle called square
square.pencolor("blue")
square.penup()
# making the x and y coordinates random
square.goto(random.randint(100,200),random.randint(100,200))
square.pendown()

for i in range(4): #drawing the square
    square.forward(20)
    square.right(90)

# =================== CLEAN UP =========================
turtle.done()
