import turtle
from turtle import Screen
import time
# Create a Blue Turtle screen
wn = Screen()
wn.bgcolor('blue')
wn.title("Blue Turtle Screen")
wn.setup(1000, 1000)


# create a list of 4 turtles with different colors
turtles = []
colors = ["red", "green", "yellow", "purple"]
for i in range(len(colors)):
    turtles.append(turtle.Turtle())
    turtles[i].shape('turtle')
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].goto(-500, 300 - i * 200)
    turtles[i].showturtle()

# show screen with turtles
wn.update()

# functions to allow a selection of time of 1, 2, 3, or 4 hours


def hour1():
    hours = 1
    race(hours)


def hour2():
    hours = 2
    race(hours)


def hour3():
    hours = 3
    race(hours)


def hour4():
    hours = 4
    race(hours)


def hour_x():
    turtle.bye()


def race(hours):
    # show the turtles as they move across the screen
    # Turtle 1 moves at x to the power of 4
    # Turtle 2 moves at 2 * x to the power of 3
    # Turtle 3 moves at 3 * x to the power of 2
    # Turtle 4 moves at 4 * x to the power of 1
    race_time = hours * 10

    for i in range(race_time):
        x = i / 10
        turtles[0].goto(-500 + x ** 4 * 10, 300)
        turtles[1].goto(-500 + 2 * x ** 3 * 10, 100)
        turtles[2].goto(-500 + 3 * x ** 2 * 10, -100)
        turtles[3].goto(-500 + 4 * x * 10, -300)
        wn.update()


# The remainder of the program is event driven based on keyboard inputs
wn.listen()

wn.onkeypress(hour1, "1")
wn.onkeypress(hour2, "2")
wn.onkeypress(hour3, "3")
wn.onkeypress(hour4, "4")
wn.onkeypress(hour_x, "x")

while True:
    wn.update()
