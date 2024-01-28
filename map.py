import pygame

#2d array
#  _ = empty space
_ = False
model_map = [
[1,1,1,1,1,1,1,1,1,1],
[1,_,_,_,_,_,_,_,_,1],
[1,_,_,_,1,_,_,_,_,1],
[1,_,_,1,1,1,_,_,_,1],
[1,_,_,_,_,_,_,_,_,1],
[1,_,_,_,1,1,1,_,_,1],
[1,_,_,_,_,_,1,_,_,1],
[1,1,1,1,1,1,1,1,1,1],
]






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