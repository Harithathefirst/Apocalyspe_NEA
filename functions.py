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

#function to check if somethign has been pressed 
def check_click(x,y,width,height):
        #checks mouse coordinates and returns true if within rectangle boundareis
        (MOUSE_X,MOUSE_Y) = pygame.mouse.get_pos()
        if (MOUSE_X > x and MOUSE_X < x + width) and (MOUSE_Y > y and MOUSE_Y < y + height):
            return True

def check_user_input():
     pass

#checks the user input for symbols

# def check_user_input_symb(user_input):
#     symbol_pattern = re.compile(r'[^a-zA-Z0-9\s]')
#     char_match = symbol_pattern.search(user_input)
#     print(char_match)
#     return bool(char_match)




def error_message(text_error):
     text_rect = ERROR_TEXT_FONT.render(text_error,True,ERROR_RED)
     #print(text_rect.get_width())
     screen.blit(text_rect,((1000-text_rect.get_width())//2+250,592))



def check_user_input_length(user_input):
     #checks if text entered is correct length
     if len(user_input) >= 3 and len(user_input) <=15:
          print("valid length")
          return True
     elif len(user_input) == 0:
          print("empty entry")
          return False
     else:
          print("wrong length")
          return False

# def check_for_space(user_input):
#      if user_input.isspace() == True:
#           print("empty")  #if blank retrun false
#           return False
#      else:
#           return True



def check_no_symbol(user_input):
     if user_input.isalnum() == True: #all alphanumeric characters in str
          print("no symbol detected")
          return True 
     elif user_input.isalnum() == False: #symbol found in str
          print("Symbol detected")
          return False

#inp = input("enter: ")
     
def check_menu(user_input):
     while check_user_input_length(user_input) == False or check_no_symbol(user_input) == False:
          user_input = " "
     
       

#check_no_symbol(user_input)

#check_no_symbol(user_input)

    
# target = pygame.image.load("C:\\Users\\bindu\\OneDrive - Bright Futures Educational Trust\\Alevel\\CS NEA\\documentcode_git\\Apocalyspe_NEA\\textures and sprites\\target.png")
# target = pygame.transform.scale_by(target,0.2)


# text = input("Enter ")
# print(text)
# print(text.isalnum())


# ent = input("enter: ")

# while ent == " ":
#      print("pls enter a value")
#      ent = input("enter: ")
     
# print(ent)