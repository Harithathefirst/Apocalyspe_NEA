#packages/imports
import pygame 
import sys #import sys  #imports system-specific parameters and functions 
from settings import *
import math #access sin and cos
import time
from player import *
from map import *
from main_menu import play_game


#initialise pygame
pygame.init()

#create instance of classes
map = Map() #map class
player = Player() #player class



""" run=True
#game runs in this loop
#FONT = pygame.font.SysFont('Horta',35)
#text = FONT.render('quit' , True , RED) 

#main game loop
while run:
    #play_game()
    #close game condition
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
            pygame.quit()
            sys.exit(0) # closes the while loop 
    pygame.display.flip() #updates screen every frame
    clock.tick(FPS)#main loop shouldnt run faster than 60 times per second 
    screen.fill(BLACK)
    map.draw_map()
    player.movement()
    player.draw_player() """
    


class Game:
    def __init__(self):
        self.map = Map()
        self.player = Player()
    
    def check_quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            pygame.quit()
            sys.exit(0) # closes the while loop 
        pygame.display.flip()
        clock.tick(FPS)
        screen.fill(BLACK)

        
    
    def main_game_loop(self):
        for event in pygame.event.get():
            self.check_quit()
            self.map.draw_map()
            self.player.movement()
            self.player.draw_player()
 



game = Game()

while __name__ == "__main__":
    game.main_game_loop()



















































    
