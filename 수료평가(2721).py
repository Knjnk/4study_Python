import pygame
import sys

pygame.init()

screen_size = (600, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Pac-Man')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
pacman_position = [300, 300]
pacman_speed = 5
pacman_radius = 15

ghost_position = [100, 100]
ghost_speed = 2
ghost_radius = 20

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pacman_position[0] -= pacman_speed
    elif keys[pygame.K_RIGHT]:
        pacman_position[0] += pacman_speed
    elif keys[pygame.K_UP]:
        pacman_position[1] -= pacman_speed
    elif keys[pygame.K_DOWN]:
        pacman_position[1] += pacman_speed

    if ghost_position[0] < pacman_position[0]:
        ghost_position[0] += ghost_speed
    elif ghost_position[0] > pacman_position[0]:
        ghost_position[0] -= ghost_speed
    if ghost_position[1] < pacman_position[1]:
        ghost_position[1] += ghost_speed
    elif ghost_position[1] > pacman_position[1]:
        ghost_position[1] -= ghost_speed

    screen.fill(BLACK)

    pygame.draw.circle(screen, YELLOW, pacman_position, pacman_radius)

    pygame.draw.circle(screen, RED, ghost_position, ghost_radius)

    pygame.display.update()
