import pygame
from characters.player import Player
import time
import math
from projectiles.bullet import Bullet
from instructions.button_behavior.a_button import aButton
from instructions.button_behavior.d_button import dButton
from instructions.button_behavior.f_button import fButton
from instructions.button_behavior.s_button import sButton
from instructions.button_behavior.space_button import spaceButton


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
player_coords = (0,0)
theta = 0
bullet = Bullet(player_coords, player.image_size, theta)
shooting = False
bullets = []
landing_coord = None
landing_coordinate = my_font.render(f"{landing_coord}", True, (255, 255, 255))
crouching = False

a_instruction = aButton(10, screen.get_height()-25*4 - 30)
d_instruction = dButton(10, screen.get_height()-25*3 - 30)
f_instruction = fButton(10, screen.get_height()-25*2 - 30)
s_instruction = sButton(10, screen.get_height()-25 - 30)
space_instruction = spaceButton(10, screen.get_height() - 30) # LOWER OPACITY

# -------- Main Program Loop -----------
while run:
    # --- Main event loop
    clock.tick(100)

    
    keys = pygame.key.get_pressed()
    angle_pointed = round(Player.theta(player))
    theta_display = my_font.render(f"{angle_pointed}°", True, (255, 255, 255))

    f_pressed = keys[pygame.K_f]
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
            (print) # REPLACE WITH CROUCH FRAME, maybe make a list of booleans that is sliced from -2 and when it changes from true to false play the getting up animation
            crouching = True

    for event in pygame.event.get():  # User did something

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  
            shooting = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            shooting = False

        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    screen.fill((0, 0, 0))
    if started:

        screen.blit(a_instruction.image, a_instruction.rect)
        screen.blit(d_instruction.image, d_instruction.rect)
        screen.blit(f_instruction.image, f_instruction.rect)
        screen.blit(s_instruction.image, s_instruction.rect)
        screen.blit(space_instruction.image, space_instruction.rect)

        if shooting:
            bullet = Bullet((player.x, player.y), player.image_size, player.normalized_angle)
            Bullet.calc_landing_coords(bullet)
            screen.blit(bullet.image, pygame.Rect(bullet.bullet_landing_coord[0], bullet.bullet_landing_coord[1], bullet.image_size[0], bullet.image_size[1]))
            for bullet in bullets:
                print()
            landing_coordinate = my_font.render(f"{bullet.bullet_landing_coord}", True, (255, 255, 255))

        cardinal_direction_display = my_font.render(f"NA: {player.normalized_angle}°", True, (255, 255, 255))
        if not(f_pressed): # Lock the direction, ONLY UPDATE THE FRAME WHEN MOVING
            player.normalize_angle(angle_pointed)

        screen.blit(player.image, player.rect)
        screen.blit(theta_display, (20, 20))
        screen.blit(cardinal_direction_display, (60 , 20))
        screen.blit(landing_coordinate, (120, 20))
        
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
            if down_pressed:
                screen.blit(player.image, player.rect) # CHANGE TO CROUCHING

    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
