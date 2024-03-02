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
        self.square = pygame.Surface((50,50))
        self.square.fill(GREEN)
        self.rect = self.square.get_rect()
        self.rect.x = 500
        self.rect.y = 500
    

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

    def move(self,dx,dy):
         speed = PLAYER_SPEED*10
         self.rect.x += dx*speed
         self.rect.y += dy*speed
      

    def moving(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
                self.move(0,-20)
        if keys[pygame.K_a]:
                self.move(-20,0)
        if keys[pygame.K_s]:
                self.move(0,20)              
        if keys[pygame.K_d]:
                self.move(20,0)
        
        #if keys[pygame.K_LEFT]:
              #self.angle -= PLAYER_ROTATION_SPEED * delta_time #rotate to the left
        #if keys[pygame.K_RIGHT]:
              #self.angle += PLAYER_ROTATION_SPEED * delta_time #rotate to the right
        #self.angle %= 2 * math.pi #stores players angle as the result of modding 360

        

    #draws the player and a line from the front of the player
    def draw_player(self):
        #pg.draw.line(surface,colour,start(x,y),end(x,y),width)
        pygame.draw.line(screen,
                         RED,
                         (self.x * 100, self.y * 100),
                         (self.x * 100 + SCREEN_WIDTH * math.cos(self.angle), self.y * 100 + SCREEN_WIDTH * math.sin(self.angle)),2)
        #pygame.draw.circle(screen,GREEN,(self.x*100,self.y*100),15)

    def position_current(self): #players current positiopn on map
          return self.x,self.y
    
    def position_map(self): #returns map tile player is on 
          return int(self.x),int(self.y)
          
    
        
    def check_wall(self,x,y): #takes in x and y coordniates of the player
        if (self.rect.x,self.rect.y) not in m.worldmap:#returns the coordinates of the player if it is not where there is 1 on map - a wall
              return (self.rect.x,self.rect.y)
        

    def collision(self,dx,dy): #takes in the players calculated dx and dy
          if self.check_wall(int(self.rect.x + dx),int(self.rect.y)): #allows movement on the x axis if x coordinate is not at a wall 
                self.rect.x += dx #adds on the calculated dx - can move in x direction
          if self.check_wall(int(self.rect.x),int(self.rect.y + dy)): #allows movement if y coordinate is not at a wall
                self.rect.y += dy #adds on calculated dy -can move in y direction
          
    



          
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

