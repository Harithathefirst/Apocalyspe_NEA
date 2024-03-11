import pygame
import math #access sin and cos
from settings import *
from player import *


player = Player() #make instance of player

            
 
def raycast():
        ox, oy = player.position_current #map coordinates
        x_map,y_map = player.position_map # players position on map grid line
        #angle for first ray
        ray_angle = player.angle - HALF_FOV + 0.0001 #adding 0.0001 avoids dividing by 0 error
         
        for ray in range(NUM_RAYS):
            sin_ray_angle = math.sin(ray_angle) #sin of current ray
            cos_ray_angle = math.cos(ray_angle) #cosine of current ray

            #calculates where horizontal ray intersects grid lines
            #same as vertical but flip the signs 
            #dy = 1 on grid
            #y_hor is where ray intersects horizontal grid lines
            y_hor, dy = (y_map + 1, 1) if sin_ray_angle > 0 else (y_map - 1e-6,-1)
            #length of ray to reach y_hor
            depth_hor = (y_hor - oy) / sin_ray_angle
            #valeu of x coordinate
            x_hor = ox + depth_hor * cos_ray_angle

            delta_depth  = dy/sin_ray_angle  #opp/sin = hyp
            dx = delta_depth * cos_ray_angle #hyp*cos = adj
          #casts ray in steps to maxdepth=20
            for i in range(MAX_DEPTH):
               #horizontal ray
               tile_hor = int(x_hor),int(y_hor)
                #stops ray if hit wall
               if tile_hor in m.worldmap:
                    break
               #otherwise continue casting ray 
               x_hor += dx
               y_hor += dy
               #horizontal ray depth
               depth_hor += delta_depth

          #calculate where the ray intersects the grids vertical lines
            #dx = 1 on grid 
            #xvert is where ray intersects vertical grid line
            x_vert, dx = (x_map + 1, 1) if cos_ray_angle > 0 else (x_map - 1e-6,-1) #1e-6 = 1x10^-6
            #length of ray to reach x vert 
            depth_vert = (x_vert - ox) / cos_ray_angle
            #value of y coordinate
            y_vert = oy + depth_vert * sin_ray_angle

            delta_depth = dx/cos_ray_angle #adj/cos = hyp
            dy = delta_depth * sin_ray_angle #hyp*sin

            #cast ray in cycle of number of steps 20
            for i in range(MAX_DEPTH):
               #vertical ray
               tile_vert = int(x_vert),int(y_vert)
               #stops drawing ray if it hits wall
               if tile_vert in m.worldmap:
                    break
               #ray continues if not
               x_vert += dx
               y_vert += dy
               #vertical total ray depth
               depth_vert += delta_depth
             #calculates whichever ray is shorter and assigns this to depth   
            if depth_vert < depth_hor:
                 depth = depth_vert
            else:
                 depth = depth_hor
                 
            #ray will be drawn using depth as the ray line
            pygame.draw.line(screen,'yellow',(100*ox,100*oy),
                          (100 * ox + 100 * depth * cos_ray_angle, 100 * oy + 100 * depth * sin_ray_angle),2)    

            ray_angle += DELTA_ANGLE