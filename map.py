import pygame
from settings import *


#2d array
#  _ = empty space
""" _ = False
model_map = [
[1,1,1,1,1,1,1,1,1,1],
[1,_,_,_,_,_,_,_,_,1],
[1,_,_,_,1,_,_,_,_,1],
[1,_,_,1,1,1,_,_,_,1],
[1,_,_,_,_,_,_,_,_,1],
[1,_,_,_,1,1,1,_,_,1],
[1,_,_,_,_,_,1,_,_,1],
[1,1,1,1,1,1,1,1,1,1],
] """

pygame.init()

MAP_WIDTH = 10
TILE_SIZE = int(SCREEN_WIDTH/ MAP_WIDTH)
#visual representation of map
MAP = (
    '##########'
    '#        #'
    '#   #    #'
    '#  ###   #'
    '#       ##'
    '#   ###  #'
    '#     #  #'
    '##########'
) 

  #draw out the 2d map
#def draw_map():
    #loop over map rows - R=10xC=8
for row in range(10):
        #loop over map columns
        for column in range (8):
            #calculate square index for each square on map - where each square will go 
            square = row * MAP_WIDTH + column

            #draw map in game window
            #pygame.draw.rect(surface,color,rect,optwidth)
            #pygame.draw.rect(
                #screen,
                #(#200, 200, 200) if MAP[square] == '#' else (100, 100, 100),#dark grey for the walls,light grey everywhere else
                #(column * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)#actual size of the squares and position (x,y,width,height)
            
            #)  
try:
     print(MAP[square] == '#')
except IndexError:
      print("out of range")
      

 



















































#player_x,player_y = (1,1 )


#MAP_SIZE = 8
#draw map
#def draw_map():
    #loop over map rows
    #for row in range(8):
        #loop over map columns
        #for column in range (8):
            #calculate square index
            #square = row * MAP_SIZE * column

            #draw map in game window
            #pygame.draw.rect
                #screen,
                #(200,200,200) 