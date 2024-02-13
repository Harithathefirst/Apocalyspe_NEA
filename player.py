import pygame

def movement(x,y,x_change,y_change,speed):
    for event in pygame.event.get():
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
    #add on the change coordinates to og coordinates
    x += x_change
    y += y_change
    return x,y,x_change,y_change
