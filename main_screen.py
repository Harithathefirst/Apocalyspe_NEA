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
from raycasting import *


#initialise pygame
#pygame.init()


#create instance of classes
map = Map() #map class
player = Player() #player class

#filepath = pathlib.Path(__file__).resolve().parent / 'title.png'
#logo = pygame.image.load(filepath)
##logo = pygame.transform.scale_by(logo,2) 
#gunfilepath = pathlib.Path(__file__).resolve().parent / 'title_gun.png'

#gun = pygame.image.load('title_gun.png')


run=True
#game runs in this loop
#FONT = pygame.font.SysFont('Horta',35)
#text = FONT.render('quit' , True , RED) 

#main game loop
while run:
    #screen.fill(MAIN_PURPLE)
    #screen.blit(logo,(SCREEN_WIDTH/2 /10 ,0))
    #screen.blit(gun,SCREEN_WIDTH/2)
    #close game condition
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
            pygame.quit()
            sys.exit(0) # closes the while loop 
            
    pygame.display.flip() #updates screen every frame
    screen.fill(BLACK)
    map.draw_map()
    player.draw_player()
    player.movement()
    player.raycast()
    
    #print(raycast())
    #print(player.x,player.y)
    #print(player.movement())
    #player.stop_moving()
    #player.moving()
    #player.moving()
    #screen.blit()
    #raycast()
    clock.tick(FPS)#main loop shouldnt run faster than 60 times per second 
    
   
 
    #screen.blit(logo,(100,100))
  
    #player.moving()
    #"C:\Users\bindu\OneDrive - Bright Futures Educational Trust\Alevel\CS NEA\documentcode_git\Apocalyspe_NEA\title.png"
  
    
    


""" class Game:
    def __init__(self):
    pygame.init()
        self.map = Map()
        self.player = Player()
        self.clock = clock
    
    def check_quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            pygame.quit()
            sys.exit(0) # closes the while loop 
    
    def update(self):
        pygame.display.flip()
        self.clock.tick(FPS)
    
    def main_game_loop(self):
        for event in pygame.event.get():
            self.map.draw_map()
            self.player.movement1()
            self.player.draw_player()
            raycast()


game = Game()
run = True
while run == True:
    if __name__ == "__main__":
        game.main_game_loop() """
    #run == False


""" class Game:
    def __init__(self):
        pygame.init()
        self.screen = screen
        self.clock = clock
        self.deltatime = delta_time
        self.new_game()

    def new_game(self):
        pass

    def update(self):
        self.player.movement1()
        self.raycasying()
        pygame.display.flip()
        self.deltatime = self.clock.tick(FPS)

    def draw(self):
        self.screen.fill(BLACK)
        self.map.draw_map()
        self.player.draw_player()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

game = Game()
if __name__ == '__main__':
    game.run()



 """













































    
