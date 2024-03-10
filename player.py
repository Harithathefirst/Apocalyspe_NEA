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
        self.speed = 0.05
        self.x_change = 0
        self.y_change = 0
        #self.square = pygame.Surface((50,50))
        #self.square.fill(GREEN)
        #self.rect = self.square.get_rect()
        #self.rect.x,self.rect.y = PLAYER_INITIAL_POS
    

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
        self.angle %= 2 * math.pi #players angle should remain between 0-360

    @property
    def position_current(self): #players current positiopn on map
          return self.x,self.y
    @property   
    def position_map(self): #returns map tile player is on 
          return int(self.x),int(self.y)


        

    #def move(self,dx,dy):
         #speed = PLAYER_SPEED*10
         #self.rect.x += dx*speed
         #self.rect.y += dy*speed

         #self.collision(dx,dy)
      

    
    def movement1(self):
        self.x_change = 0
        self.y_change = 0
        keys = pygame.key.get_pressed()
                    #W - move forards
        if keys[pygame.K_w]:
                    self.y_change=-self.speed
            #A - move to the left
        elif keys[pygame.K_a]:
                    self.x_change=-self.speed
            #S - move backwards
        elif keys[pygame.K_s]:
                    self.y_change=self.speed
            #D- move to the right
        elif keys[pygame.K_d]:
                    self.x_change=self.speed
         

                #rotation will be with mouse 
        if keys[pygame.K_LEFT]:
            self.angle -= PLAYER_ROTATION_SPEED * delta_time #rotate to the left
        if keys[pygame.K_RIGHT]:
            self.angle += PLAYER_ROTATION_SPEED * delta_time #rotate to the right
        self.angle %= 2 * math.pi #stores players new angle as the result of modding 360

        
               

        self.collision1(self.x,self.y)

       # return self.angle,self.x_change,self.y_change
    
    #def moving(self):
       # self.x += self.x_change
       # self.y += self.y_change


    
                         
                  
           

        
#document error of player wont stop moving
 #collision       


    #draws the player and a line from the front of the player
    def draw_player(self):
      #pygame.draw.line(surface,colour,start(x,y),end(x,y),width)
      pygame.draw.line(screen,
                        RED,
                        (self.x * 100, self.y * 100),
                        (self.x * 100 +  math.cos(self.angle), self.y * 100 + math.sin(self.angle)),2)
      pygame.draw.circle(screen,GREEN,(self.x*100,self.y*100),15)

  
          
  
    def check_wall(self,x,y): #takes in x and y coordniates of the player
        if (x,y) not in m.worldmap:#returns the coordinates of the player if it is not where there is 1 on map - a wall
              return (x,y)
        

    def collision(self,dx,dy): #takes in the players calculated dx and dy
          if self.check_wall(int(self.x + dx),int(self.y)): #allows movement on the x axis if x coordinate is not at a wall 
                self.x += dx #adds on the calculated dx - can move in x direction
          if self.check_wall(int(self.x),int(self.y + dy)): #allows movement if y coordinate is not at a wall
                self.y += dy #adds on calculated dy -can move in y direction

    def collision1(self,x,y): #takes in the players calculated dx and dy 
      if self.check_wall(int(self.x + self.x_change),int(self.y)): #allows movement on the x axis if x coordinate is not at a wall 
            self.x += self.x_change #adds on the calculated dx - can move in x direction
      if self.check_wall(int(self.x),int(self.y + self.y_change)): #allows movement if y coordinate is not at a wall
            self.y += self.y_change #adds on calculated dy -can move in y direction

      
          


          
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
          
"""  
def moving(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
                self.move(0,-10)
        if keys[pygame.K_a]:
                self.move(-10,0)
        if keys[pygame.K_s]:
                self.move(0,10)              
        if keys[pygame.K_d]:
                self.move(10,0)
        
        #if keys[pygame.K_LEFT]:
              #self.angle -= PLAYER_ROTATION_SPEED * delta_time #rotate to the left
        #if keys[pygame.K_RIGHT]:
              #self.angle += PLAYER_ROTATION_SPEED * delta_time #rotate to the right
        #self.angle %= 2 * math.pi #stores players angle as the result of modding 360    """   
      



