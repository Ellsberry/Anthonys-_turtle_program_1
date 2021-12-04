from turtle import Screen
# from turtle import Turtle as nt
import turtle as t
import random
from sys import exit
import math
import winsound
wn = Screen()
t.shape("turtle")
t.color("green")
t.pencolor("black")
t.setup(600, 300)
t.penup()
x = int(t.xcor())
y = int(t.ycor())
# print(f"x = {x} y = {y}")
number_of_enemies = 4
enemies = []
# create the player's bullet
bullet = t.Turtle()
bullet.color("yellow")
bullet.shape('triangle')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed = 20

# bullet state {ready = ready to fire & fire = bullet is firing
bulletstate = "ready"


def fire_bullet():
    # declare bulletsate as a global variable
    global bulletstate
    if bulletstate == 'ready':
        play_sound("LASER.WAV")
        bulletstate = 'fire'
        # move the bullet above the player
        x = t.xcor()
        y = t.ycor() +10
        bullet.setposition(x, y)
        bullet. showturtle()



def left():
    global x
    global y
    x -= 20
    if x < -600:
        x = -600
    t.goto(x, y)


def right():
    global x
    global y
    x += 20
    if x > 600:
        x = 600
    t.goto(x, y)


def up():
    global x
    global y
    y += 20
    if y > 300:
        y = 300
    t.goto(x, y)


def down():
    global x
    global y
    y -= 20
    if y < -300:
        y = -300
    t.goto(x, y)


wn.listen()
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")
wn.onkeypress(fire_bullet, "space")

"""
for mom_using_the_wheelbarrow_outside in range(number_of_enemies):
    enemies.append(nt())

for enemy in enemies:
    enemy = t.Turtle()
    enemy.shape("turtle")
    enemy.color("red")
    enemy.pencolor("black")
    enemy.penup()
    enemy.speed(3)
    ex = random.randint(-300, 300)
    ey = random.randint(-150, 150)
    enemy.setposition(ex, ey)
"""

# Anthony creates a new loop.
for index in range(number_of_enemies):
    enemies.append(t.Turtle())
    enemies[index].shape("turtle")
    if index == 1:
        enemies[index].color("blue")
    elif index == 2:
        enemies[index].color("yellow")
    else:
        enemies[index].color("violet")

    enemies[index].penup()
    ex = random.randint(-300, 300)
    ey = random.randint(-150, 150)
    enemies[index].setposition(ex, ey)


enemy_go = True


def is_collision(t1, t2):
    # print("t1x= ",t1.xcor(), "t1y = ",t1.ycor(), "t2x = ",t2.xcor(),"t2y = ",t2.ycor())
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2)+math.pow(t1.ycor()-t2.ycor(), 2))
    if distance < 25:
        return True
    else:
        return False


def play_sound(sound_file):
    winsound.PlaySound(sound_file, winsound.SND_ASYNC)


while enemy_go:
    # print(f"x = {x} y = {y}")
    for enemy in enemies:
        rotate = random.randint(1, 180)
        RightOrLeft = random.randint(1, 2)
        enemy_distance = random.randint(20, 100)
        ey = int(enemy.ycor())
        ex = int(enemy.xcor())
        if RightOrLeft == 1:
            enemy.right(rotate)
        else:
            enemy.left(rotate)
        enemy.forward(enemy_distance)
        if enemy.xcor() > 600:
            enemy.forward(-enemy_distance)
        elif enemy.xcor() < -600:
            enemy.forward(-enemy_distance)
        elif enemy.ycor() > 300:
            enemy.forward(-enemy_distance)
        elif enemy.ycor() < -300:
            enemy.forward(-enemy_distance)
        if is_collision(enemy, t):
            play_sound('EXPLODE.WAV')
            exit()
