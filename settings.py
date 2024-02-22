import pygame 

RES = SCREEN_WIDTH,SCREEN_HEIGHT = 1500,900
#1504/8 = 188
#904/8 = 113
FPS = 60
PLAYER_INITIAL_POS = 1.5, 5 #model_map
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.004
PLAYER_ROTATION_SPEED = 0.002
delta_time = 1 #makes players speed indepenedent to the frame rate

screen = pygame.display.set_mode(RES) #creates display surface and makes it fullscreen by resizing
pygame.display.set_caption("Apocalypse") #sets title on the window
clock = pygame.time.Clock() #clock object to help make frame rate 

#Colours
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)

