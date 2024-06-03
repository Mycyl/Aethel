import pygame

class Henchman:
    def __init__(self, boss_x, boss_y, boss_image_size): # SUMMONS THE HENCHMEN
        self.x = boss_x
        self.image = pygame.image.load("images/projectiles/henchmen/InitialHenchman.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.y = boss_y + boss_image_size[1] - self.image_size[1]
        self.delta = 10

    def move_henchman(self):
        self.x -= self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])