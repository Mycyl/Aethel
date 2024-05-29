import pygame
import math

class Bullet:

    def __init__(self, player_coords, player_image_size, theta):
        

        self.player_image_size = player_image_size

        self.image = pygame.image.load("images/fx/particles/bullets/bullet/InitialBlast.png")
        self.image_size = self.image.get_size()
        self.x = player_coords[0] + player_image_size[0]/2 - self.image_size[0]/2
        self.y = player_coords[1] + player_image_size[1]/2 - self.image_size[1]/2
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 5
        self.hypotenuse = 400
        self.bullet_landing_coord = (0, 0) #UPDATE
        self.player_coords = player_coords

        

        self.reached_coord_x = False # CHANGE TO TRUE IF X AND Y HAVE PASSED OR ARE EQUAL TO LANDING COORD
        self.reached_coord_y = False
        self.reached_coord = False

        self.theta = theta

        self.adjacent = 0
        self.opposite = 0

    def calc_landing_coords(self): # self.bullet_landing_coord

        x_delta = self.hypotenuse*math.cos(self.theta * (math.pi/180)) - self.image_size[0]/2
        y_delta = -(self.hypotenuse*math.sin(self.theta * (math.pi/180)) + self.image_size[1]/2)

        absolute_cardinal_directions = [0, 90, 180, 270]

        if not(self.theta in absolute_cardinal_directions):
            self.adjacent = x_delta
            self.opposite = y_delta
        else:
            if self.theta == 0:
                self.adjacent = x_delta
                self.opposite = 0
            elif self.theta == 90:
                self.adjacent = 0
                self.opposite = y_delta
            elif self.theta == 180:
                self.adjacent = x_delta
                self.opposite = 0
            elif self.theta == 270:
                self.adjacent = 0
                self.opposite = y_delta
        
        player_center_x = self.player_coords[0] + self.player_image_size[0]/2
        player_center_y = self.player_coords[1] + self.player_image_size[1]/2

        self.bullet_landing_coord = (round(player_center_x + x_delta), round(player_center_y + y_delta))

        # MAKE A BOOLEAN TO TELL IF THE BULLET HAS REACHED THE COORD

    def move_bullet(self):

        if self.adjacent > 0:
            self.x += self.delta

            if self.x >= self.bullet_landing_coord[0]:
                self.reached_coord_x = True

        elif self.adjacent < 0:
            self.x -= self.delta

            if self.x <= self.bullet_landing_coord[0]:
                self.reached_coord_x = True

        else:
            self.reached_coord_x = True
            

        if self.opposite < 0:
            self.y -= self.delta

            if self.y <= self.bullet_landing_coord[1]:
                self.reached_coord_y = True


        elif self.opposite > 0:
            self.y += self.delta

            if self.y >= self.bullet_landing_coord[1]:
                self.reached_coord_y = True

        else:
            self.reached_coord_y = True

        

        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
    
    def check_reached_coord(self):
        if self.reached_coord_x and self.reached_coord_y:
            self.reached_coord = True

