#packages/imports
import pygame 
import sys #import sys  #imports system-specific parameters and functions
import os 
import pathlib
from settings import *
import math #access sin and cos
import time
from player import *
from map import *
from main_menu import play_game
from buttons import *


#initialise pygame
pygame.init()

#create instance of classes
map = Map() #map class
player = Player() #player class


#logo = pygame.image.load('title.png')


run=True
#game runs in this loop
#FONT = pygame.font.SysFont('Horta',35)
#text = FONT.render('quit' , True , RED) 

#main game loop
while run:
    #screen.fill(MAIN_PURPLE)
    #screen.blit(logo,(500,500))
    #close game condition
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
            pygame.quit()
            sys.exit(0) # closes the while loop 

    map.draw_map()
    player.moving()
    #player.moving()
    #"C:\Users\bindu\OneDrive - Bright Futures Educational Trust\Alevel\CS NEA\documentcode_git\Apocalyspe_NEA\title.png"
  
    #player.draw_player()
    
    
    screen.blit(player.player,player.rect)
    #screen.fill(BLACK)
    pygame.display.flip() #updates screen every frame
clock.tick(FPS)#main loop shouldnt run faster than 60 times per second 
    
   

    #screen.blit(logo,(100,100))

    


""" class Game:
    def __init__(self):
        self.map = Map()
        self.player = Player()
    
    def check_quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            pygame.quit()
            sys.exit(0) # closes the while loop 
    
    def update(self):
        pygame.display.flip()
    
    def main_game_loop(self):
        for event in pygame.event.get():
            self.map.draw_map()
            self.player.movement()
            self.player.draw_player()



game = Game()

if __name__ == "__main__":
    game.main_game_loop






 """












































    
