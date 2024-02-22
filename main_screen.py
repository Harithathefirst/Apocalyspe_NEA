#packages/imports
import pygame 
import sys #import sys  #imports system-specific parameters and functions 
from settings import *
import math #access sin and cos
import time
from player import *
from map import *
from floorcasting import *


#initialise pygame
pygame.init()

#create instance of map class
map = Map()
x=600
y=300


run=True
#game runs in this loop
while run:
    #close game condition
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #run=False
            pygame.quit()
            sys.exit(0) # closes the while loop 
    pygame.display.flip() #updates screen every frame
    clock.tick(FPS)#main loop shouldnt run faster than 60 times per second 
    screen.fill(BLACK)
    map.draw_map()
    pygame.draw.circle(screen,GREEN,(x,y),10)


    #draw 2d map representation
    #draw_map()
    #pixels = floorcasting()
    #screen.blit(pixels, (0,0)) #draws the pixels frame onto the screen













































""" class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(RES) #creates display surface and makes it fullscreen by resizing
        self.clock = pygame.time.Clock() #clock object to help make frame rate
        self.new_game()

    def new_game(self):
        self.map= Map(self)
    
    def update(self):
        pygame.display.flip() #updates screen every frame
        self.clock.tick(FPS)

    def draw(self):
        self.screen.fill(BLACK)
        self.map.draw_map()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#run=False
                pygame.quit()
                sys.exit() # closes the while loop 

    
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run() """