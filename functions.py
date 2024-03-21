import pygame
from settings import *


def multiple_lines_text(text,pos,font): 
        #font = INSTRUCTION_TEXT_FONT 
        paragraph = [word.split (' ') for word in text.splitlines()] #2d list 
        space = font.size(' ')[0] #width of character
        x,y = pos #where text will start
        for lines in paragraph:
            for words in lines:
                text_draw = font.render(words,True,MENU_ORANGE)
                word_width, word_height = text_draw.get_size()
                #if text recahes edge of screen start new line
                if x + word_width >= SCREEN_WIDTH:
                    x = pos[0]
                    y += word_height
                screen.blit(text_draw,(x,y))
                x += word_width + space
        #start a new line at the word breaks
        x = pos[0]
        y += word_height
       

# target = pygame.image.load("C:\\Users\\bindu\\OneDrive - Bright Futures Educational Trust\\Alevel\\CS NEA\\documentcode_git\\Apocalyspe_NEA\\textures and sprites\\target.png")
# target = pygame.transform.scale_by(target,0.2)