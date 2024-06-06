import pygame

class Card:
    def __init__(self, x, y):
        self.image = pygame.image.load("images/starting_screen/card/InitialLevelCard.png")
        self.rescale_image()
        self.image_size = self.image.get_size()
        self.x = x - self.image_size[0]/2
        self.y = y - self.image_size[1]/2
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.mouse_pos=(0,0)
        self.hovering = False

    def hover(self):
        self.mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(self.mouse_pos):
            self.hovering = True
        else:
            self.hovering = False

    def rescale_image(self):
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * .7, self.image_size[1] * .7)
        self.image = pygame.transform.scale(self.image, scale_size)

    def scale(self):
        if self.hovering:
            print("hovering")
        else:
            print("not hovering")
    
