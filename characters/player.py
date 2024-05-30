import pygame
import math

class Player:
    def __init__(self, x, y, hp):
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/characters/player/Initial_Character_Sprite.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 5
        self.jumping = False
        self.cardinal_direction_pointing = "N"
        self.normalized_angle = 90
        self.hp = hp

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
    

    def normalize_angle(self, angle_pointed):
        angles = [[0, 36], [36, 72], [72, 108], [108, 144], [144, 180], [180, 216], [216, 252], [252, 288], [288, 324], [324, 360]]
        cardinal_directions = ["E", "NE", "N", "NW", "W", "W", "SW", "S", "SE", "E"]
        for i in range(len(angles)):
            if angle_pointed > angles[i][0] and angle_pointed <= angles[i][1]:
                self.cardinal_direction_pointing = cardinal_directions[i]
        normalized_angles = [0, 45, 90, 135, 180, 180, 225, 270, 315, 0]
        self.normalized_angle = normalized_angles[cardinal_directions.index(self.cardinal_direction_pointing)]


