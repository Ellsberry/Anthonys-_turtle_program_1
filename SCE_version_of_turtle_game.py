from turtle import Screen
from turtle import Turtle as T
import turtle as t
import random
from sys import exit
import math
import winsound

# set up screen
# tutorial uses wn (short for window) for screen
wn = Screen()
wn.bgcolor("black")
wn.title("Turtle Wars")

# set the score to zero
score = 0
score_pen = t.Turtle()
score_pen.speed(0)
score_pen.color('White')
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: {}".format(score)
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

# create the player's bullet
bullet = t.Turtle()
bullet.color("yellow")
bullet.shape('triangle')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

# Create player
player = t.Turtle()
player.shape("turtle")
player.color("green")
player.penup()

"""
t.shape("turtle")
t.color("green")
# t.pencolor("black")
t.penup()
"""

t.setup(600, 300)
x = int(player.xcor())
y = int(player.ycor())
# print(f"x = {x} y = {y}")
number_of_enemies = 5
enemies = []
turtle_direction = 0
bullet_path = set()
bulletspeed = 60

# bullet state {ready = ready to fire & fire = bullet is firing
bulletstate = "ready"


def fire_bullet():
    # declare bulletstate as a global variable
    global bulletstate
    global heading_set
    global heading
    if bulletstate == 'ready':
        heading_set = True
        play_sound("LASER.WAV")
        bulletstate = 'fire'
        # move the bullet above the player
        bpx = player.xcor()
        bpy = player.ycor()
        bullet.setposition(bpx, bpy)
        # bullet.setheading(heading)
        bullet.showturtle()


def left():
    global x
    global y
    x -= 20
    if x < -600:
        x = -600
    player.goto(x, y)


def right():
    global x
    global y
    x += 20
    if x > 600:
        x = 600
    player.goto(x, y)


def up():
    global x
    global y
    y += 20
    if y > 300:
        y = 300
    player.goto(x, y)


def down():
    global x
    global y
    y -= 20
    if y < -300:
        y = -300
    player.goto(x, y)


def rotate_clockwise():
    global turtle_direction
    player.right(90)
    turtle_direction += 90


def rotate_counter_clockwise():
    global turtle_direction
    player.left(90)
    turtle_direction -= 90


wn.listen()
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")
wn.onkeypress(fire_bullet, "space")
wn.onkeypress(rotate_clockwise, "r")
wn.onkeypress(rotate_counter_clockwise, "l")

# Anthony & Steve create a new loop.
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
player_lives = 3


def is_collision(t1, t2):
    # print("t1x= ",t1.xcor(), "t1y = ",t1.ycor(), "t2x = ",t2.xcor(),"t2y = ",t2.ycor())
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 25:
        return True
    else:
        return False


def play_sound(sound_file):
    winsound.PlaySound(sound_file, winsound.SND_ASYNC)


while player_lives > 0:
    global heading_set
    global heading
    # print(f"x = {x} y = {y}")
    # Move the bullet
    if bulletstate == "fire":
        if heading_set:
            heading = player.heading()
            bullet.setheading(heading)
            heading_set = False
        bullet_heading = bullet.heading()
        bby = bullet.ycor()
        bbx = bullet.xcor()
        bullet.forward(bulletspeed)
        by = bullet.ycor()
        bx = bullet.xcor()
        # set_y = range(bby, by)
        # set_x = range(bbx, bx)
        bullet_path.clear()
        if by >= 300 or by <= -300 or bx >= 600 or bx <= -600:
            bulletstate = "ready"
            bullet.hideturtle()
        if bullet_heading == 90:
            bullet_path.add((int(bbx), int(bby)))
            for index in range(60):
                bby += 1
                bullet_path.add((int(bbx), int(bby)))
            print(f"bullet_path = {bullet_path}")
        if bullet_heading == 270:
            bullet_path.add((int(bbx), int(bby)))
            for index in range(60):
                bby -= 1
                bullet_path.add((int(bbx), int(bby)))
            print(f"bullet_path = {bullet_path}")
        if bullet_heading == 180:
            bullet_path.add((int(bbx), int(bby)))
            for index in range(60):
                bbx -= 1
                bullet_path.add((int(bbx), int(bby)))
            print(f"bullet_path = {bullet_path}")
        if bullet_heading == 0:
            bullet_path.add((int(bbx), int(bby)))
            for index in range(60):
                bbx += 1
                bullet_path.add((int(bbx), int(bby)))
            print(f"bullet_path = {bullet_path}")

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
        if is_collision(bullet, enemy):
            enemy.hideturtle()
        if is_collision(enemy, player):
            play_sound('EXPLODE.WAV')
            player_lives -= 1
