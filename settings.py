import pygame 

RES = WIDTH,HEIGHT = 1500,900
FPS = 30
screen = pygame.display.set_mode(RES) #creates display surface and makes it fullscreen by resizing
pygame.display.set_caption("Apocalypse") #sets title on the window
clock = pygame.time.Clock() #clock object to help make frame rate

#Colours
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)

