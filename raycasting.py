import pygame
import sys
import math #access sin and cos
from settings import *

def raycast():
    ray_angle = PLAYER_ANGLE - HALF_FOV + 0.0001 #adding 0.0001 avoids dividing by 0 error
    for ray in range(NUM_RAYS):
        ox, oy = 0,0
        ray_angle += DELTA_ANGLE

