# Simple Snake Game in Python 3 for Beginners
# By @Atamyrat2005

import turtle
import time
import random

tizlik = 0.15

#Ekrana çykarýan, 

ekran = turtle.Screen()
ekran.title('Snake Game by @Atamyrat2005')
ekran.bgcolor('green')
ekran.setup(width=600, height=600)
ekran.tracer(0)

# Ýylanyň kellesini yasamak

kelle = turtle.Turtle()
kelle.speed(0)
kelle.shape('square')
kelle.color('black')
kelle.penup()
kelle.goto(0, 100)
kelle.direction = 'stop'

# Ýylanyň awyny ýasamak

awy = turtle.Turtle()
awy.speed(0)
awy.shape('circle')
awy.color('red') 
awy.penup()
awy.goto(0, 0)
awy.shapesize(0.80, 0.80)

guyruglar = []
utuk = 0

# Utuky ýazdyrmak

yaz = turtle.Turtle()
yaz.speed(0)
yaz.shape('square')
yaz.color('white') 
yaz.penup()
yaz.goto(0, 260)
yaz.hideturtle()
yaz.write('Utuk: {}'. format(utuk), align='center', font=('Courier', 24, 'normal'))

# Ýylana hereket etdirmek 

def hereket():
    if kelle.direction == 'up':
        y = kelle.ycor()
        kelle.sety(y + 20)
    if kelle.direction == 'down':
        y = kelle.ycor()
        kelle.sety(y - 20)
    if kelle.direction == 'right':
        x = kelle.xcor()
        kelle.setx(x + 20)
    if kelle.direction == 'left':
        x = kelle.xcor()
        kelle.setx(x - 20)


def goUp():
    if kelle.direction != 'down':
        kelle.direction = 'up'

def goDown():
    if kelle.direction != 'up':
        kelle.direction = 'down'

def goRight():
    if kelle.direction != 'left':
        kelle.direction = 'right'

def goLeft():
    if kelle.direction != 'right':
        kelle.direction = 'left'

ekran.listen()
ekran.onkey(goUp, 'Up')
ekran.onkey(goDown, 'Down')
ekran.onkey(goRight, 'Right')
ekran.onkey(goLeft, 'Left')

while True:
    ekran.update()

# Ýylan ekerandan çykanda oýun gutarýa (Game Over)

    if kelle.xcor() > 300 or kelle.xcor() < -300 or kelle.ycor() > 300 or kelle.ycor() < - 300:
        yaz.clear()
        yaz.goto(0, 0)
        yaz.write('Game Over!', align='center', font=('Courier', 36, 'normal'))
        ekran.update()
        time.sleep(2)
        break

    if kelle.distance(awy) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        awy.goto(x, y)

        utuk = utuk + 10
        yaz.clear()
        yaz.write('Utuk: {}'. format(utuk), align='center', font=('Courier', 24, 'normal'))

        tizlik = tizlik -0.001

# Ýylan her gezek awyna degende ýylana bir guýruk oşulýa

        tazeGuyrugy = turtle.Turtle()
        tazeGuyrugy.speed(0)
        tazeGuyrugy.shape('square')
        tazeGuyrugy.color('white')
        tazeGuyrugy.penup()
        guyruglar.append(tazeGuyrugy)

    for i in range(len(guyruglar) - 1, 0, -1):
        x = guyruglar[i - 1].xcor()
        y = guyruglar[i - 1].ycor()
        guyruglar[i].goto(x, y)

    if len(guyruglar) > 0:
        x = kelle.xcor()
        y = kelle.ycor()
        guyruglar[0].goto(x, y)

    hereket()
    time.sleep(tizlik)
