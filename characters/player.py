import pygame
import math

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/Initial_Character_Sprite.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 5
        self.jumping = False

    def move_direction(self, direction):
       if direction == "right":
           self.x += self.delta
       elif direction == "left":
           self.x -= self.delta
       elif direction == "up":
           self.y -= self.delta
       elif direction == "down":
           self.y += self.delta
       self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def theta(self):
        center_coords_player = (self.x + self.image_size[0]/2, self.y + self.image_size[1]/2)
        mouse_pos = pygame.mouse.get_pos()
        opposite, adjacent = -(mouse_pos[1] - center_coords_player[1]), mouse_pos[0] - center_coords_player[0]
        if adjacent != 0:
            theta = (math.atan(opposite/adjacent)) * (180/math.pi)
            if theta < 0:
                angle = 180 + theta
            else:
                angle = theta
        else:
            angle = 90
        if opposite >= 0:
            return angle
        return 180 + angle 
            


