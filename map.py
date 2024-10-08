import pygame
from settings import *


#2d array
#  _ = empty space

_ = 0
model_map = [
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,_,_,_,_,_,1,_,_,_,_,_,_,_,1],
[1,_,_,_,_,1,1,1,1,_,1,1,1,_,1],
[1,_,_,_,_,_,1,_,_,_,_,_,1,_,1],
[1,_,1,1,_,_,_,_,_,_,_,_,1,_,1],
[1,1,1,_,_,_,_,_,_,_,_,1,1,_,1],
[1,_,1,_,_,_,_,1,1,1,_,_,_,_,1],
[1,_,_,_,_,_,_,_,_,1,_,_,_,_,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
] 

class Map:
    def __init__(self):
        self.model_map = model_map #what the map should look like
        self.worldmap = {} #dictionary to write the coordinated of any elements with numeric value
        self.get_map() 

    def get_map(self):
        for j, row in enumerate(model_map): #l
            for i, value in enumerate(row):
                if value:
                    self.worldmap[(i,j)] = value #writes value into dictionary if there is a numerical value - 1
    def draw_map(self):
        [pygame.draw.rect(screen,'white',(pos[0] * 100, pos[1] * 100, 100, 100), 2)       #RECT - (x,y,width,height)
        for pos in self.worldmap] #draws 100x100 grid where there is 1 in dictionary
        
    



    

































































""" #constants to do with map grid
MAP_HEIGHT = 8
MAP_WIDTH = 8
TILE_SIZE = int((SCREEN_WIDTH / MAP_WIDTH))
print(TILE_SIZE)
 
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
                (column * TILE_SIZE, row * TILE_SIZE, TILE_SIZE - 1, TILE_SIZE - 1),#actual size of the squares and position (x,y,width,height)
            )  

#print(MAP)

#try:
     #print(MAP[square])
#except IndexError:
      #print("out of range") """
      

 


















































 