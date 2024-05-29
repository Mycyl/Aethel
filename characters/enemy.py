import pygame

class Enemy:

    def __init__(self, x, y, hp):
        
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/characters/enemy/InitialEnemy.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.starting_hp = hp
        self.hp = hp