import pygame
from settings import *
from player import Player





class Graphics:
    def __init__(self):
        self.screen = screen
        self.wall_textures = self.render_texture()

    def draw(self):
        self.render_game_obj()
    
    def render_game_obj(self):
        list_objects = self.p.raycast.objects_to_render
        for depth, image, pos, in list_objects:
            self.screen.blit(image,pos)

    @staticmethod
    def get_texture(path,text_res = (TEXTURE_SIZE,TEXTURE_SIZE)):
        wall = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(wall,text_res)

    def render_texture(self):
        return {
            1: self.get_texture('wall metal.jpg')
        }

# Resources = {
    
# }

# textures
# wall1 = pygame.image.load('wall metal.jpg').convert()
# textures = {
#     '1': pygame.image.load('wall metal.jpg').convert(),
    
#}