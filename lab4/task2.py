import pygame
from pygame.draw import *
from pygame import gfxdraw
from math import *

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

FPS = 30
thickness_skyline = 1
width, height = 800, 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('I come in peace')


def draw_sky(x, y, w, h):
    '''Здесь и ниже:
       x, y - координаты левого верхнего угла рисуемого объекта;
       w, h - ширина и высота рисуемого объекта.
    '''
    rect(screen, BLUE_SKY, (x, y, w, h))


def draw_skyline(x1, y1, x2, y2):
    '''x1, y1 - координаты левой границы линии;
       x2, y2 - координаты правой границы линии.
    '''
    line(screen, BLUE_SKYLINE, (x1, y1), (x2, y2), thickness_skyline)


def draw_floor(x, y, w, h):
    rect(screen, GREEN_GRASS, (x, y+thickness_skyline, w, h-thickness_skyline))


def draw_moon(x, y, r):
    '''x, y -  координаты центра объекта;
       r - радиус объекта.
    '''
    circle(screen, WHITE, (x, y), r)


def draw_clouds(w, h):
    i = 0
    for i in range(1, 4):
        x1, y1 = (-1)**i * i * width/14, i * height/50
        x2, y2 = (-1)**i * i * width/6.4, i * height/12.5
        ellipse(screen, GRAY_CLOUD_1, (x1, y1, w, h))
        ellipse(screen, GRAY_CLOUD_1, (x2, y2, w, h))
    for i in range(1, 4):
        x3, y3 = (-1)**i * i * width/7, i * height/9.1
        ellipse(screen, GRAY_CLOUD_2, (x3, y3, w, h))


def draw_alien(x, y, w, h):
    # head
    for ang in range(-45, 40, 10):
        ang = ang * pi/180
        # координаты центра головы
        x0 = x + 0.01*w
        y0 = y + h/5 + (h/3 - h/5)/2
        # вращение треугольника вокруг точки (x0, y0)
        x1 = int(x0 + (x-0.24*w-x0)*cos(ang) - (y+h/5-y0)*sin(ang))
        y1 = int(y0 + (y+h/5-y0)*cos(ang) + (x-0.24*w-x0)*sin(ang))
        x2 = int(x0 + (x+0.26*w-x0)*cos(ang) - (y+h/5-y0)*sin(ang))
        y2 = int(y0 + (y+h/5-y0)*cos(ang) + (x+0.26*w-x0)*sin(ang))
        x3 = int(x0 + (x+0.01*w-x0)*cos(ang) - (y+h/3-y0)*sin(ang))
        y3 = int(y0 + (y+h/3-y0)*cos(ang) + (x+0.01*w-x0)*sin(ang))
        gfxdraw.filled_trigon(screen, x1, y1, x2, y2, x3, y3, GREEN_ALIEN)
    # body
    ellipse(screen, GREEN_ALIEN, (x-w/10, y+h/3.2, w/4, h/3.5))
    # hands
    ellipse(screen, GREEN_ALIEN, (x+w/10, y+h/3, w/7, h/14))
    ellipse(screen, GREEN_ALIEN, (x+w/6, y+h/2.7, w/7, h/20))
    ellipse(screen, GREEN_ALIEN, (x+w/3.3, y+h/2.5, w/6, h/24))
    
    ellipse(screen, GREEN_ALIEN, (x-w/6, y+h/3, w/7, h/14))
    ellipse(screen, GREEN_ALIEN, (x-w/4.5, y+h/2.6, w/9, h/20))
    ellipse(screen, GREEN_ALIEN, (x-w/4, y+h/2.3, w/14, h/22))
    # legs
    ellipse(screen, GREEN_ALIEN, (x+w/20, y+h/1.9, w/6.5, h/9))
    ellipse(screen, GREEN_ALIEN, (x+w/9, y+h/1.65, w/9, h/8))
    ellipse(screen, GREEN_ALIEN, (x+w/5.3, y+h/1.45, w/7, h/14))

    ellipse(screen, GREEN_ALIEN, (x-w/6, y+h/1.9-h/22, w/6.5, h/9))
    ellipse(screen, GREEN_ALIEN, (x-w/5, y+h/1.65-h/22, w/9, h/8))
    ellipse(screen, GREEN_ALIEN, (x-w/3.25, y+h/1.45-h/22, w/7, h/14))
    # eyes
    circle(screen, BLACK, (x+x/20, y+h/4.1), h/32)
    circle(screen, WHITE, (x+x/18, y+h/4), h/90)
    
    circle(screen, BLACK, (x-x/35, y+h/4.3), h/25)
    circle(screen, WHITE, (x-x/45, y+h/4.2), h/90)
    # apple
    circle(screen, RED, (x+w/2, y+h/2.7), 0.05*h)
    line(screen, BLACK, (x+w/2.05, y+h/3), (x+w/1.9, y+h/3.5), 2)
    polygon(screen, GREEN_LEAF, [(x+w/2, y+h/3.2), (x+w/2, y+h/3.35),
            (x+w/2.1, y+h/3.7), (x+w/2.1, y+h/3.5), (x+w/2, y+h/3.2)])



def draw_ufo(x, y, w, h, sc):
    '''
       sc - поверхность, на которой отрисовывается поверхность со светом.
    '''
    # light
    surface_light = pygame.Surface((w, h*2.5), pygame.SRCALPHA)
    surface_light.fill(SURFACE_COLOR)
    polygon(surface_light, LIGHT_COLOR,
            [(w/2, 0), (w, h*2.5), (w*0.05, h*2.5), (w/2, 0)])
    sc.blit(surface_light, (x, y))
    # plate
    ellipse(screen, GRAY_UFO_2, (x, y, w, h))
    ellipse(screen, GRAY_UFO_1, (x+w*0.15, y-h/20, int(w*0.7), int(h*0.7)))
    n_portholes = 6
    for i in range(n_portholes//2):
        ellipse(screen, WHITE, (x+w*0.03+i*w/6, y+h/2.2+i*h/7, w/7, h/7))
        ellipse(screen, WHITE, (x+w*0.83-i*w/7, y+h/2.2+i*h/7, w/7, h/7))


def main():
    draw_sky(0, 0, width, 0.55*height)
    draw_skyline(0, 0.55*height, width, 0.55*height)
    draw_floor(0, 0.55*height, width, 0.45*height)
    draw_moon(0.6*width, 0.25*height, 0.1*height)
    draw_clouds(width, 0.1*height)
    draw_alien(int(0.7*width), int(0.55*height), int(0.25*width)*1.2,
               int(0.33*height)*1.2)
    draw_ufo(int(0.008*height), int(0.4*height), int(0.35*width),
             int(0.1*height), screen)
    
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
