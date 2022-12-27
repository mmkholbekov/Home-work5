class Hero:
    bot = 'bot'
    def __init__(self,name,abyliti):
        self.name = name
        self.abyliti = abyliti

class Hero_super(Hero):
    dotty = 'dotty'

    def __str__(self):
        print(f'{self.name}')

    def new(self):
        print('it is super_hero')


# ВИРУС

import turtle
screen = turtle.Screen()
screen.setup(500, 600, startx=0, starty=100)
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pencolor("green")
a = 0
b = 0
t.speed(0)
t.penup()
t.goto(0, 200)
t.pendown()
while(True):
    t.forward(a)
    t.right(b)
    a += 3
    b += 1
    if b == 210:
        break
    t.hideturtle()
turtle.done()

# Вирус 2
# from turtle import *
# color("green")
# bgcolor("black")
# speed(11)
# hideturtle()
# a = 0
# while a < 200:
#     right(a)
#     forward(a * 3)
#     a = a + 1
