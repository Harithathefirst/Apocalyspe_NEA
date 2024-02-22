import pygame
from settings import *
import math

""" 
class Player:
    def __init__(self,x,y,speed):
        self.x = x
        self.y = y
        self.speed = 8
    
    def move_forward(self,event,speed):
            if event.key == pygame.K_w:
                x_change = 0
                y_change=-speed """

class Player:
    def __init__(self):
        self.x,self.y = PLAYER_INITIAL_POS 
        self.angle = PLAYER_ANGLE
        self.rotspeed = PLAYER_ROTATION_SPEED
    

    def movement(self):
        sin_A = math.sin(self.angle) #calculates sin of the angle a
        cos_A = math.cos(self.angle)#cos angle a  
        dx,dy = 0,0 #initial coordinates
        speed = PLAYER_SPEED

        keys = pygame.key.get_pressed() #gets the state of all keyboard buttons
        if keys[pygame.K_w]:
                dx += speed*cos_A
                dy += speed*sin_A
        elif keys[pygame.K_a]:
                dx += speed*sin_A
                dy += -(speed*cos_A)
        elif keys[pygame.K_s]:
                dx+= -(speed*cos_A)
                dy+=-(speed*sin_A)
        elif keys[pygame.K_d]:
                dx+= -(speed*sin_A)
                dy+= speed*cos_A

        self.x += dx #adds on moveemnt to initial player y pos
        self.y += dy #adds on movement to initial player x pos

    def draw_player(self):
        #pg.draw.line(surface,colour,start(x,y),end(x,y),width)
        pygame.draw.line(screen,
                         RED,
                         (self.x * 100, self.y * 100),
                         (self.x * 100 + SCREEN_WIDTH * math.cos(self.angle), self.y * 100 + SCREEN_WIDTH * math.sin(self.angle)),2)
        pygame.draw.circle(screen,GREEN,(self.x*100,self.y*100),20)





""" ef movement(event,speed,x_change,y_change):
 #WASD CONTROLS
        if event.type == pygame.KEYDOWN:
            #W - move forards
            if event.key == pygame.K_w:
                x_change = 0
                y_change=-speed
            #A - move to the left
            elif event.key == pygame.K_a:
                x_change=-speed
                y_change=0
            #S - move backwards
            elif event.key == pygame.K_s:
                x_change=0
                y_change=speed
            #D- move to the right
            elif event.key == pygame.K_d:
                x_change=speed
                y_change=0
        elif event.type == pygame.KEYUP:
                 #W - move forards
            if event.key == pygame.K_w:
                x_change = 0
                y_change=0 
            #A - move to the left
            elif event.key == pygame.K_a:
                x_change=0
                y_change=0
            #S - move backwards
            elif event.key == pygame.K_s:
                x_change=0
                y_change=0
            #D- move to the right
            elif event.key == pygame.K_d:
                x_change=0
                y_change=0
            return x_change,y_change
 """

#def add(a,b):
    #return a+b



