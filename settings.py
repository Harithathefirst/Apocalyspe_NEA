import pygame 
import math 
import pathlib


pygame.init()

RES = SCREEN_WIDTH,SCREEN_HEIGHT = 1500,900
HALF_SCREEN_WIDTH = SCREEN_WIDTH//2
HALF_SCREEN_HEIGHT = SCREEN_HEIGHT//2
#1504/8 = 188
#904/8 = 113
FPS= 60



#map coordinates
PLAYER_INITIAL_POS = 4,6  #on model_map 1 line is equal to 1
PLAYER_ANGLE = 0 #initial angle
PLAYER_SPEED = 0.05 # players speed
PLAYER_ROTATION_SPEED = 0.03 # speed that player can rotate "camera"
delta_time = 1 #makes players speed indepenedent to the frame rate

FOV = math.pi / 3 #players field of view #60* FOV
HALF_FOV = FOV / 2 #half the FOV
NUM_RAYS = SCREEN_WIDTH // 2  #number of rays that will come from player
HALF_NUM_RAYS = NUM_RAYS // 2 #half of number of rays
DELTA_ANGLE = FOV / NUM_RAYS #angle between each ray
MAX_DEPTH = 20 #draw distance

WALL_DIST = HALF_SCREEN_WIDTH / math.tan(HALF_FOV)
SCALE = SCREEN_WIDTH // NUM_RAYS




screen = pygame.display.set_mode((RES))#creates display surface and makes it fullscreen by resizing  pygame.RESIZABLE
pygame.display.set_caption("Apocalypse") #sets title on the window
clock = pygame.time.Clock() #clock object to help make frame rate 



#Colours
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
MAIN_PURPLE =(51, 0, 123)
USERNAME_BLUE = (0, 179, 255)
MENU_ORANGE = (253, 110, 14)
CLOSE_GREEN = (148, 221, 38)
ERROR_RED = (230,0,0)

#Fonts
font_file_path = pathlib.Path(__file__).resolve().parent / 'BarlowSemiCondensed-Black.ttf'
MENU_TEXT_FONT = pygame.font.Font(font_file_path,60)
INSTRUCTION_TITLE_FONT = pygame.font.Font(font_file_path,80)
LEADERBOARD_TITLE_FONT = pygame.font.Font(font_file_path,100)
INSTRUCTION_TEXT_FONT = pygame.font.Font(font_file_path,45)
ERROR_TEXT_FONT = pygame.font.Font(font_file_path,40)
#CONTROLS_TEXT_FONT = pygame.font.Font(font_file_path,50)
USERNAME_FONT = pygame.font.Font(font_file_path,100)
TEXT_FONT = pygame.font.Font(None,40)

INSTRUCTION_TEXT = "YOU ARE THE THE LAST SURVIVOR OF A POST-APOCALYPTIC WORLD.\nNAVIGATE THROUGH THE LEVELS, KILL THE ROBOTS TO STAY ALIVE AND\nESCAPE. GOOD LUCK SOLDIER!"
CONTROLS_TEXT = "W - MOVE FORWARD            \nA - MOVE LEFT                       \nS - MOVE BACKWARD           \nD - MOVE RIGHT          \nSPACEBAR - JUMP      \nMOUSE - LOOK AROUND \nMOUSE - LEFTCLICK SHOOT"


#textures
TEXTURE_SIZE = 256
HALF_TEXTURE_SIZE = TEXTURE_SIZE//2