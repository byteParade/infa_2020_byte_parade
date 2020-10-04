import pygame
from pygame.draw import *

pygame.init()

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GRAY = (217, 217, 217)

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill(GRAY)

# Angry smile
# head
circle(screen, YELLOW, (200, 200), 150)
# eyes
circle(screen, RED, (125, 150), 30)
circle(screen, BLACK, (125, 150), 10)
circle(screen, RED, (275, 150), 35)
circle(screen, BLACK, (275, 150), 10)
# mouth
line(screen, BLACK, (275, 300), (125, 300), 20)
# eyebrows
line(screen, BLACK, (50, 65), (155, 127), 12)
line(screen, BLACK, (240, 123), (340, 65), 12)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
