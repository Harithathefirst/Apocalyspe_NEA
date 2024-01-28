import pygame as pg
import sys

pg.init()

screen = pg.display.set_mode((500,500),pg.RESIZABLE)
FPS = 60
clock = pg.time.Clock()
run=True

obj = pg.Surface((50,50))
obj.fill ((255,255,255))
rect = obj.get_rect()
rect.x = 100
rect.y = 100
speed = 2

def move(dx,dy):
    rect.x += dx * speed
    rect.y += dy * speed

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run=False
            pg.quit()
            sys.exit()
    keys = pg.key.get_pressed()

    if keys[pg.K_d]:
        move(1,0)
    if keys[pg.K_a]:
        move(-1,0) 
    if keys[pg.K_w]:
        move(0,-1)
    if keys[pg.K_s]:
        move(0,1)  

    screen.fill((0,0,0))
    screen.blit(obj,rect)

    pg.display.flip()

clock.tick(FPS)


