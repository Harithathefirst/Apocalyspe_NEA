import pygame

def movement(event,speed,x_change,y_change):
 #WASD CONTROLS
        if event.type == pygame.KEYDOWN:
            #W - move forards
            if event.key == pygame.K_w:
                x_change = 0
                y_change=-speed
            #A - move to the left
            elif event.key == pygame.K_a:
                x_change=-speed
                y_change=0
            #S - move backwards
            elif event.key == pygame.K_s:
                x_change=0
                y_change=speed
            #D- move to the right
            elif event.key == pygame.K_d:
                x_change=speed
                y_change=0
        elif event.type == pygame.KEYUP:
                 #W - move forards
            if event.key == pygame.K_w:
                x_change = 0
                y_change=0 
            #A - move to the left
            elif event.key == pygame.K_a:
                x_change=0
                y_change=0
            #S - move backwards
            elif event.key == pygame.K_s:
                x_change=0
                y_change=0
            #D- move to the right
            elif event.key == pygame.K_d:
                x_change=0
                y_change=0
            return x_change,y_change


#def add(a,b):
    #return a+b

class Player:
    def __init__(self,x,y,speed):
        self.x = x
        self.y = y
        self.speed = 8
    
    def move_forward(self,event,speed):
            if event.key == pygame.K_w:
                x_change = 0
                y_change=-speed