import pygame
import sys
import math #access sin and cos
from settings import *
from player import *


player = Player()

def raycast():
    ox, oy = player.position_current #players current position on the map
    x_map,y_map = player.position_map
    ray_angle = PLAYER_ANGLE - HALF_FOV + 0.0001 #adding 0.0001 avoids dividing by 0 error

    for ray in range(NUM_RAYS):
          sin_ray_angle = math.sin(ray_angle)
          cos_ray_angle = math.cos(ray_angle)

          #calculate where the ray intersects the grids vertical lines
          ray_angle += DELTA_ANGLE
      

