import pygame 
import sys #import sys  #imports system-specific parameters and functions 
from settings import *
import math #access sin and cos
import time
from player import *

pygame.init()
screen = pygame.display.set_mode(RES) #creates display surface and makes it fullscreen by resizing
pygame.display.set_caption("Apocalypse") #sets title on the window
clock = pygame.time.Clock() #clock object to help make frame rate

""" #circle starting coordinates
x=200
y=200
x_change = 0
y_change = 0
speed = 8 """


run=True
#game runs in this loop
while run:
    #pygame.draw.rect(screen,BLUE, pygame.Rect(500, 500,75,75)) 
    pygame.draw.rect(screen,RED, pygame.Rect(100, 100, 50, 50)) 
    pygame.draw.rect(screen,GREEN, pygame.Rect(500, 500, 100, 300)) 
    #close game condition
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
            pygame.quit()
            sys.exit() # closes the while loop 

        #movement(event,speed,x_change,y_change)
        #add on the change coordinates to og coordinates
        #x += x_change
        #y += y_change
        #print(x,y)
        


    #screen.fill(BLACK)
    #pygame.draw.circle(screen,RED,(x,y),30)
    pygame.display.flip()#updates screen every frame
    clock.tick(FPS)#main loop shouldnt run faster than 60 times per second  
 
    
 
#pygame.display.flip()

""" class Main_Game:
    def __init__(self):
        #attribute of everything in the class
        #initiates pygame
        pygame.init()
        self.screen = pygame.display.set_mode(RES), pygame.RESIZABLE #creates display surface and makes it fullscreen by resizing
        self.clock = pygame.time.Clock() #clock object to help make frame rate
        self.name = pygame.display.set_caption("Apocalypse") #sets title on the window

    def update(self):
        pygame.display.flip() #updates display surface - the whole screen is updated
        self.clock.tick(FPS)  #the while loop should not run faster than 60 times per second

    def draw(self):
        self.screen.fill(BLACK)#makes screen black at each iteration

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                pygame.quit()
                sys.exit() # closes the while loop 
     """



""" a=5
b=2
c= add(a,b)
print(c) """
        
    
             
    
    



