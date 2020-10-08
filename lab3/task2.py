import pygame
from pygame.draw import *

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 55, 55)
GRAY_CLOUD_1 = (102, 102, 102)
GRAY_CLOUD_2 = (51, 51, 51)
GRAY_UFO_1 = (204, 204, 204)
GRAY_UFO_2 = (153, 153, 153)
BLUE_SKY = (0, 34, 43)
BLUE_SKYLINE = (46, 69, 68)
GREEN_GRASS = (34, 43, 0)
GREEN_ALIEN = (221, 233, 175)
GREEN_LEAF = (136, 170, 0)

FPS = 30
width = 707
height = 1000
screen = pygame.display.set_mode((width, height))

# The arrival of an alien
# sky
rect(screen, BLUE_SKY, (0, 0, width, 0.55*height))
# skyline
fat_skyline = 1
line(screen, BLUE_SKYLINE, (0, 0.55*height), (width, 0.55*height), fat_skyline)
# grass
rect(screen, GREEN_GRASS, (0, 0.55*height + fat_skyline, width,
                           0.45*height - fat_skyline))
# moon
circle(screen, WHITE, (0.6*width, 0.25*height), 100)
# clouds
for i in range(1, 4):
    ellipse(screen, GRAY_CLOUD_1, ((-1)**i*i*50, i*20, width, 0.1*height))
    ellipse(screen, GRAY_CLOUD_1, ((-1)**i*i*110, i*80, width, 0.1*height))
for i in range(1, 4):
    ellipse(screen, GRAY_CLOUD_2, (((-1)**i*i*100, i*100, width, 0.09*height)))
# alien
def alien():
    pass
# ufo
def ufo():
    pass

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
