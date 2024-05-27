import pygame

class spaceButton:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image_list = ["images/fx/buttons/up/space_button.png"] # add down button
        self.image = pygame.image.load("images/fx/buttons/up/space_button.png")
        self.image_size = self.image.get_size()
        self.rescale_image(self.image)
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def rescale_image(self, image):
        scale = 0.5
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * scale, self.image_size[1] * scale)
        self.image = pygame.transform.scale(self.image, scale_size)