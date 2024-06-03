import pygame

class Enemy:

    def __init__(self, x, y, hp):
        self.phase_one = False
        self.phase_two = False
        self.phase_three = False
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/characters/enemy/InitialEnemy.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.starting_hp = hp
        self.hp = hp
        self.attack = "Obstacles"

    def phase_attack(self):

        if self.phase_two:
            self.attack = "Henchmen"
        elif self.phase_three:
            self.attack = "Combined"