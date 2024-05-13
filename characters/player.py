import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/Initial_Character_Sprite.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = .25

    def move_direction(self, direction):
       if direction == "right":
           self.x += self.delta
           self.y -= self.delta
       elif direction == "left":
           self.x -= self.delta
           self.y += self.delta
       elif direction == "up":
           self.y += self.delta
           self.x += self.delta
       elif direction == "down":
           self.x -= self.delta
           self.y -= self.delta
       self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])