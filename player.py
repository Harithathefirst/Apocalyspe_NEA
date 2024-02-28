import pygame
from settings import *
import math
from map import *
import sys

m = Map()

class Player:
    def __init__(self):
        self.x,self.y = PLAYER_INITIAL_POS 
        self.angle = PLAYER_ANGLE
        self.rotspeed = PLAYER_ROTATION_SPEED
    

    def movement(self):
        sin_A = math.sin(self.angle) #calculates sin of the angle a
        cos_A = math.cos(self.angle)#cos angle a  
        dx,dy = 0,0 #initial coordinates
        speed = PLAYER_SPEED * delta_time #speed of the player independent of the frame rate

        keys = pygame.key.get_pressed() #gets the state of all keyboard buttons
        if keys[pygame.K_w]:
                #move in the forward direction
                dx += speed*cos_A
                dy += speed*sin_A
        elif keys[pygame.K_a]:
                #move in the left direction
                dx += speed*sin_A
                dy += -(speed*cos_A)
        elif keys[pygame.K_s]:
                #move in the backward direction
                dx+= -(speed*cos_A)
                dy+=-(speed*sin_A)
        elif keys[pygame.K_d]:
                #move in the right direction
                dx+= -(speed*sin_A)
                dy+= speed*cos_A

        #self.x += dx #adds on moveemnt to initial player y pos
        #self.y += dy #adds on movement to initial player x pos

        self.collision(dx,dy)
 
        #rotation will be with mouse 
        if keys[pygame.K_LEFT]:
              self.angle -= PLAYER_ROTATION_SPEED * delta_time #rotate to the left
        if keys[pygame.K_RIGHT]:
              self.angle += PLAYER_ROTATION_SPEED * delta_time #rotate to the right
        self.angle %= 2 * math.pi #stores players angle as the result of modding 360

    #draws the player and a line from the front of the player
    def draw_player(self):
        #pg.draw.line(surface,colour,start(x,y),end(x,y),width)
        pygame.draw.line(screen,
                         RED,
                         (self.x * 100, self.y * 100),
                         (self.x * 100 + SCREEN_WIDTH * math.cos(self.angle), self.y * 100 + SCREEN_WIDTH * math.sin(self.angle)),2)
        pygame.draw.circle(screen,GREEN,(self.x*100,self.y*100),15)
        
    def check_wall(self,x,y):
        return (x,y) not in m.worldmap

    def collision(self,dx,dy):
          if self.check_wall(int(self.x + dx),int(self.y)):
                self.x += dx
          if self.check_wall(int(self.x),int(self.y + dy)):
                self.y += dy
          
    

          
"""           
m = Map()

while True:
    for event in pygame.event.get():
          if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    m.draw_map()
    pygame.display.flip()
     """
          
 
      
      


""" def movement(speed,x,y,x_change,y_change):
    for event in pygame.event.get:
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
            return x_change,y_change  """

