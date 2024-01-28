import pygame 
import sys #import sys  #imports system-specific parameters and functions 
from settings import *
import math #access sin and cos
import time
#from player import movement

pygame.init()
screen = pygame.display.set_mode(RES) #creates display surface and makes it fullscreen by resizing
pygame.display.set_caption("Apocalypse") #sets title on the window
clock = pygame.time.Clock() #clock object to help make frame rate

#circle starting coordinates
x=200
y=200

run=True
#game runs in this loop
while run:
    #close game condition
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            run=False
            pygame.quit()
            sys.exit() # closes the while loop 
    ##circle to check what fullscreen does to objects
    pygame.draw.circle(screen,RED,(x,y),30)
    pygame.display.flip() #updates the surface every frame
    #clock.tick(60) #while loop shoudlnt run faster than 60 times per second

"""
#x_change = 0
#y_change = 0

#speed = 8

#run=True
#game runs in this loop
while run:
    #close game condition
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
            pygame.quit()
            sys.exit() # closes the while loop 
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

    #add on the change coordinates to og coordinates
    x += x_change
    y += y_change
 """
    
  
""" 

#class Main_Game:
    def __init__(self):
        #attribute of everything in the class
        #initiates pygame
        pygame.init()
        self.screen = pygame.display.set_mode(RES), pygame.RESIZABLE #creates display surface and makes it fullscreen by resizing
        self.clock = pygame.time.Clock() #clock object to help make frame rate
        self.name = pygame.display.set_caption("Apocalypse") #sets title on the window
        #return self.clock

    #def update(self):
        pygame.display.flip() #updates display surface - the whole screen is updated
        self.clock.tick(FPS)  #the while loop should not run faster than 60 times per second

    #def draw(self):
        self.screen.fill(BLACK)#makes screen black at each iteration
         """          
    
    



