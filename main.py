import pygame
from characters.player import Player
from actions.user_roll import UserRoll
import time
import math

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
player = Player(200, 400)

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
started = False
theta = 0
theta_display = my_font.render(f"{theta}°", True, (255, 255, 255))
cardinal_direction_display = my_font.render(f"{player.cardinal_direction_pointing}", True, (255, 255, 255))

jumping = False

y_gravity = 0.5
jump_height = 15
jump_pause = 1 # second
y_velocity = jump_height
space_list = []
jump_pause_elapsed = True
jump_time_started = True
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while run:
    # --- Main event loop
    clock.tick(100)

    keys = pygame.key.get_pressed()
    angle_pointed = round(Player.theta(player))
    theta_display = my_font.render(f"{angle_pointed}°", True, (255, 255, 255))

    up_pressed = keys[pygame.K_w]
    down_pressed = keys[pygame.K_s]
    left_pressed = keys[pygame.K_a]
    right_pressed = keys[pygame.K_d]
    space_pressed = keys[pygame.K_SPACE]

    if space_pressed and not(started):
        started = True
    elif space_pressed and started:
        space_pressed = False
        jumping = True

    if started:
        if left_pressed:
            player.move_direction("left")
        elif right_pressed:
            player.move_direction("right")
        elif down_pressed:
            print() # REPLACE WITH CROUCH FRAME, maybe make a list of booleans that is sliced from -2 and when it changes from true to false play the getting up animation

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    screen.fill((0, 0, 0))
    if started:

        cardinal_direction_display = my_font.render(f"{player.cardinal_direction_pointing}", True, (255, 255, 255))
        player.get_dir(angle_pointed)

        screen.blit(player.image, player.rect)
        screen.blit(theta_display, (20, 20))
        screen.blit(cardinal_direction_display, (60 , 20))
        if jumping: # JUMPING MECHANICS
            player.y -= y_velocity
            y_velocity -= y_gravity
            if y_velocity < - jump_height:
                jumping = False
                y_velocity = jump_height
            player.rect = pygame.Rect(player.x, player.y, player.image_size[0], player.image_size[1])
            screen.blit(player.image, player.rect) # CHANGE TO JUMPING
        else:
            player.rect = pygame.Rect(player.x, player.y, player.image_size[0], player.image_size[1])
            screen.blit(player.image, player.rect) # CHANGE TO STANDING
            jump_time_started = False

    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
