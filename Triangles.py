import pygame
import random
import math
import time


print("In geometry, congruent means identical in shape and size.\n",
      "Congruence can be applied to line segments,"
      " angles, and figures.")

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
FONT = pygame.font.Font(None, 36)  # Font for axis labels

# Create a window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TRIANGLES")
window.fill(WHITE)

# Scale factor for positioning and scaling shapes
SCALE_FACTOR = 40


def scale_x(x):
    return WIDTH / 2 + x * SCALE_FACTOR


def scale_y(y):
    return HEIGHT / 2 - y * SCALE_FACTOR

# Draw the x and y axes
pygame.draw.line(window, BLACK, (0, HEIGHT / 2), (WIDTH, HEIGHT / 2), 2)
pygame.draw.line(window, BLACK, (WIDTH / 2, 0), (WIDTH / 2, HEIGHT), 2)

# Add numbers to the x and y axes
for x in range(-10, 10):
    text = FONT.render(str(x), True, BLACK)
    text_rect = text.get_rect()
    text_rect.centerx = scale_x(x)
    text_rect.centery = HEIGHT // 2
    window.blit(text, text_rect)

for y in range(-10, 10):
    text = FONT.render(str(y), True, BLACK)
    text_rect = text.get_rect()
    text_rect.centerx = WIDTH // 2
    text_rect.centery = scale_y(y)
    window.blit(text, text_rect)

# Triangle 1
base, height, width = 3, 4, 5
point_1 = (400 - ((base + 1) * SCALE_FACTOR), 400)       # point is on x axis at (-4, 0)
point_2 = (400 - (1 * SCALE_FACTOR), 400)                               # point is on x axis at (-1, 0)
point_3 = (400 - (1 * SCALE_FACTOR), 400 + (-height * SCALE_FACTOR))     # point is on y axis at (-1, 4)

points = [point_1, point_2, point_3]
pygame.draw.polygon(window, RED, points, 2)


# Triangle 2 mirrors Triangle 1
base, height, width = 3, 4, 5
point_1 = (400 - ((base + 1) * SCALE_FACTOR), 400)       # point is on x axis at (-4, 0)
point_2 = (400 - (1 * SCALE_FACTOR), 400)                               # point is on x axis at (-1, 0)
point_3 = (400 - (1 * SCALE_FACTOR), 400 + (height * SCALE_FACTOR))     # point is on y axis at (-1, 4)

points = [point_1, point_2, point_3]
pygame.draw.polygon(window, GREEN, points, 2)

# Triangle 3 is Triangle 1 translated
base, height, width = 3, 4, 5
point_1 = (400 - ((base + 1) * SCALE_FACTOR) + 200, 400 - 200)
point_2 = (400 - (1 * SCALE_FACTOR) + 200, 400 - 200)
point_3 = (400 - (1 * SCALE_FACTOR) + 200, 400 - 200 + (-height * SCALE_FACTOR))

points = [point_1, point_2, point_3]
pygame.draw.polygon(window, BLUE, points, 2)

# Triangle 4 translates  Triangle 1
base, height, width = 6, 8, 10
point_1 = (400 - ((base + 1) * SCALE_FACTOR), 400)
point_2 = (400 - (1 * SCALE_FACTOR), 400)
point_3 = (400 - (1 * SCALE_FACTOR), 400 + (-height * SCALE_FACTOR))

points = [point_1, point_2, point_3]
pygame.draw.polygon(window, YELLOW, points, 2)

# Triangle 5 translates  Triangle 1
base, height, width = 3, 4, 5
point_1 = (500, 400)
point_2 = (580, 490)
point_3 = (448, 610)

points = [point_1, point_2, point_3]
pygame.draw.polygon(window, BLACK, points, 2)


pygame.display.flip()


# calculate the angles  of the 3, 4, 5 triangle using the sine and cosine functions
a = 3
b = 4
c = 5
angle_A = math.degrees(math.asin(a / c))
angle_B = math.degrees(math.asin(b / c))
angle_C = 180 - angle_A - angle_B
print(f'the angles for a 3 4 5 triangle are:  angle_A = {angle_A}  angle_B = {angle_B}  angle_C = {angle_C}')

# calculate the angles  of the 6, 8, 10 triangle using the sine and cosine functions
a = 6
b = 8
c = 10
angle_A = math.degrees(math.asin(a / c))
angle_B = math.degrees(math.asin(b / c))
angle_C = 180 - angle_A - angle_B
print(f'the angles for a 6 8 10  triangle are:  angle_A = {angle_A}  angle_B = {angle_B}  angle_C = {angle_C}')



time.sleep(100)
