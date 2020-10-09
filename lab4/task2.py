import pygame
from pygame.draw import *

pygame.init()

SURFACE_COLOR = (0, 0, 0, 0)
LIGHT_COLOR = (255, 255, 255, 50)
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

global thickness_skyline, width, height

FPS = 30
width = 707
height = 1000
screen = pygame.display.set_mode((width, height))

thickness_skyline = 1
buff_x = int(width/70)

def draw_sky():
    rect(screen, BLUE_SKY, (0, 0, width, 0.55*height))

def draw_skyline():
    line(screen, BLUE_SKYLINE, (0, 0.55*height), (width, 0.55*height),
         thickness_skyline)

def draw_floor():
    rect(screen, GREEN_GRASS, (0, 0.55*height + thickness_skyline, width,
                           0.45*height - thickness_skyline))

def draw_moon():
    circle(screen, WHITE, (0.6*width, 0.25*height), 100)


def draw_clouds():
    for i in range(1, 4):
        ellipse(screen, GRAY_CLOUD_1, ((-1)**i*i*50, i*20, width, 0.1*height))
        ellipse(screen, GRAY_CLOUD_1, ((-1)**i*i*110, i*80, width, 0.1*height))
    for i in range(1, 4):
        ellipse(screen, GRAY_CLOUD_2, (((-1)**i*i*100, i*110,
                width, 0.09*height)))

def alien():
    pass

def ufo(x, y, w, h, sc):
    #light
    surface_light = pygame.Surface((w, h*2.5), pygame.SRCALPHA)
    surface_light.fill(SURFACE_COLOR)
    polygon(surface_light, LIGHT_COLOR,
            [(w/2, 0), (w, h*2.5), (w*0.05, h*2.5), (w/2, 0)])
    sc.blit(surface_light, (x, y))
    #plate
    ellipse(screen, GRAY_UFO_2, (x, y, w, h))
    ellipse(screen, GRAY_UFO_1, (x+w*0.15, y-h/20, int(w*0.7), int(h*0.7)))
    n_portholes = 6
    for i in range(n_portholes//2):
        ellipse(screen, WHITE, (x+w*0.03+i*w/6, y+h/2.2+i*h/7, w/7, h/7))
        ellipse(screen, WHITE, (x+w*0.83-i*w/7, y+h/2.2+i*h/7, w/7, h/7))

def main():
    draw_sky()
    draw_skyline()
    draw_floor()
    draw_moon()
    draw_clouds()
    ufo(int(0.008*height), int(0.4*height), int(0.35*width), int(0.1*height),
            screen)
    
    pygame.display.update()
    clock = pygame.time.Clock()

    finished = False
    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

    pygame.quit()

main()
