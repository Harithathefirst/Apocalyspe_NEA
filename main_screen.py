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
from menu import *
from raycasting import *


#initialise pygame
pygame.init()


#create instance of classes
map = Map() #map class
player = Player() #player class
b = Menu()
#c= test_circle()

def gameplay():
    player.raycast()
    player.movement()


run=True
menu = True
instructions = False
leaderboard = False
#game runs in this loop
#main game loop




while run:
    if menu == True:
         b.background()
         pygame.draw.circle(screen,RED,(605,392),10)
         b.title()
         b.play_game()
         b.instruction()
         b.controls()
         b.leaderboard()

    #close game condition
    for event in pygame.event.get():
        (MOUSE_X,MOUSE_Y) = pygame.mouse.get_pos()
        if event.type == pygame. MOUSEBUTTONDOWN:
            if (MOUSE_X > b.play_x and MOUSE_X < b.play_x + b.width_play) and (MOUSE_Y > b.box_y and MOUSE_Y < b.box_y + b.height_box):
                 print(MOUSE_X,MOUSE_Y)
                 print("clicked")
            elif event.type == pygame.MOUSEBUTTONUP:
                 menu = False
        if event.type == pygame. MOUSEBUTTONDOWN:
            if (MOUSE_X > b.instruction_x and MOUSE_X < b.instruction_x + b.width_instruct_lb) and (MOUSE_Y >  b.box_y and MOUSE_Y < b.box_y + b.height_box*2):
                print("instr clck")
                print(MOUSE_X,MOUSE_Y)
            elif event.type == pygame.MOUSEBUTTONUP:
                instructions = True
        if event.type == pygame. MOUSEBUTTONDOWN:
            if (MOUSE_X > b.leaderboard_x and MOUSE_X < b.leaderboard_x + b.width_instruct_lb) and (MOUSE_Y > b.box_y and MOUSE_Y < b.box_y + b.height_box):
                print("leaderbosr dpress")
            elif event.type == pygame.MOUSEBUTTONUP:
                leaderboard = True
                
        if event.type == pygame.QUIT:
            run=False
            pygame.quit()
            sys.exit(0) # closes the while loop 
         
            
    pygame.display.flip() #updates screen every frame
    screen.fill(BLACK)
    #map.draw_map()
    #player.draw_player()
    if menu == False:
        player.movement()
        player.raycast()
    # elif instructions == True:
    #     screen.fill(MAIN_PURPLE)
    # elif leaderboard == True:
    #     screen.fill(RED)
   
    clock.tick(FPS) #main loop shouldnt run faster than 60 times per second 



    
    #print(raycast())
    #print(player.x,player.y)
    #print(player.movement())
    #player.stop_moving()
    #player.moving()
    #player.moving()
    #screen.blit()
    #raycast()

    
   
 
    
  
    
    
    


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













































    
