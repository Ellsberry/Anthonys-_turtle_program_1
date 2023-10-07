import turtle

# Create a Blue Turtle screen





# create a list of 4 turtles with different colors
turtles = []
colors = ["red", "green", "yellow", "purple"]








# show screen with turtles
screen.update()

# functions to allow a selection of time of 1, 2, 3, or 4 hours


def hour1():




def hour_x():



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
        turtles[1].goto(-500 + 1 * x ** 3 * 10, 100)
        turtles[2].goto(-500 + 2 * x ** 2 * 10, -100)
        turtles[3].goto(-500 + 4 * x * 10, -300)
        screen.update()


# The remainder of the program is event driven based on keyboard inputs
screen.listen()

screen.onkeypress(hour1, "1")
screen.onkeypress(hour2, "2")
screen.onkeypress(hour3, "3")
screen.onkeypress(hour4, "4")
screen.onkeypress(hour_x, "x")

while True:
    screen.update()
