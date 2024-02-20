import pygame
import numpy as np

HRES = 120 # horizontal resolution
HALFVRES = 100 #vertical resolution
MOD = HRES/60 #relation between hres and 60degrees FOV = scaling factor
posx,posy,rot = 0,0,0 #startign x and y pos for player and inital rotation


def floorcasting():
    #frame can contain widgets which make it easier to manipulate each pixel 
    #numpy.random.uniform gets random samples from uniform distribution and retruns them as a numpy array
    #(0,1,(output shape))
    frame = np.random.uniform(0,1,(150,90,3))
    #copies the array to a new surface
    surf = pygame.surfarray.make_surface(frame*255)#255-standard colour scale
    surf = pygame.transform.scale(surf,(1504,904))#use transform.scale to scale up the array to fit the whole window
    
    return surf 

def rotation():
    for i in range(HRES): # passes through all the columns in the screen
        rot_i = rot +np.deg2rad(i/MOD-30) #calculates the angle that represents the direction of each column in the frame
        sin,cos = np.sin(rot_i),np.cos(rot_i) #calculates sin and cos of these angles

    for j in range (HALFVRES): # passes through all the lines at the bottom of the screen
        n = HALFVRES/ (HALFVRES-j) # calculate distance from that point to the player #closest line ges distance of 1 line in midle tends to lareg value
        x , y = posx +cos*n,posy + sin*n #x and y of each pixel

        if int(x)%2 == int(y)%2:
            pass


