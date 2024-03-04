import pygame 
import math 

RES = SCREEN_WIDTH,SCREEN_HEIGHT = 1500,900
#1504/8 = 188
#904/8 = 113
FPS= 60

PLAYER_INITIAL_POS = 9,7.5  #on model_map 1 line is equal to 1
PLAYER_ANGLE = 0 #initial angle
PLAYER_SPEED = 0.01 # players speed
PLAYER_ROTATION_SPEED = 0.02 # speed that player can rotate "camera"
delta_time = 1 #makes players speed indepenedent to the frame rate

FOV = math.pi / 3 #players field of view #60* FOV
HALF_FOV = FOV / 2 #half the FOV
NUM_RAYS = SCREEN_WIDTH // 2  #number of rays that will come from player
HALF_NUM_RAYS = NUM_RAYS // 2 #half of number of rays
DELTA_ANGLE = FOV / NUM_RAYS #angle between each ray
MAX_DEPTH = 20 #draw distance

screen = pygame.display.set_mode(RES)#creates display surface and makes it fullscreen by resizing
pygame.display.set_caption("Apocalypse") #sets title on the window
clock = pygame.time.Clock() #clock object to help make frame rate 

#Colours
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
MAIN_PURPLE =(51, 0, 123)

TITLE_IMAGE_SIZE = (500,500)
