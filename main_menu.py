import pygame 
from settings import *

def play_game():
    screen.fill(BLACK)
    pygame.draw.rect(screen,RED, pygame.Rect(100, 100, 50, 50),2)

""" filepath = pathlib.Path(__file__).resolve().parent / 'title.png'
logo = pygame.image.load(filepath)
logo = pygame.transform.scale(logo,TITLE_IMAGE_SIZE) """


def draw_floor():
    pygame.draw.rect(screen,(119,119,119),(0,HALF_SCREEN_HEIGHT,SCREEN_WIDTH,SCREEN_HEIGHT))
                 



