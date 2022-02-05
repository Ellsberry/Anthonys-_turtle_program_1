from turtle import Turtle as T
from turtle import Screen
import time
import random
from path import path
import winsound


class AnthonysTurtleChildClass(T):
    """ Objects in this class also have attributes and methods inherited  from Turtle"""
    def __init__(self, o_type, speed, color):
        super().__init__()                        # this creates an instance/turtle object
        if o_type == "player":                      # Build enemy objects
            self.shape("turtle")
            self.setposition(-200, -200)
            self.speed(speed)
            self.color(color)
            self.lives = 3                      # the player starts with 3 lives
            self.penup()
        elif o_type == 'enemy':                    # Build enemy objects
            self.shape("turtle")
            self.speed(speed)
            self.color(color)
            self.path = set()
            self.points = 1                      # At beginning of the game enemies are worth 1 point
            self.penup()
            x = random.randint(-300, 300)
            y = random.randint(-150, 150)
            self.setposition(x, y)
        elif o_type == 'bullet':
            self.shape("triangle")
            self.hideturtle()
            self.speed(speed)
            self.color(color)
            self.active = False
            # self.heading = 0
            self.path = set()
            self.penup()
            self.clear()

    def lft(self):
        if self.xcor() - 20 < -600:
            self.setposition(-600, self.ycor())
        else:
            self.setposition(self.xcor() - 20, self.ycor())

    def rt(self):
        if self.xcor() + 20 > 600:
            self.setposition(600, self.ycor())
        else:
            self.setposition(self.xcor() + 20, self.ycor())

    def up(self):
        if self.ycor() + 20 > 300:
            self.setposition(self.xcor(), 300)
        else:
            self.setposition(self.xcor(), self.ycor() + 20)

    def dn(self):
        if self.ycor() - 20 < -300:
            self.setposition(self.xcor(), -300)
        else:
            self.setposition(self.xcor(), self.ycor() - 20)

    def rotate_clockwise(self):
        self.right(90)

    def rotate_counter_clockwise(self):
        self.left(90)

    # Movement of Enemy
    def move_enemy(self):
        # this randomly rotates an enemy and then moves the enemy a distance between 20 and 100 pixel
        rotate = random.randint(1, 180)
        right_or_left = random.randint(1, 2)
        enemy_distance = random.randint(20, 100)
        if right_or_left == 1:
            self.right(rotate)
        else:
            self.left(rotate)

        self.forward(enemy_distance)
        if self.xcor() > 600:
            self.setposition(600, int(self.ycor()))
        if self.xcor() < -600:
            self.setposition(-600, int(self.ycor()))
        if self.ycor() > 300:
            self.setposition(int(self.xcor()), 300)
        if self.ycor() < -300:
            self.setposition(int(self.xcor()), -300)

    def fire_bullet(self,x_start, y_start, b_heading):
        c_heading = int(b_heading)
        if self.active is True:
            return
        else:
            laser_sound = r"C:\Users\ajh08_idy4tts\Documents\Anthonys-_turtle_program_1\LASER.WAV"
            winsound.PlaySound(laser_sound, winsound.SND_ASYNC)
            self.active = True
            self.setposition(x_start, y_start)
            self.path = set()
            self.setheading(b_heading)
            self.showturtle()
            jump_distance = 400
            if c_heading == 0:
                self.setposition(int(x_start + jump_distance), int(y_start))
            if c_heading == 90:
                self.setposition(int(x_start), int(y_start + jump_distance))
            if c_heading == 180:
                self.setposition(int(x_start - jump_distance), int(y_start))
            if c_heading == 270:
                self.setposition(int(x_start), int(y_start) - jump_distance)
            x_end = int(self.xcor())
            y_end = int(self.ycor())
            self.showturtle()
            self.path = path(x_start, y_start, x_end, y_end)

    def move_bullet(self):
        if self.active is False or self.xcor() >= 600 or self.xcor() <= -600 or self.ycor() >= 300 or self.ycor() <= -300:
            self.active = False
            self.hideturtle()
            self.path = set()
            return
        else:
            self.path = set()
            x_start = int(self.xcor())
            y_start = int(self.ycor())
            jump_distance = 100
            bullet_heading = int(self.heading())
            if bullet_heading == 0:
                self.setposition(int(self.xcor() + jump_distance), int(self.ycor()))
            if bullet_heading == 90:
                self.setposition(int(self.xcor()), int(self.ycor() + jump_distance))
            if bullet_heading == 180:
                self.setposition(int(self.xcor() - jump_distance), int(self.ycor()))
            if bullet_heading == 270:
                self.setposition(int(self.xcor()), int(self.ycor() - jump_distance))
            x_end = int(self.xcor())
            y_end = int(self.ycor())
            self.path = path(x_start, y_start, x_end, y_end)
            if x_end >= 600 or x_end <= -600 or y_end >= 300 or y_end <= -300:
                self.active = False
                self.hideturtle()
                return


# The following code is for testing this child class

if __name__ == "__main__":

    # Setup Screen as wn (short for window)
    wn = Screen()
    wn.bgcolor("black")
    wn.title("Turtle Wars")

    # Create player
    anthony = AnthonysTurtleChildClass("player", int(5), 'white')

    # Create Enemies
    # number_of_enemies = int(input("How many enemies do you want?"))
    number_of_enemies = 5                                            # REMOVE THIS LINE AFTER TESTING
                                                                     # AND UN-COMMENT THE NUMBER OF ENEMIES INPUT LINE
    enemy_speed = 3
    enemies = []                                                         # this is for the list of enemies
    for index in range(number_of_enemies):
        if index == 0:
            enemies.append(AnthonysTurtleChildClass('enemy', enemy_speed, 'blue'))
        elif index == 1:
            enemies.append(AnthonysTurtleChildClass('enemy', enemy_speed, 'green'))
        elif index == 2:
            enemies.append(AnthonysTurtleChildClass('enemy', enemy_speed, 'yellow'))
        elif index == 3:
            enemies.append(AnthonysTurtleChildClass('enemy', enemy_speed, 'orange'))
        elif index == 4:
            enemies.append(AnthonysTurtleChildClass('enemy', enemy_speed, 'grey'))
        else:
            enemies.append(AnthonysTurtleChildClass('enemy', enemy_speed, 'violet'))

    # Create bullet
    # bullet = AnthonysTurtleChildClass('bullet', 0, 'yellow')

    anthony.rotate_clockwise()
    time.sleep(.5)
    anthony.rotate_clockwise()
    time.sleep(.5)
    anthony.rotate_clockwise()
    time.sleep(.5)

    anthony.rotate_counter_clockwise()
    time.sleep(.5)
    anthony.rotate_counter_clockwise()
    time.sleep(.5)
    anthony.rotate_counter_clockwise()
    time.sleep(.5)
    anthony.rotate_counter_clockwise()

    anthony.rt()
    time.sleep(.5)

    anthony.lft()
    time.sleep(.5)
    anthony.lft()
    time.sleep(.5)
    anthony.lft()
    time.sleep(.5)
    anthony.lft()
    time.sleep(.5)
    anthony.lft()
    time.sleep(.5)
    anthony.lft()
    time.sleep(.5)
    anthony.lft()
    time.sleep(.5)
    anthony.lft()
    time.sleep(.5)
    anthony.lft()
    sleep_time = .5
    anthony.lft()

    time.sleep(5)
