import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/Initial_Character_Sprite.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = .25
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

    def jump(self):
        mass = 1
        velocity = 0.2
        keys = pygame.key.get_pressed()
        if not(self.jumping):
            if keys[pygame.K_SPACE]:
                self.jumping = True
        if self.jumping:
            Force = (1 / 2) * mass * (velocity ** 2)
            self.y -= Force
            velocity -= 1
            if velocity < 0:
                mass *= -1
            if velocity == -5:
                self.jumping = False
                mass = 1
                velocity = 5
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

