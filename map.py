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

#constants to do with map grid
MAP_HEIGHT = 8
MAP_WIDTH = 8
TILE_SIZE_width = int((SCREEN_WIDTH / MAP_WIDTH))
TILE_SIZE_height = int((SCREEN_HEIGHT / MAP_WIDTH))
print(TILE_SIZE_width)
print(TILE_SIZE_height)
print(TILE_SIZE_width*8)
print(TILE_SIZE_height*8)
print(SCREEN_WIDTH)
print(SCREEN_HEIGHT)
 
#visual representation of map
MAP = (
    '########'
    '#  #   #'
    '# ###  #'
    '#      #'
    '#      #'
    '# ###  #'
    '#   #  #'
    '########'
) 

  #draw out the 2d map
def draw_map():
    #loop over map rows - R=8xC=8 
    for row in range(8):
        #loop over map columns
        for column in range (8):
            #calculate square index for each square on map - where each square will go 
            square = row * MAP_WIDTH + column

            #draw map in game window
            #pygame.draw.rect(surface,color,rect,optwidth)
            pygame.draw.rect(
                screen,
                (100, 100, 100) if MAP[square] == '#' else (200, 200, 200),#ligth grey for the walls,dark grey everywhere else
                (column * TILE_SIZE_height, row * TILE_SIZE_width, TILE_SIZE_height- 1, TILE_SIZE_width - 1),#actual size of the squares and position (x,y,width,height)
            )  

#print(MAP)

#try:
     #print(MAP[square])
#except IndexError:
      #print("out of range")
      

 


















































 