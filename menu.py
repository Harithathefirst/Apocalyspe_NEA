import pygame
import time
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
        self.font = MENU_TEXT_FONT
        self.text_colour = (MENU_ORANGE)
        self.invisible_box_colour = MAIN_PURPLE
        self.height = 100 #height of box arund buttons approx
        self.height_box = 65 #height of box around all buttons
        self.width_play = 290 #width of box around play button
        self.width_instruct_lb = 386 #width of box around leaderboard and instructions
        self.width_controls = 327 #width of box around controls 
        self.width = 500 #width of box around buttons approx
        self.border = 2 #thickness of border of boxes
        self.play_x = 605 #where the play game box button will begin  xcoord
        self.instruction_x = 550 #where the instructiosn box button will begin drawing xcoord
        self.leaderboard_x = 558  #where the leaderboard box button will begin drawing xcoord
        self.box_y = 392 #the y coordinate of where all the boxes will begin drawing
        self.gap = (128/3) #gap between each button

       


    def background(self):
        #fills screen as purple 
        screen.fill(MAIN_PURPLE)

    def title(self):
        #copies image onto main game screen
        #centers image 
        screen.blit(logo,((SCREEN_WIDTH - logo.get_width())/2 - 81,5))
        
   
    def draw_button(self,font):
        #draws username input box
        pygame.time.delay(5000)
        pygame.draw.rect(screen,USERNAME_BLUE,(SCREEN_WIDTH//2,SCREEN_HEIGHT//2,self.width,self.height))
        username_text = font.render('ENTER PLAYER NAME')

    def play_game(self):
        #play game button
        text = "PLAY GAME"
        play_game = self.font.render(text,True,self.text_colour)
        play_rect_draw = pygame.draw.rect(screen,
                         MENU_ORANGE,
                         (self.play_x,self.box_y,self.width_play,self.height_box),self.border)
        play_rect = play_game.get_rect(center = (500 + self.width//2,372 + self.height//2))
        #print(play_game.get_rect())
        screen.blit(play_game,play_rect)

    
    def instruction(self):
        #instructiopns button
        text = "INSTRUCTIONS "
        instructions = self.font.render(text,True,self.text_colour)
        instructions_rect_draw = pygame.draw.rect(screen,
                         MENU_ORANGE,
                         (self.instruction_x,self.box_y + self.height + self.gap,self.width_instruct_lb,self.height_box*2),self.border) 
        instructions_rect = instructions.get_rect(center = (500+self.width//2,372 + self.height + self.gap + self.height//2))
        #print(instructions.get_rect())
        screen.blit(instructions,instructions_rect)

    def controls(self):
        #instructions button
        text = "& CONTROLS"
        controls = self.font.render(text,True,self.text_colour)
        #controls_rect_draw = pygame.draw.rect(screen,
         #                MENU_ORANGE,
          #               (500,372 + self.height + (128/3),self.width,self.height*2),self.border) 
        controls_rect = controls.get_rect(center = (500+self.width//2,372 + self.height + self.gap + self.height//2 + 75))
        #print(controls.get_rect())
        screen.blit(controls,controls_rect)

    def leaderboard(self):
        #leaderbaord button
        text = "LEADERBOARD"
        leaderboard = self.font.render(text,True,self.text_colour)
        leaderboard_rect_draw = pygame.draw.rect(screen,
                         MENU_ORANGE,
                         (self.leaderboard_x,self.box_y + self.height + self.gap+self.height*2 + self.gap,
                          self.width_instruct_lb,self.height_box),self.border) 
        leaderboard_rect = leaderboard.get_rect(center = (500 + self.width//2,372 + self.height + self.gap + self.height*2 + self.gap + 50))
        #print(leaderboard.get_rect())
        screen.blit(leaderboard,leaderboard_rect)

    def click_play_game(self):
         if (self.MOUSE_X > 605 and self.MOUSE_X < 605 + self.width_play) and (self.MOUSE_Y > 392 and self.MOUSE_Y < 392 + self.height_play):
                 print(self.MOUSE_X,self.MOUSE_Y)
                 print("clicked")
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def draw_circ(self):
           #pygame.draw.circle(screen,BLUE,(self.x ,-(SCREEN_HEIGHT/3)),15) 
           #pygame.draw.circle(screen,RED,(self.x,SCREEN_HEIGHT),15) 
           pygame.draw.circle(screen,GREEN,(self.x,((SCREEN_HEIGHT/3) + (SCREEN_HEIGHT/3))),15)  
           pygame.draw.circle(screen,BLUE,(self.x,(SCREEN_HEIGHT/3.7)),15)       

    
    
        










        
        #filepath = pathlib.Path(__file__).resolve().parent / 'textures and sprites/title1.png'
        #logo = pygame.image.load(filepath)
        #logo = pygame.transform.scale_by(logo,1) 
        #print(logo.get_size())