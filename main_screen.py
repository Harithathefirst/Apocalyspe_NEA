#packages/imports
import pygame 
import sys #import sys  #imports system-specific parameters and functions
import os 
import pathlib
from settings import *
import math #access sin and cos
import time
from player import Player
from map import *
from menu import *
from raycasting import *
from Buttons import *
#from texture import *


#initialise pygame
pygame.init()


#create instance of classes
map = Map() #map class
player = Player() #player class
menu = Menu()
play_game = Buttons("PLAY GAME",605,392,290,65,0,0)
instructions = Buttons("INSTRUCTIONS",550,(392+100),386,65*2,(128/3),100)
controls = Buttons("& CONTROLS",0,0,0,0,(128/3),175)
leaderboard = Buttons("LEADERBOARD",558,(392 + 100 + (100*2)),386,65,(256/3),300)
#t = Graphics()
#c= test_circle()

run=True
main_menu = True
#instructions = False
#leaderboard = False
#game runs in this loop
#main game loop

while run:
     for event in pygame.event.get():
          (MOUSE_X,MOUSE_Y) = pygame.mouse.get_pos()
          if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
               run=False
               pygame.quit()
               sys.exit(0) # closes the while loop 

     if main_menu == True:
          menu.background()
          menu.title()
          #menu.instructions_screen()
          play_game.make_button()
          instructions.make_button()
          controls.make_button()
          leaderboard.make_button()

          if play_game.check_click() == True and event.type == pygame.MOUSEBUTTONDOWN:
               main_menu = False
          #screen.fill(BLACK)
          player.movement()
          player.raycast()
               
          #pygame.time.delay(5000)
          #b.username_box()
          #b.username_input()
          
   

#close game condition
# print(MOUSE_X,MOUSE_Y)
    
    
    
                          
             

     pygame.display.flip() #updates screen every frame
     #screen.fill(BLACK)
        #map.draw_map()
        #player.draw_player()
    
        #t.draw()
        #player.mouse_movement()
        #player.move_update()

     clock.tick(FPS) #main loop shouldnt run faster than 60 times per second 



      #b.instructions_screen()
    #while menu == False and instructions == False and leaderboard == False:

    # while instructions == True and menu == False and leaderboard == False:
    #      screen.fill(MAIN_PURPLE)
    # while leaderboard == True and menu == False and instructions == False:
    #      screen.fill(RED)
    #print(raycast())
    #print(player.x,player.y)
    #print(player.movement())
    #player.stop_moving()
    #player.moving()
    #player.moving()
    #screen.blit()
    #raycast()

    
   
 
    
  
    
    
# class Game:
#      def __init__(self):
#          pygame.init()
#          self.screen = screen
#          self.clock = clock
#          self.map = Map()
#          self.player = Player()
#          self.menu = Menu()
#          self.play_game = Buttons("PLAY GAME",605,392,290,65,0,0)
#          self.instructions = Buttons("INSTRUCTIONS",550,(392+100),386,65*2,(128/3),100)
#          self.controls = Buttons("& CONTROLS",0,0,0,0,(128/3),175)
#          self.leaderboard = Buttons("LEADERBOARD",558,(392 + 100 + (100*2)),386,65,(256/3),300)
               
    
#      def check_events(self):
#          for event in pygame.event.get():
#              if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
#                pygame.quit()
#                sys.exit(0) # closes the while loop 

#      def main_menu(self):
#           self.menu.background()
#           self.menu.title()
#           self.menu.instructions_screen()
#           self.play_game.make_button()
#           self.instructions.make_button()
#           self.controls.make_button()
#           self.leaderboard.make_button()
          

#      def update(self):
#          pygame.display.flip()
#          self.clock.tick(FPS)
    
#      def main_game_loop(self):
#           screen.fill(BLACK)
#           #self.map.draw_map()
#           self.player.movement()
#           #self.player.draw_player()
#           self.player.raycast()
#           #self.screen.fill(BLACK)
#           self.update()
#           self.check_events()


# game = Game()
# while __name__ == '__main__':
#      game.check_events()
#      game.main_menu()



             

     #    pygame.display.flip() #updates screen every frame
     #    screen.fill(BLACK)
     #    #map.draw_map()
     #    #player.draw_player()
     #    player.movement()
     #    player.raycast()
     #    t.draw()
     #    #player.mouse_movement()
     #    #player.move_update()



# run=True
# menu = True
# instructions = False
# leaderboard = False
# #game runs in this loop
# #main game loop

# while run:
#         if menu == True:
#             b.background()
#             #pygame.draw.circle(screen,RED,(605,392),10)
#             b.title()
#             b.play_game()
#             b.instruction()
#             b.controls()
#             b.leaderboard()
 













































    
