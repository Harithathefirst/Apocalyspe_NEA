import pygame
import math #access sin and cos
from settings import *
from player import *


#player = Player() #make instance of player


class Raycasting:
  def __init__(self,player):
    self.player = Player()
    self.map = Map()
    
def render(self):
    self.objects_to_render = []
    for ray, values in enumerate(self.raycasting_result):
      depth, projection_height, texture,offset = values

    wall_column = self.textures[texture].subsurface   (
    offset * (TEXTURE_SIZE - SCALE), 0, SCALE, TEXTURE_SIZE
              )
    wall_column = pygame.transform.scale(wall_column, (SCALE,projection_height))
    wall_pos = (ray * SCALE, HALF_SCREEN_HEIGHT - projection_height // 2)

    self.objects_to_render.append((depth, wall_column, wall_pos))
    
def raycast(self):
    # self.raycasting_result = []
    ox, oy = self.player.position_current #map coordinates
    x_map,y_map = self.player.position_map # players position on map grid line
    #texture_vert,texture_hor = 1,1
    #angle for first ray
    
    ray_angle = self.player.angle - HALF_FOV + 0.0001 #adding 0.0001 avoids dividing by 0 error
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
        #texture_hor = m.worldmap[tile_hor]
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
        # texture_vert = m.worldmap[tile_vert]
          break
        #ray continues if not
        x_vert += dx
        y_vert += dy
        #vertical total ray depth
        depth_vert += delta_depth

        #calculates whichever ray is shorter and assigns this to depth   
      if depth_vert < depth_hor:
        depth = depth_vert
        #depth,texture = depth_vert, texture_vert
        #y_vert &= 1
        #offset = y_vert if cos_ray_angle > 0 else (1 - y_vert)
      else:
        depth = depth_hor
        #depth,texture = depth_hor, texture_hor
        #x_hor %= 1
        #offset = (1 - x_hor) if sin_ray_angle > 0 else x_hor

      #remove close fishbowl effect
      depth *= math.cos(self.angle - ray_angle)
                  

      projection_height = WALL_DIST / (depth + 0.0001) #height of space between ray  #+0.0001 to avoid /0 error

      #raycastign result
      #self.raycasting_result.append((depth,projection_height,texture,offset))

      #  #draw walls
      shade_colour = [255 / (1 + depth ** 6 * 0.00002)] * 3 #makes further away walls darker
      pygame.draw.rect(screen, shade_colour,
                      (ray * SCALE,HALF_SCREEN_HEIGHT - projection_height//2,SCALE,projection_height)) #places rectangle according to the number of the ray on x axis and places in center of screen

      # # #ray will be drawn using depth as the ray line
      # pygame.draw.line(screen,'yellow',(100*ox,100*oy),
      #                   (100 * ox + 100 * depth * cos_ray_angle, 100 * oy + 100 * depth * sin_ray_angle),2)    

      ray_angle += DELTA_ANGLE















