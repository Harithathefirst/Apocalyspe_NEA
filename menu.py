import pygame
import time
from settings import *
from Buttons import *






#FONT = pygame.font.SysFont('Horta',35)
#text = FONT.render('quit' , True , RED) 
#self.font = pygame.font.SysFont('freesansbold.ttf', 32)




class Menu:
    def __init__(self):
        self.font = MENU_TEXT_FONT
        self.text_colour = (MENU_ORANGE)
        self.invisible_box_colour = MAIN_PURPLE
        self.username_font = USERNAME_FONT
        self.close = Buttons("CLOSE",1400,800,50,100,0,0,1400)

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
        self.username_width = (SCREEN_WIDTH - 500)
        self.username_height = (SCREEN_HEIGHT - 450)

       


    def background(self):
        #fills screen as purple 
        screen.fill(MAIN_PURPLE)

    def title(self):
        #define boxes/title image
        logo = pygame.image.load("C:\\Users\\bindu\\OneDrive - Bright Futures Educational Trust\\Alevel\\CS NEA\\documentcode_git\\Apocalyspe_NEA\\textures and sprites\\title1.png") #import the title image
        logo = pygame.transform.scale_by(logo,1.7) #scales all sides by scalefactor
        #copies image onto main game screen
        #centers image 
        screen.blit(logo,((SCREEN_WIDTH - logo.get_width())/2 - 81,0))
        #print(logo.get_height())
        #print(logo.get_width())
        #print(width)
        #screen.blit(logo,((SCREEN_WIDTH-973)/2 - 81,0))
        
   
    def username_box(self):
        #draws username input box
        text = "ENTER PLAYER NAME"
        blue = pygame.draw.rect(screen,USERNAME_BLUE,(250 - 20,self.box_y - 10,self.username_width + 40,self.username_height + 20))
        username_text = self.username_font.render(text,True,BLACK)
        username_box = username_text.get_rect(center = (500 + self.width//2,372 + self.height//2))
        username_text = self.username_font.render(text,True,BLACK)
        usr_height = username_text.get_height()
        usr_inp = pygame.draw.rect(screen,WHITE,(250 - 20 + 20 ,self.box_y - 10 + usr_height - 20,self.username_width ,self.username_height//8 + 20))
        screen.blit(username_text,username_box)
        

    def username_input(self):
         pass
    

    def instructions_screen(self):
         screen.fill(MAIN_PURPLE)
         self.close.make_button()
         text_title = "INSTRUCTIONS"
         text_title_draw = self.font.render(text_title,True,self.text_colour)
         screen.blit(text_title_draw,(6,0 ))

         text_main = (
                       "YOU ARE THE THE LAST SURVIVOR OF A POST - APOCALYPTIC WORLD.\n" 
                       "NAVIGATE THROUGH THE LEVELS,KILL THE ROBOTS TO STAY ALIVE AND\n"
                        "ESCAPE.GOOD LUCK SOLDIER! ")
         text_main_draw = self.font.render(text_main,True,self.text_colour)
         screen.blit(text_main_draw,(10,50))

         #text_controls = "CONTROLS:"
         #text_controls_draw = self.font.render(text_controls,True,self.text_colour)

        # key_control_w = "W - MOVE FORWARD"
        #  key_control_w_draw = self.font.render(key_control_w,True,self.text_colour)

        #  key_control_a = "A - MOVE LEFT"
        #  key_control_a_draw = self.font.render(key_control_a,True,self.text_colour)

        #  key_control_s = "S - MOVE BACKWARD"
        #  key_control_s_draw = self.font.render(key_control_s,True,self.text_colour)

        #  key_control_d = "D - MOVE RIGHT"
        #  key_control_d_draw = self.font.render(key_control_s,True,self.text_colour)

        #  key_control_sp = "SPACE - JUMP"
        #  key_control_sp_draw = self.font.render(key_control_s,True,self.text_colour)

        #  key_control_m = "MOUSE - LOOK AROUND"
        #  key_control_m_draw = self.font.render(key_control_s,True,self.text_colour)

        #  key_control_mshoot = "MOUSE - MOVE FORWARD"
        #  key_control_mshoot_draw = self.font.render(key_control_s,True,self.text_colour)

         


    def leaderboard_screen(self):
        screen.fill(MAIN_PURPLE)
        print("leaderboard")  
        
        
         
























































  # def play_game(self):
    #     #play game button
    #     text = "PLAY GAME"
    #     play_game = self.font.render(text,True,self.text_colour)
    #     play_rect_draw = pygame.draw.rect(screen,
    #                      MENU_ORANGE,
    #                      (self.play_x,self.box_y,self.width_play,self.height_box),self.border)
    #     play_rect = play_game.get_rect(center = (500 + self.width//2,372 + self.height//2))
    #     #print(play_game.get_rect())
    #     screen.blit(play_game,play_rect)


    # def instruction(self):
    #     #instructiopns button
    #     text = "INSTRUCTIONS "
    #     instructions = self.font.render(text,True,self.text_colour)
    #     instructions_rect_draw = pygame.draw.rect(screen,
    #                      MENU_ORANGE,
    #                      (self.instruction_x,self.box_y + self.height + self.gap,self.width_instruct_lb,self.height_box*2),self.border) 
    #     instructions_rect = instructions.get_rect(center = (500+self.width//2,372 + self.height + self.gap + self.height//2))
    #     #print(instructions.get_rect())
    #     screen.blit(instructions,instructions_rect)



    # def controls(self):
    #     #instructions button
    #     text = "& CONTROLS"
    #     controls = self.font.render(text,True,self.text_colour)
    #     #controls_rect_draw = pygame.draw.rect(screen,
    #      #                MENU_ORANGE,
    #       #               (500,372 + self.height + (128/3),self.width,self.height*2),self.border) 
    #     controls_rect = controls.get_rect(center = (500+self.width//2,372 + self.height + self.gap + self.height//2 + 75))
    #     #print(controls.get_rect())
    #     screen.blit(controls,controls_rect)

    # def leaderboard(self):
    #     #leaderbaord button
    #     text = "LEADERBOARD"
    #     leaderboard = self.font.render(text,True,self.text_colour)
    #     leaderboard_rect_draw = pygame.draw.rect(screen,
    #                      MENU_ORANGE,
    #                      (self.leaderboard_x,self.box_y + self.height + self.gap+self.height*2 + self.gap,
    #                       self.width_instruct_lb,self.height_box),self.border) 
    #     leaderboard_rect = leaderboard.get_rect(center = (500 + self.width//2,372 + self.height + self.gap + self.gap + self.height//2 + 200))
    #     #print(leaderboard.get_rect())
    #     screen.blit(leaderboard,leaderboard_rect)

  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # def draw_circ(self):
    #        #pygame.draw.circle(screen,BLUE,(self.x ,-(SCREEN_HEIGHT/3)),15) 
    #        #pygame.draw.circle(screen,RED,(self.x,SCREEN_HEIGHT),15) 
    #        pygame.draw.circle(screen,GREEN,(self.x,((SCREEN_HEIGHT/3) + (SCREEN_HEIGHT/3))),15)  
    #        pygame.draw.circle(screen,BLUE,(self.x,(SCREEN_HEIGHT/3.7)),15)       

    
    
        










        
        #filepath = pathlib.Path(__file__).resolve().parent / 'textures and sprites/title1.png'
        #logo = pygame.image.load(filepath)
        #logo = pygame.transform.scale_by(logo,1) 
        #print(logo.get_size())