from turtle import Screen
import turtle as t
import random
from sys import exit
import math
import winsound
wn = Screen()
t.shape("turtle")
t.color("green")
t.pencolor("black")
t.setup(600,300)
t.penup()
x = int(t.xcor())
y = int(t.ycor())
print(f"x = {x} y = {y}")
def L():
    global x
    global y
    x -= 20
    if x < -600:
        x = -600
    t.goto(x,y)
def R():
    global x
    global y
    x += 20
    if x > 600:
        x = 600
    t.goto(x,y)
def U():
    global x
    global y
    y += 20
    if y > 300:
        y = 300
    t.goto(x,y)
def D():
    global x
    global y
    y -= 20
    if y < -300:
        y = -300
    t.goto(x,y)
wn.listen()
wn.onkeypress(U,"Up")
wn.onkeypress(D,"Down")
wn.onkeypress(L,"Left")
wn.onkeypress(R,"Right")
enemy = t.Turtle()
enemy.shape("turtle")
enemy.color("red")
enemy.pencolor("black")
enemy.penup()
enemy.speed(3)
enemy.goto(30,0)
enemygo = True
def isCollision(t1,t2):
    # print("t1x= ",t1.xcor(), "t1y = ",t1.ycor(), "t2x = ",t2.xcor(),"t2y = ",t2.ycor())
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 25:
        return True
    else:
        return False
def play_sound(sound_file, time = 0):
    winsound.PlaySound(sound_file, winsound.SND_ASYNC)
while enemygo:
    print(f"x = {x} y = {y}")
    edistance = random.randint(20,100)
    RightOrLeft = random.randint(1,2)
    rotate = random.randint(1,180)
    ey = int(enemy.ycor())
    ex = int(enemy.xcor())
    if RightOrLeft == 1:
        enemy.right(rotate)
    else:
        enemy.left(rotate)
    enemy.forward(edistance)
    if enemy.xcor() > 600:
        enemy.forward(-edistance)
    elif enemy.xcor() < -600:
        enemy.forward(-edistance)
    elif enemy.ycor() > 300:
        enemy.forward(-edistance)
    elif enemy.ycor() < -300:
        enemy.forward(-edistance)
    if isCollision(enemy,t):
        play_sound('EXPLODE.WAV')
        exit()
