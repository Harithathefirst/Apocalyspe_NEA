import pygame
from settings import *
import os
import pathlib


class Buttons:
    def __init__(self):
        self.height = 500
        self.width = self.height*2
        self.border = 2
        #self.font = pygame.font.SysFont('freesansbold.ttf', 32)

    def menu(self):
        filepath = pathlib.Path(__file__).resolve().parent / 'title1.png'
        logo = pygame.image.load(filepath)
        logo = pygame.transform.scale_by(logo,1) 
        #print(logo.get_size())
        screen.fill(MAIN_PURPLE)
        screen.blit(logo,((SCREEN_WIDTH - 973)/2 - 81,0))
   
    def draw_button(self):
        pygame.draw.rect(screen,USERNAME_BLUE,(500,500,self.width,self.height))
        username_text = self.font.render('ENTER PLAYER NAME')

    def play_game(self):
        pygame.draw.rect(screen,MENU_ORANGE,(SCREEN_WIDTH//2,SCREEN_HEIGHT//2,self.width,self.height),2)