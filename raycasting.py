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
          x_vert, dx = (x_map + 1, 1) if cos_ray_angle > 0 else (x_map - 1e-6,-1)
          depth_vert = (x_vert - ox) / cos_ray_angle
          y_vert = oy + depth_vert*sin_ray_angle

          vertical_depth = dx/cos_ray_angle
          dy =vertical_depth*sin_ray_angle

          for i in range(MAX_DEPTH):
               tile_vert = int(x_vert),int(y_vert)
               if tile_vert in m.worldmap:
                    break
               else:
                x_vert += dx 
                y_vert += dy
                depth_vert += vertical_depth
          
          ray_angle += DELTA_ANGLE
      

