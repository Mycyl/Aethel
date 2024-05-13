import pygame
from characters.player import Player
from actions.user_roll import UserRoll

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Pygame")

roll_num = []
rolls = open("user_rolls", "r")
for w in rolls:
    roll_num.append(w.rstrip())
rolls = roll_num[0]

# set up variables for the display
size = (1200, 600)
screen = pygame.display.set_mode(size)
player = Player(0, 0)

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True

# -------- Main Program Loop -----------
while run:
    # --- Main event loop

    keys = pygame.key.get_pressed()

    up_pressed = keys[pygame.K_w]
    left_pressed = keys[pygame.K_a]
    down_pressed = keys[pygame.K_s]
    right_pressed = keys[pygame.K_d]

    if up_pressed:
        player.move_direction("up")
    if left_pressed:
        player.move_direction("left")
    if right_pressed:
        player.move_direction("right")
    if down_pressed:
        player.move_direction("down")

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    screen.fill((0, 0, 0))
    screen.blit(player.image, player.rect)
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
