import pygame
import random
import math
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 36)  # Font for axis labels

# Create a window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Triangles")

# Scale factor for positioning and scaling shapes
SCALE_FACTOR = 40


def scale_x(x):
    return WIDTH / 2 + x * SCALE_FACTOR


def scale_y(y):
    return HEIGHT / 2 - y * SCALE_FACTOR

window.fill(WHITE)

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

shapes = []
# Define 5 triangles 4 congruent and 1 similar
base, height = 4, 5
points = [
    (400 - (base * SCALE_FACTOR), 400),
    (400, 400),
    (400, 400 - height * SCALE_FACTOR)
]
pygame.draw.polygon(window, WHITE, points, 2)
pygame.display.flip()

time.sleep(5)

"""


while len(shapes) < 5:
    # For triangles
    base = random.randint(2, 8)
    height = random.randint(2, 8)
    shapes.append(("triangle", base, height))

shapes = []

# Game loop
running = True
shape_index = 0

while running and shape_index < len(shapes):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(WHITE)

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

    # Draw the current shape as an outline
    current_shape = shapes[shape_index]
    if current_shape[0] == "rectangle":
        width = int(current_shape[1])
        height = int(current_shape[2])
        # print(f"width = {width}  and height = {height}")
        pygame.draw.rect(window, BLACK, (400 - (width / 2 * SCALE_FACTOR), 400 - (height / 2 * SCALE_FACTOR),
                                         width * SCALE_FACTOR, height * SCALE_FACTOR), 2)
        area = width * height
    elif current_shape[0] == "circle":
        radius = int(current_shape[3])
        # print(f"radius = {radius}  and radius squared = {radius ** 2}")
        area = 3.14 * (radius ** 2)
        pygame.draw.circle(window, BLACK, (400, 400), radius * SCALE_FACTOR, 2)
    elif current_shape[0] == "sine wave":
        # frequency = 2
        # amplitude = 80
        # offset_y = 400
        # num_points = WIDTH
        # for i in range(num_points):
        #     x = i / num_points * 2 * math.pi
        #     y1 = (amplitude * math.sin(x * frequency)) + offset_y / 3
        #     y2 = (amplitude / 2 * math.sin(x * frequency * 2)) + offset_y / 3
        #     y3 = (amplitude / 4 * math.sin(x * frequency * 4)) + offset_y / 3
        #     y = y1 + y2 + y3
        #     print(f"x = {x}     y = {y - offset_y}")
        #     if i > 0:
        #         pygame.draw.aaline(window, (0, 0, 0), prev_pt, (i, y))
        #     prev_pt = i, y
        # frequency = 2
        # amplitude = 40
        # offset_y = 400
        # num_points = WIDTH
        # for i in range(num_points):
        #     x = i / num_points * 2 * math.pi
        #     y = (amplitude * math.sin(x * frequency * 2)) + offset_y * 1.5
        #     print(f"x = {x}     y = {y - offset_y}")
        #     if i > 0:
        #         pygame.draw.aaline(window, (0, 0, 0), prev_pt, (i, y))
        #     prev_pt = i, y
        frequency = 2
        amplitude = 40
        offset_y = 400
        num_points = WIDTH
        for i in range(num_points):
            x = i / num_points * 2 * math.pi
            y1 = (amplitude * math.sin(x * frequency)) + offset_y / 2
            y2 = (amplitude * math.sin(x * frequency * 2)) + offset_y / 2
            y3 = (amplitude / 4 * math.sin(x * frequency * 4)) + offset_y / 6
            y4 = (amplitude * math.cos(x * frequency)) + offset_y / 6
            y5 = (amplitude / 2 * math.cos(x * frequency * 2)) + offset_y / 6
            y6 = (amplitude / 4 * math.cos(x * frequency * 4)) + offset_y / 6
            y = y1 + y2
            print(f"x = {x}     y = {y - offset_y}")
            if i > 0:
                pygame.draw.aaline(window, (0, 0, 0), prev_pt, (i, y))
            prev_pt = i, y

    elif current_shape[0] == "triangle":
        base, height = int(current_shape[1]), int(current_shape[2])
        # print(f'base = {base}  and height = {height}')
        area = (1/2) * base * height
        points = [
            (400 - (base / 2 * SCALE_FACTOR), 400),
            (400 + (base / 2 * SCALE_FACTOR), 400),
            (400, 400 - height * SCALE_FACTOR)
        ]
        pygame.draw.polygon(window, BLACK, points, 2)

    pygame.display.flip()

    # Ask the player to input the area of the current shape
    player_input = input(f"Enter the area of the {current_shape[0]}: ")

    try:
        player_area = float(player_input)

        if abs(player_area - area) <= 1:
            print("Correct!")
        else:
            print(f"Sorry, the correct area is {area:.2f}")
        shape_index += 1
    except ValueError:
        print("Invalid input. Please enter a number.")

# Clean up
pygame.quit()
"""