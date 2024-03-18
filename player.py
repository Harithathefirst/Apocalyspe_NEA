import pygame
from settings import *
import math
from map import *
import sys
       
        #self.rotspeed = PLAYER_ROTATION_SPEED
m = Map()
#texture = Graphics()

class Player:
  def __init__(self):
    self.x,self.y = PLAYER_INITIAL_POS 
    self.speed = PLAYER_SPEED * delta_time #makes speed independent of frame rate for smoother movemnt
    self.x_change = 0
    self.y_change = 0 
    self.angle = PLAYER_ANGLE 
    self.rotspeed = PLAYER_ROTATION_SPEED
    #self.raycasting_result = []
    #self.objects_to_render = []
    #self.textures = self.texture.wall_textures()

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
    ox, oy = self.position_current #map coordinates
    x_map,y_map = self.position_map # players position on map grid line
    #texture_vert,texture_hor = 1,1
    #angle for first ray
    
    ray_angle = self.angle - HALF_FOV + 0.0001 #adding 0.0001 avoids dividing by 0 error
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




    #draws the player and a line from the front of the player
  def draw_player(self):
    #pygame.draw.line(surface,colour,start(x,y),end(x,y),width)
    pygame.draw.line(screen,RED,(self.x*100,self.y*100),
                      (self.x*100 + SCREEN_WIDTH* math.cos(self.angle),
                      self.y*100 + SCREEN_WIDTH* math.sin(self.angle)),2) #line coming fromplayer forward direction
    pygame.draw.circle(screen,GREEN,(self.x*100,self.y*100),15) #player represented as a green circle


  @property
  def position_current(self): #players current positiopn on map
        return self.x,self.y
  @property   
  def position_map(self): #returns map tile player is on 
        return int(self.x),int(self.y)
  
    
  def movement(self):
        self.dx = 0 #x axis movement
        self.dy = 0 #y axis movement
        sin_A = math.sin(self.angle) #calculates sin of the angle a
        cos_A = math.cos(self.angle)#cos angle a 
        
        keys = pygame.key.get_pressed()
                    #W - move forards
        if keys[pygame.K_w]:
                    self.dx += self.speed*cos_A
                    self.dy += self.speed*sin_A

            #A - move to the left
        elif keys[pygame.K_a]:
                    self.dx += self.speed*sin_A
                    self.dy += -(self.speed*cos_A)
            #S - move backwards
        elif keys[pygame.K_s]:
                    self.dx += -(self.speed*cos_A)
                    self.dy+= -(self.speed*sin_A)
            #D- move to the right
        elif keys[pygame.K_d]:
                    self.dx=-(self.speed*sin_A)
                    self.dy=(self.speed*cos_A)

        self.collision(self.dx,self.dy)
      #                 #rotation will be with mouse 
      #  if keys[pygame.K_LEFT]:
      #        self.angle -= self.rotspeed * delta_time #rotate to the left
      #  if keys[pygame.K_RIGHT]:
      #        self.angle += self.rotspeed * delta_time #rotate to the right
      #  self.angle %= 2 * math.pi #makes sure players angle stays between 0 and 360
  
        #  #rotation will be with mouse 
        MOUSE_X,MOUSE_Y = pygame.mouse.get_pos()
        if MOUSE_X < HALF_SCREEN_WIDTH - 100:
            self.angle -= PLAYER_ROTATION_SPEED * delta_time #rotate to the left
          #pygame.mouse.set_pos(HALF_SCREEN_WIDTH,HALF_SCREEN_HEIGHT)
        if MOUSE_X > HALF_SCREEN_WIDTH + 100 :
            self.angle += PLAYER_ROTATION_SPEED * delta_time #rotate to the right
          #pygame.mouse.set_pos(HALF_SCREEN_WIDTH,HALF_SCREEN_HEIGHT)
        self.angle %= 2 * math.pi #players angle shopuld remain between 0-360
        
        

          #rotate to the left
      #     if MOUSE_X > HALF_SCREEN_WIDTH:
      #         self.angle += PLAYER_ROTATION_SPEED  #rotate to the right
      # self.angle %= 2 * math.pi #players angle should remain between 0-360     
        


  
  def move_update(self):
      self.x += self.dx #adds on how much x has changed to players x coordinate
      self.y += self.dy #adds on how much y has changed to players y coordinate

  
  def check_wall(self,x,y): #takes in x and y coordniates 
      if (x,y) not in m.worldmap:#returns the coordinates of the player if it is not where there is 1 on map - a wall
          return (x,y)


  def collision(self,x,y): 
      if self.check_wall(int(self.x + self.dx),int(self.y)): #allows movement on the x axis if x coordinate is not at a wall 
            self.x += self.dx #adds on the calculated x change - can move in x direction
      if self.check_wall(int(self.x),int(self.y + self.dy)): #allows movement if y coordinate is not at a wall
            self.y += self.dy #adds on calculated y change -can move in y direction















    # def movement1(self):
    #     self.x_change = 0
    #     self.y_change = 0

    #     keys = pygame.key.get_pressed()
    #              #W - move forards  
    #     if keys[pygame.K_w]:
    #         self.x_change += 0
    #         self.y_change += -self.speed

    #          #A - move to the left
    #     elif keys[pygame.K_a]:
    #         self.x_change += -self.speed
    #         self.y_change += 0
    #          #S - move backwards
    #     elif keys[pygame.K_s]:
    #         self.x_change += 0
    #         self.y_change += self.speed
    #          #D- move to the right
    #     elif keys[pygame.K_d]:
    #         self.x_change=self.speed
    #         self.y_change= 0
         

    #              #rotation will be with mouse 
    #     if keys[pygame.K_LEFT]:
    #           self.angle -= self.rotspeed * delta_time #rotate to the left
    #     if keys[pygame.K_RIGHT]:
    #           self.angle += self.rotspeed * delta_time #rotate to the right
    #     self.angle %= 2 * math.pi #makes sure players angle stays between 0 and 360

         
    
    
    # def move_update1(self):
    #      self.x += self.x_change #adds on how much x has changed to players x coordinate
    #      self.y += self.y_change #adds on how much y has changed to players y coordinate


























      
    # def movement_yt(self):
    #     sin_A = math.sin(self.angle) #calculates sin of the angle a
    #     cos_A = math.cos(self.angle)#cos angle a  
    #     dx,dy = 0,0 #initial coordinates
    #     speed = PLAYER_SPEED * delta_time #speed of the player independent of the frame rate

    #     keys = pygame.key.get_pressed() #gets the state of all keyboard buttons
    #     #calculates like a diagonal
    #     if keys[pygame.K_w]:
    #         #move in the forward direction
    #        dx += speed*cos_A 
    #        dy += speed*sin_A
    #     elif keys[pygame.K_a]:
    #         #move in the left direction
    #         dx += speed*sin_A
    #         dy += -(speed*cos_A)
    #     elif keys[pygame.K_s]:
    #        #move in the backward direction
    #        dx += -(speed*cos_A)
    #        dy += -(speed*sin_A)
    #     elif keys[pygame.K_d]:
    #        #move in the right direction
    #        dx+= -(speed*sin_A)
    #        dy+= speed*cos_A

    #     #self.x += dx #adds on moveemnt to initial player y pos
    #     #self.y += dy #adds on movement to initial player x pos
    #     self.collision(dx,dy)
    #     for event in pygame.event.get():
    #             #if event.type == pygame. MOUSEBUTTONDOWN:
    #             (MOUSE_X,MOUSE_Y) = pygame.mouse.get_pos()
    #             #rotation will be with mouse 
    #             if MOUSE_X < HALF_SCREEN_WIDTH:
    #                 self.angle -= PLAYER_ROTATION_SPEED  #rotate to the left
    #             if MOUSE_X > HALF_SCREEN_WIDTH:
    #                 self.angle += PLAYER_ROTATION_SPEED  #rotate to the right
    #             self.angle %= 2 * math.pi #players angle should remain between 0-360          


    # def collision1(self,dx,dy): #takes in the players calculated dx and dy
    #       if self.check_wall(int(self.x + dx),int(self.y)): #allows movement on the x axis if 
    #         #x coordinate is not at a wall 
    #           self.x += dx #adds on the calculated dx - can move in x direction
    #       if self.check_wall(int(self.x),int(self.y + dy)): #allows movement if y coordinate is not at a wall
    #           self.y += dy #adds on calculated dy -can move in y direction 




























































          
         
