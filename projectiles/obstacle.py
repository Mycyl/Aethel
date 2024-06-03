import pygame
import random

class Obstacle:

    def __init__(self, boss_coords, boss_image_size, y): # boss_image_size: (width, length)

        self.image = pygame.image.load("images/projectiles/obstacles/obstacle/obstacle.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.x = boss_coords[0]
        self.y = random.randint(boss_coords[1], boss_coords[1] + boss_image_size[1] - self.image_size[0])
    
        self.reached_coord = False
        self.delta = 10

    def check_reached_coord_obstacle(self):
        if self.x <= 0:
            self.reached_coord = True
        
    def move_bullet(self):
        self.x -= self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])