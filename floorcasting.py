import pygame
import numpy as np



def floorcasting():
    frame = np.random.uniform(0,1,(150,90,3))

    surf = pygame.surfarray.make_surface(frame*255)
    surf = pygame.transform.scale(surf,(1504,904))
    
    return surf
