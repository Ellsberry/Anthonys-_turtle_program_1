import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 36)  # Font for axis labels

# Create a window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Area Calculation Game")

# Scale factor for positioning and scaling shapes
SCALE_FACTOR = 40


def scale_x(x):
    return WIDTH / 2 + x * SCALE_FACTOR


def scale_y(y):
    return HEIGHT / 2 - y * SCALE_FACTOR


# Define 5 shapes (rectangles, circles, and triangles)
shapes = []
while len(shapes) < 5:
    shape_type = random.choice(["rectangle", "circle", "triangle"])

    if shape_type == "rectangle":
        width = random.randint(2, 8)
        height = random.randint(2, 8)
        shapes.append(("rectangle", width, height))
    elif shape_type == "circle":
        radius = random.randint(2, 4)
        shapes.append(("circle", 0, 0, radius))
    else:
        # For triangles
        base = random.randint(2, 8)
        height = random.randint(2, 8)
        shapes.append(("triangle", base, height))


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
