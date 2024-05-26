import pygame
import math

class Bullet:

    def __init__(self, player_coords, player_image_size, theta):
        self.x = player_coords[0] + player_image_size[0]/2
        self.y = player_coords[1] + player_image_size[1]/2

        self.player_image_size = player_image_size

        self.image = pygame.image.load("images/fx/particles/bullets/bullet/InitialBlast.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 5
        self.hypotenuse = 400
        self.bullet_landing_coord = (0, 0) #UPDATE
        self.player_coords = player_coords

        self.theta = theta


    def calc_landing_coords(self): # self.bullet_landing_coord

        x_delta = self.hypotenuse*math.cos(self.theta * (math.pi/180)) - self.image_size[0]/2
        y_delta = self.hypotenuse*math.sin(self.theta * (math.pi/180)) + self.image_size[1]/2

        player_center_x = self.player_coords[0] + self.player_image_size[0]/2
        player_center_y = self.player_coords[1] + self.player_image_size[1]/2

        self.bullet_landing_coord = (round(player_center_x + x_delta), round(player_center_y - y_delta))

        # MAKE A BOOLEAN TO TELL IF THE BULLET HAS REACHED THE COORD
