import pygame
import sys

# Initialize Pygame
pygame.init()

# Set screen size and caption
screen_size = (600, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Pac-Man')

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
# Define Pac-Man variables
pacman_position = [300, 300]
pacman_speed = 5
pacman_radius = 15

# Define ghost variables
ghost_position = [100, 100]
ghost_speed = 2
ghost_radius = 20

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Move Pac-Man
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pacman_position[0] -= pacman_speed
    elif keys[pygame.K_RIGHT]:
        pacman_position[0] += pacman_speed
    elif keys[pygame.K_UP]:
        pacman_position[1] -= pacman_speed
    elif keys[pygame.K_DOWN]:
        pacman_position[1] += pacman_speed

    # Move ghost
    if ghost_position[0] < pacman_position[0]:
        ghost_position[0] += ghost_speed
    elif ghost_position[0] > pacman_position[0]:
        ghost_position[0] -= ghost_speed
    if ghost_position[1] < pacman_position[1]:
        ghost_position[1] += ghost_speed
    elif ghost_position[1] > pacman_position[1]:
        ghost_position[1] -= ghost_speed

    # Draw background
    screen.fill(BLACK)

    # Draw Pac-Man
    pygame.draw.circle(screen, YELLOW, pacman_position, pacman_radius)

    # Draw ghost
    pygame.draw.circle(screen, RED, ghost_position, ghost_radius)

    # Update display
    pygame.display.update()
