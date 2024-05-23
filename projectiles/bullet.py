import pygame
import math

class Bullet:
    def __init__(self, player_coords, theta):
        self.x = player_coords[0]
        self.y = player_coords[1]
        self.image = pygame.image.load("images/InitialBlast.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 5
        self.hypotenuse = 10
        self.bullet_landing_coord = (0, 0) #UPDATE
        self.player_coords = player_coords
        self.theta = theta

    def calc_landing_coords(self):
        x_delta = self.hypotenuse*math.cos(self.theta)
        y_delta = self.hypotenuse*math.sin(self.theta)
        self.bullet_landing_coord = (self.player_coords[0] + x_delta, self.player_coords[1]+y_delta)

        # MAKE A BOOLEAN TO TELL IF THE BULLET HAS REACHED THE COORD
