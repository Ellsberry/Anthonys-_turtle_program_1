import time
from turtle import Screen
import turtle as t
from anthonys_turtle_child_class import AnthonysTurtleChildClass
from path import path
import math
import winsound
import sys

# Setup Screen as wn (short for window)
wn = Screen()
wn.bgcolor("black")
wn.title("Anthony's Turtle Wars")

# Display a score box and set the score to zero
score = 0
score_pen = t.Turtle()
score_pen.speed(0)
score_pen.color('White')
score_pen.penup()
score_pen.setposition(-290, 280)
score_string = "Score: {}".format(score)
# score_pen.write(score_string, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()


def change_score(previous_score, amount):
    """previous score is the score before the new amount is added"""
    new_score = previous_score + amount
    score_pen.clear()
    score_pen.setposition(-290, 280)
    # new_score_string = "Score: {}".format(new_score)
    # score_pen.write(new_score_string, False, align="left", font=("Arial", 14, "normal"))
    score_pen.hideturtle()
    return new_score


def play_sound(sound_file):
    if sound_file == "EXPLODE.WAV":
        sound_path = r"C:\Users\Steve Ellsberry\PycharmProjects\Anthonys-_turtle_program_1\EXPLODE.WAV"
        # sound_path = r"C:\Users\ajh08_idy4tts\Documents\Anthonys-_turtle_program_1\EXPLODE.WAV"
    else:
        sound_path = r"C:\Users\Steve Ellsberry\PycharmProjects\Anthonys-_turtle_program_1\LASER.WAV"
        # sound_path = r"C:\Users\ajh08_idy4tts\Documents\Anthonys-_turtle_program_1\LASER.WAV"
    winsound.PlaySound(sound_path, winsound.SND_ASYNC)


def is_collision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 25:
        play_sound('EXPLODE.WAV')
        return True
    else:
        return False


# Create player

anthony = AnthonysTurtleChildClass("player", int(5), 'cyan')
players_name = t.textinput(wn,"Hi Who is going to play the game")
anthony.lives = int(t.textinput(wn, "How many player lives do you want to start with?"))


# AND UN-COMMENT THE NUMBER OF ENEMIES INPUT LINE

def create_new_enemies(e_number, e_speed):
    e_number += 1
    e_speed += 1
    enemies = []                                                         # this is for the list of enemies
    for index in range(e_number):
        if index == 0:
            enemies.append(AnthonysTurtleChildClass('enemy', enemy_speed, 'red'))
        elif index == 1:
            enemies.append(AnthonysTurtleChildClass('enemy', enemy_speed, 'red'))
        elif index == 2:
            enemies.append(AnthonysTurtleChildClass('enemy', enemy_speed, 'red'))
        elif index == 3:
            enemies.append(AnthonysTurtleChildClass('enemy', enemy_speed, 'red'))
        elif index == 4:
            enemies.append(AnthonysTurtleChildClass('enemy', enemy_speed, 'red'))
        else:
            enemies.append(AnthonysTurtleChildClass('enemy', enemy_speed, 'blue'))
    return enemies, e_number, e_speed


# Create a list of enemies
number_of_enemies = int(t.textinput(wn,"How many enemies do you want at the start?"))
enemy_speed = 5
active_enemies, number_of_enemies, enemy_speed = create_new_enemies(number_of_enemies, enemy_speed)

# Create bullet
bullet = AnthonysTurtleChildClass('bullet', 10, 'yellow')


def call_fire_bullet():
    bullet.fire_bullet(anthony.xcor(), anthony.ycor(), anthony.heading())


# The remainder of the program is event driven based on keyboard inputs
wn.listen()

wn.onkeypress(anthony.up, "Up")
wn.onkeypress(anthony.dn, "Down")
wn.onkeypress(anthony.lft, "Left")
wn.onkeypress(anthony.rt, "Right")
wn.onkeypress(call_fire_bullet, "space")
wn.onkeypress(anthony.rotate_clockwise, "r")
wn.onkeypress(anthony.rotate_counter_clockwise, "l")
# hi
while anthony.lives > 0:
    if len(active_enemies) <= 0:
        active_enemies, number_of_enemies, enemy_speed = create_new_enemies(number_of_enemies, enemy_speed)
    for enemy in active_enemies:
        score_pen.speed(0)
        score_pen.clear()
        score_pen.color('White')
        score_pen.penup()
        score_pen.setposition(-290, 280)
        score_string = f"{players_name} has {anthony.lives} lives left and Score: {score}"
        score_pen.write(score_string, False, align="left", font=("Arial", 14, "normal"))
        score_pen.hideturtle()
        x_start = int(enemy.xcor())
        y_start = int(enemy.ycor())
        enemy.move_enemy()
        x_end = int(enemy.xcor())
        y_end = int(enemy.ycor())
        enemy.path = path(x_start, y_start, x_end, y_end)
        if is_collision(enemy, anthony):
            play_sound('EXPLODE.WAV')
            anthony.lives -= 1
            if anthony.lives <= 0:
                play_again = t.textinput(wn,'Do you want to continue to play (y or n)?')
                if play_again == 'n':
                    time.sleep(5)
                    sys.exit()
                else:
                    anthony.lives = int(t.textinput(wn, "How many lives do you want?"))
                    wn.listen()
            continue
        # Determine if a bullet is active and see if the path of the bullet and the enemy intersect
        if bullet.active:
            if len(enemy.path.intersection(bullet.path)) > 0:
                enemy.hideturtle()
                active_enemies.remove(enemy)
                play_sound('EXPLODE.WAV')
                score = change_score(score, enemy.points)


    # enemy.move_enemy()
    if bullet.active is True:
        bullet.move_bullet()

wn.mainloop()
