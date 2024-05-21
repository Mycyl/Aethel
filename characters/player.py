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
        self.cardinal_direction_pointing = "N"

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
            theta = (math.atan(opposite/adjacent)) * (180/math.pi) # Angle calculation
            if theta < 0: # Dealing with extraneous cases
                angle = 180 + theta
            else:
                angle = theta
        else:
            angle = 90
        if opposite >= 0: 
            if angle == 0 and adjacent < 0:
                return 180
            return angle
        return 180 + angle 
        
    def get_dir(self, angle_pointed):
        if angle_pointed <= 36 or angle_pointed > 270:
            self.cardinal_direction_pointing = "E" # TOUCH UP ON THIS
        elif angle_pointed > 36 and angle_pointed <= 72:
            self.cardinal_direction_pointing = "NE"
        elif angle_pointed > 72 and angle_pointed <= 108:
            self.cardinal_direction_pointing = "N"
        elif angle_pointed > 108 and angle_pointed <= 144:
            self.cardinal_direction_pointing = "NW"
        elif angle_pointed > 144 and angle_pointed <= 270:
            self.cardinal_direction_pointing = "W"


