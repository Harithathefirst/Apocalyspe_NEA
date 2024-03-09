import pygame
from settings import *


class Buttons:
    def __init__(self,width,height):
        self.width = 50
        self.height = self.width*2
        self.border = 2
        self.font = pygame.font.Font('freesansbold.ttf', 32)

    def draw_button(self):
        pygame.draw.rect(screen,USERNAME_BLUE,(500,500,self.width,self.height))
        username_text = self.font.render('ENTER PLAYER NAME')