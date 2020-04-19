import turtle
import random
import math


wn = turtle.Screen()
wn.bgcolor('black')

first = turtle.Turtle()
first.speed(20)
first.color('gold')

def drawSquare(length, angle):
    for i in range(4):
        first.forward(length)
        first.right(angle)

for i in range(60):
    drawSquare(100, 90)
    first.right(11)

second = turtle.Turtle()
second.speed(10)
second.color('crimson')

def drawSquare(length, angle):
    for i in range(4):
        second.forward(length)
        second.right(angle)

for i in range(60):
    drawSquare(100, 90)
    second.right(11)

third = turtle.Turtle()
third.speed(10)
third.color('whitesmoke')

def drawSquare(length, angle):
    for i in range(4):
        third.forward(length)
        third.right(angle)

for i in range(60):
    drawSquare(100, 90)
    third.right(11)


fourth = turtle.Turtle()
fourth.speed(10)
fourth.color('indigo')

def drawSquare(length, angle):
    for i in range(4):
       fourth.forward(length)
       fourth.right(angle)

for i in range(60):
    drawSquare(100, 90)
    fourth.right(11)    

fifth = turtle.Turtle()
fifth.speed(10)
fifth.color('burlywood')

def drawSquare(length, angle):
    for i in range(4):
       fifth.forward(length)
       fifth.right(angle)

for i in range(60):
    drawSquare(100, 90)
    fifth.right(11)    


sixth = turtle.Turtle()
sixth.speed(10)
sixth.color('lime')

def drawSquare(length, angle):
    for i in range(4):
       sixth.forward(length)
       sixth.right(angle)

for i in range(60):
    drawSquare(100, 90)
    sixth.right(11)    

