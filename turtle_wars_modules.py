"""This module contains the player, bullet and enemy classes including
        their attributes and methods"""
import sys
import turtle
import turtle as t
from turtle import Screen
# import sys
import random
# from sys import exit
import math
import winsound
from path import path

# Setup Screen set score to zero
# set up screen use wn (short for window) for screen
wn = Screen()
wn.bgcolor("black")
wn.title("Turtle Wars")

# Display a score box and set the score to zero
score = 0
score_pen = t.Turtle()
score_pen.speed(0)
score_pen.color('White')
score_pen.penup()
score_pen.setposition(-290, 280)
score_string = "Score: {}".format(score)
score_pen.write(score_string, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

# Build Player objects
player = t.Turtle()
player.shape("turtle")
player.color('white')
player.speed(0)
player.penup()
player_lives = ""
number_of_player_lives = 3   # int(turtle.textinput(player_lives, "How many player lives do you want?   "))

# Build enemy objects
# number_of_enemies = int(input("How many enemies do you want?")
# points is the number of points scored when an enemy is destroyed
points = 1                            # at the beginning of the game an enemy is worth 1 point
enemies = []
enemy_number = ""
number_of_enemies = 5   # int(turtle.textinput(enemy_number, "How many enemies do you want?   "))
for index in range(number_of_enemies):
    enemy = t.Turtle()
    enemy.speed(3)
    enemies.append(enemy)
    enemies[index].shape("turtle")
    if index == 0:
        enemies[index].color("blue")
    elif index == 1:
        enemies[index].color("green")
    elif index == 2:
        enemies[index].color("yellow")
    elif index == 3:
        enemies[index].color("orange")
    elif index == 4:
        enemies[index].color("grey")
    else:
        enemies[index].color("violet")
    enemies[index].penup()
    x = random.randint(-300, 300)
    y = random.randint(-150, 150)
    enemies[index].setposition(x, y)

# Build bullet object
bullet = t.Turtle()
bullet.color("red")
bullet.shape('triangle')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()
b_path = set()
d_score_points = 1
x_score = 0


def play_sound(sound_file):
    winsound.PlaySound(sound_file, winsound.SND_ASYNC)



def is_collision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 25:
        play_sound('EXPLODE.WAV')
        return True
    else:
        return False


# Event driven movements for Bullet
def fire_bullet():
    play_sound("LASER.WAV")
    bullet_heading = player.heading()  # ensure the bullet is out of the mouth of the player
    # establish the bullet's beginning and ending path and save in bullet_path
    b1x = player.xcor()
    b1y = player.ycor()
    bullet.setposition(b1x, b1y)
    b_heading = int(player.heading())
    bullet.setheading(b_heading)
    bullet.showturtle()
    bullet_path = set()
    if bullet_heading == 90:
        for index in range(60):
            b1y += 1
            bullet_path.add((int(b1x), int(b1y)))
        print(f"bullet_path = {bullet_path}")
    if bullet_heading == 270:
        bullet_path.add((int(b1x), int(b1y)))
        for index in range(60):
            b1y -= 1
            bullet_path.add((int(b1x), int(b1y)))
        print(f"bullet_path = {bullet_path}")
    if b_heading == 180:
        bullet_path.add((int(b1x), int(b1y)))
        for index in range(60):
            b1x -= 1
            bullet_path.add((int(b1x), int(b1y)))
        print(f"bullet_path = {bullet_path}")
    if b_heading == 0:
        bullet_path.add((int(b1x), int(b1y)))
        for index in range(60):
            b1x += 1
            bullet_path.add((int(b1x), int(b1y)))
        print(f"bullet_path = {bullet_path}")
    bullet.setposition(b1x, b1y)


def bullet_move():
    bullet_heading = player.heading()  # ensure the bullet is out of the mouth of the player
    # establish the bullet's beginning and ending path and save in bullet_path
    b1x = bullet.xcor()
    b1y = bullet.ycor()
    b_heading = int(bullet.heading())
    bullet.setheading(b_heading)
    bullet.showturtle()
    bullet_path = set()
    if bullet_heading == 90:
        for index in range(60):
            b1y += 1
            bullet_path.add((int(b1x), int(b1y)))
        print(f"bullet_path = {bullet_path}")
    if bullet_heading == 270:
        bullet_path.add((int(b1x), int(b1y)))
        for index in range(60):
            b1y -= 1
            bullet_path.add((int(b1x), int(b1y)))
        print(f"bullet_path = {bullet_path}")
    if b_heading == 180:
        bullet_path.add((int(b1x), int(b1y)))
        for index in range(60):
            b1x -= 1
            bullet_path.add((int(b1x), int(b1y)))
        print(f"bullet_path = {bullet_path}")
    if b_heading == 0:
        bullet_path.add((int(b1x), int(b1y)))
        for index in range(60):
            b1x += 1
            bullet_path.add((int(b1x), int(b1y)))
        print(f"bullet_path = {bullet_path}")
    bullet.setposition(b1x, b1y)


def increase_score(d_score, score_points):
    """Display an increase score"""
    score_pen.clear()
    d_score = d_score + score_points
    score_pen.setposition(-290, 280)
    d_score_string = "Score: {}".format(d_score)
    score_pen.write(d_score_string, False, align="left", font=("Arial", 14, "normal"))
    score_pen.hideturtle()
    return d_score
# 0 + 1 = 1

# Movement of Enemy
def move_enemy(num_player_lives, b_path, d_score, d_score_points):
    x_score = 0
    for e_enemy in enemies:
        rotate = random.randint(1, 180)
        right_or_left = random.randint(1, 2)
        enemy_distance = random.randint(20, 100)
        ey1 = int(e_enemy.ycor())
        ex1 = int(e_enemy.xcor())
        e_enemy.speed(9)                               # This is where we change the speed of the enemy turtles.
        if right_or_left == 1:
            e_enemy.right(rotate)
        else:
            e_enemy.left(rotate)
        e_enemy.forward(enemy_distance)
        if e_enemy.xcor() > 600:
            e_enemy.forward(-enemy_distance)
        elif e_enemy.xcor() < -600:
            e_enemy.forward(-enemy_distance)
        elif e_enemy.ycor() > 300:
            e_enemy.forward(-enemy_distance)
        elif e_enemy.ycor() < -300:
            e_enemy.forward(-enemy_distance)
        ey2 = int(e_enemy.ycor())
        ex2 = int(e_enemy.xcor())
        enemy_path = path(ex1, ey1, ex2, ey2)
        # enemy_path = path(-25, -25, -19, -30)
        print("enemy path = ", enemy_path)
        if is_collision(player, e_enemy):
            num_player_lives -= 1
            if num_player_lives <= 0:
                sys.exit()
            continue
        if len(enemy_path.intersection(b_path)) == 0:
            e_enemy.hideturtle()
            play_sound('EXPLODE.WAV')
            score = increase_score(x_score, points)
            x_score += 1
    return num_player_lives, x_score


# The remainder of the program is event driven based on keyboard inputs
wn.listen()

wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")
wn.onkeypress(fire_bullet, "space")
wn.onkeypress(rotate_clockwise, "r")
wn.onkeypress(rotate_counter_clockwise, "l")

while True:
    number_of_player_lives = move_enemy(number_of_player_lives, b_path, score, d_score_points)

wn.mainloop()
