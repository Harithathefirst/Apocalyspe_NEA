import pygame 
import sys #import sys  #imports system-specific parameters and functions 
from settings import *
import math #access sin and cos
import time
from player import *
from map import draw_map

#initialise pygame
pygame.init()

run=True
#game runs in this loop
while run:
    #close game condition
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #run=False
            pygame.quit()
            sys.exit(0) # closes the while loop 

    #draw 2d map representation
    draw_map()
    pygame.display.flip()#updates screen every frame
    clock.tick(FPS)#main loop shouldnt run faster than 60 times per second 

    
      
    
#screen.fill(BLACK)
#pygame.draw.circle(screen,RED,(x,y),30)