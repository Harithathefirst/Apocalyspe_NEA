import pygame
import sys
import math #access sin and cos
from settings import *
from player import *


player = Player() #make instance of player

def raycast():
    ox, oy = player.position_current #map coordinates
    x_map,y_map = player.position_map # players position on map grid lines
    #angle for first ray
    ray_angle = PLAYER_ANGLE - HALF_FOV + 0.0001 #adding 0.0001 avoids dividing by 0 error 

    for ray in range(NUM_RAYS):
          sin_ray_angle = math.sin(ray_angle) #sin of current ray
          cos_ray_angle = math.cos(ray_angle) #cosine of current ray

          #horizontal ray intersects
          y_hor, dy = (y_map + 1, 1) if sin_ray_angle > 0 else (y_map - 1e-6,-1)
          depth_hor = (y_hor - oy) / sin_ray_angle
          x_hor = ox + depth_hor*cos_ray_angle

          delta_depth  = dy/sin_ray_angle
          dx = delta_depth * cos_ray_angle
          
          for i in range(MAX_DEPTH):
               tile_hor = int(x_hor),int(y_hor)
          if tile_hor in m.worldmap:
                    break
          x_hor += dx
          y_hor += dy
          depth_hor += delta_depth

          #calculate where the ray intersects the grids vertical lines
          x_vert, dx = (x_map + 1, 1) if cos_ray_angle > 0 else (x_map - 1e-6,-1) #1e-6 = 1x10^-6 
          depth_vert = (x_vert - ox) / cos_ray_angle
          y_vert = oy + depth_vert*sin_ray_angle

          delta_depth = dx/cos_ray_angle
          dy = delta_depth * sin_ray_angle

          for i in range(MAX_DEPTH):
               tile_vert = int(x_vert),int(y_vert)
          if tile_vert in m.worldmap:
                    break
          x_vert += dx
          y_vert += dy
          depth_vert += delta_depth
                
          if depth_vert < depth_hor:
                 depth == depth_vert
          elif depth_hor<depth_vert:
                 depth = depth_hor

          pygame.draw.line(screen,'yellow',(100*ox,100*oy)),(100*ox + 100 * depth *cos_ray_angle,100 *oy +100 * depth *sin_ray_angle,2)
    

          ray_angle += DELTA_ANGLE
      

