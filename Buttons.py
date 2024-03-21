import pygame
from settings import *

class Buttons:
    def __init__(self,text,text_colour,box_colour,font,x,y,width,height,gap,offset,extra_gap,centre,text_y,border): #parameters needed to make box around text
        self.text = text #text inside box
        self.x = x #x coordinates of bow
        self.y = y #y coordinates of box
        self.width = width #width of box
        self.height = height #height of box
        self.font = font #font used for text
        self.text_colour = text_colour #text colour
        self.box_colour = box_colour
        self.invisible_box_colour = MAIN_PURPLE #colour of background to make box look invisible
        self.rect_height = 100 #rectangle height constant
        self.rect_width = 500 #rectangle width constant
        self.gap = gap #gap between each bow
        self.border = border #thickness of line 
        self.offset = offset #extra number added on to box to make it even
        self.centre = centre #x coordinate of centre of text on screen SW/2
        self.text_y = text_y #texts y coordinate
        self.extra_gap = extra_gap
        

    def make_button(self): #makes box and renders text for 
        #if button is solid
        if self.border == 0:
            text_render = self.font.render(self.text,True,self.text_colour,self.box_colour) #renders text into box
            text_rect = text_render.get_rect(center = (self.centre,self.text_y + self.gap + self.rect_height//2 + self.offset))
            screen.blit(text_render,text_rect) #copies text onto text rectangle
        else:   
            text_render = self.font.render(self.text,True,self.text_colour) #renders text into box
            text_rect_draw = pygame.draw.rect(screen,
                            self.invisible_box_colour,(self.x,self.y + self.gap - self.extra_gap,self.width,self.height),self.border)
            text_rect = text_render.get_rect(center = (self.centre,self.text_y + self.gap + self.rect_height//2 + self.offset))
            screen.blit(text_render,text_rect) #copies text onto text rectangle
 

        

    def check_click(self):
        #checks mouse coordinates and returns true if within rectangle boundareis
        (MOUSE_X,MOUSE_Y) = pygame.mouse.get_pos()
        if (MOUSE_X > self.x and MOUSE_X < self.x + self.width) and (MOUSE_Y > self.y and MOUSE_Y < self.y + self.height):
            return True
    
    
        





     # if event.type == pygame. MOUSEBUTTONDOWN:
     #      print(MOUSE_X,MOUSE_Y)
     #      if (MOUSE_X > b.play_x and MOUSE_X < b.play_x + b.width_play) and (MOUSE_Y > b.box_y and MOUSE_Y < b.box_y + b.height_box):
     #           print(MOUSE_X,MOUSE_Y)
     #           print("clicked")
     #           menu = False

    
 # if event.type == pygame. MOUSEBUTTONDOWN:
     #      print(MOUSE_X,MOUSE_Y)
     #      if (MOUSE_X > b.play_x and MOUSE_X < b.play_x + b.width_play) and (MOUSE_Y > b.box_y and MOUSE_Y < b.box_y + b.height_box):
     #           print(MOUSE_X,MOUSE_Y)
     #           print("clicked")
     #           menu = False
     #      elif event.type == pygame.MOUSEBUTTONUP:
     #            print("button up")
     #      if event.type == pygame. MOUSEBUTTONDOWN:
     #           (MOUSE_X,MOUSE_Y) = pygame.mouse.get_pos()
     #      if (MOUSE_X > b.instruction_x and MOUSE_X < b.instruction_x + b.width_instruct_lb) and (MOUSE_Y >  b.box_y and MOUSE_Y < b.box_y + b.height_box*2):
     #                      print(MOUSE_X,MOUSE_Y)
     #                      print("instr clck")
     #                      instructions = True
     #    elif event.type == pygame.MOUSEBUTTONUP:
     #            instructions = True
     #    if event.type == pygame. MOUSEBUTTONDOWN:
     #        (MOUSE_X,MOUSE_Y) = pygame.mouse.get_pos()
        
     #        if (MOUSE_X > b.leaderboard_x and MOUSE_X < b.leaderboard_x + b.width_instruct_lb) and (MOUSE_Y > b.box_y and MOUSE_Y < b.box_y + b.height_box):
     #            print(MOUSE_X,MOUSE_Y)
     #            print("leaderbosr dpress")
     #    elif event.type == pygame.MOUSEBUTTONUP:
     #            leaderboard = True