import pygame
from settings import *






#FONT = pygame.font.SysFont('Horta',35)
#text = FONT.render('quit' , True , RED) 
#self.font = pygame.font.SysFont('freesansbold.ttf', 32)

#define boxes/title image
logo = pygame.image.load("C:\\Users\\bindu\\OneDrive - Bright Futures Educational Trust\\Alevel\\CS NEA\\documentcode_git\\Apocalyspe_NEA\\textures and sprites\\title1.png") #import the title image
logo = pygame.transform.scale_by(logo,1.7) #scales all sides by 1.7
##print(logo.get_size())
#print(width)


class Menu:
    def __init__(self):
        #self.font = pygame.font.SysFont("Arial", 30)
        self.text_colour = (MENU_ORANGE)
        self.height = 100 #height of box aorund buttons approx
        self.height_play = 65 #height of box around all buttons
        self.width_play = 290 #width of box around play button
        self.width_instruct_lb = 386 #width of box around leaderboard and instructions
        self.width_controls = 327 #width of box around controls 
        self.width = 500 #width of box around buttons approx
        self.border = 2 #thickness of border
       


    def background(self):
        screen.fill(MAIN_PURPLE)

    def title(self):
        screen.blit(logo,((SCREEN_WIDTH - logo.get_width())/2 - 81,5))
        
   
    def draw_button(self):
        pygame.draw.rect(screen,USERNAME_BLUE,(500,500,self.width,self.height))
        username_text = self.font.render('ENTER PLAYER NAME')

    def play_game(self,text,font,text_colour):
        play_game = font.render(text,True,text_colour)
        play_rect_draw = pygame.draw.rect(screen,
                         MENU_ORANGE,
                         (605,392,self.width_play,self.height_play),self.border)
        play_rect = play_game.get_rect(center = (500 + self.width//2,372 + self.height//2))
        #print(play_game.get_rect())
        screen.blit(play_game,play_rect)

    
    def instruction(self,text,font,text_colour):
        instructions = font.render(text,True,text_colour)
        instructions_rect_draw = pygame.draw.rect(screen,
                         MENU_ORANGE,
                         (550,392 + self.height + (128/3),self.width_instruct_lb,self.height_play*2),self.border) 
        instructions_rect = instructions.get_rect(center = (500+self.width//2,372 + self.height + (128/3) + self.height//2))
        #print(instructions.get_rect())
        screen.blit(instructions,instructions_rect)

    def controls(self,text,font,text_colour):
        controls = font.render(text,True,text_colour)
        #controls_rect_draw = pygame.draw.rect(screen,
         #                MENU_ORANGE,
          #               (500,372 + self.height + (128/3),self.width,self.height*2),self.border) 
        controls_rect = controls.get_rect(center = (500+self.width//2,372 + self.height + (128/3) + self.height//2 + 75))
        #print(controls.get_rect())
        screen.blit(controls,controls_rect)

    def leaderboard(self,text,font,text_colour):
        leaderboard = font.render(text,True,text_colour)
        leaderboard_rect_draw = pygame.draw.rect(screen,
                         MENU_ORANGE,
                         (558,392 + self.height + (128/3)+self.height*2 + (128/3),
                          self.width_instruct_lb,self.height_play),self.border) 
        leaderboard_rect = leaderboard.get_rect(center = (500 + self.width//2,372 + self.height + (128/3) + self.height*2 + (128/3) + 50))
        #print(leaderboard.get_rect())
        screen.blit(leaderboard,leaderboard_rect)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def draw_circ(self):
           #pygame.draw.circle(screen,BLUE,(self.x ,-(SCREEN_HEIGHT/3)),15) 
           #pygame.draw.circle(screen,RED,(self.x,SCREEN_HEIGHT),15) 
           pygame.draw.circle(screen,GREEN,(self.x,((SCREEN_HEIGHT/3) + (SCREEN_HEIGHT/3))),15)  
           pygame.draw.circle(screen,BLUE,(self.x,(SCREEN_HEIGHT/3.7)),15)       

    
    
        










        
        #filepath = pathlib.Path(__file__).resolve().parent / 'textures and sprites/title1.png'
        #logo = pygame.image.load(filepath)
        #logo = pygame.transform.scale_by(logo,1) 
        #print(logo.get_size())