# m = Map()

# while True:
#     for event in pygame.event.get():
#           if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#     m.draw_map()
#     pygame.display.flip()



 
      
""" def raycasting(self):
    #define the starting angle - left most ray
          start_angle  = self.angle + HALF_FOV + 0.0001

    # loop over total rays from player
          for ray in range(10):
        #cast ray step by step
            for depth in range (MAX_DEPTH):
            #target x coordinate of wall
            #get ray target coordinates
                  target_x = self.x*100 + math.sin(start_angle) * depth*100
                  if int(target_x) in m.worldmap:
                        break
                  target_x = self.x*100 + math.sin(start_angle)*depth*100
                  target_y = self.y*100 + math.cos(start_angle) * depth*100
                  if int(target_y) in m.worldmap:
                        break
                  target_y = self.y*100 + math.cos(start_angle) * depth*100
                  

            pygame.draw.line(screen,'yellow',(self.x*100,self.y*100),
                    (target_x,target_y))
            
    #increment angle by single step of ray 
            start_angle += DELTA_ANGLE
            print(target_x)
            print(target_y) """


#def draw_player(self):
 #     #pygame.draw.line(surface,colour,start(x,y),end(x,y),width)
  #    pygame.draw.circle(screen,GREEN,(self.x*100,self.y*100),15)
   #   pygame.draw.line(screen,'yellow',(self.x*100,self.y*100),
    #                   (self.x*100 + math.sin(self.angle) * 50,self.y*100 + math.cos(self.angle) * 50),2)
      #draw FOV
     # pygame.draw.line(screen,'yellow',(self.x*100,self.y*100),
      #                  (self.x*100 + math.sin(self.angle - HALF_FOV) * 50,self.y*100 + math.cos(self.angle - HALF_FOV) * 50),2)
      
      #pygame.draw.line(screen,'yellow',(self.x*100,self.y*100),
       #                 (self.x*100 + math.sin(self.angle + HALF_FOV) * 50,self.y*100 + math.cos(self.angle + HALF_FOV) * 50),2)
        