import pygame
from characters.player import Player
from characters.enemy import Enemy
import time
import math
from projectiles.bullet import Bullet
from projectiles.obstacle import Obstacle
from instructions.button_behavior.a_button import aButton
from instructions.button_behavior.d_button import dButton
from instructions.button_behavior.f_button import fButton
from instructions.button_behavior.s_button import sButton
from instructions.button_behavior.space_button import spaceButton
from card import Card


# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Pygame")
# set up variables for the display

jumping = False

size = (1200, 600)
screen = pygame.display.set_mode(size)
player = Player(200, 400, 300)
boss = Enemy(700, 100, 3000)

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
started = False
theta = 0
theta_display = my_font.render(f"{theta}°", True, (255, 255, 255))
cardinal_direction_display = my_font.render(f"{player.cardinal_direction_pointing}", True, (255, 255, 255))



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
card = Card((screen.get_width()/2), (screen.get_height()/2))
shooting = False
landing_coord = None
landing_coordinate = my_font.render(f"{landing_coord}", True, (255, 255, 255))
crouching = False

a_instruction = aButton(10, screen.get_height()-25*4 - 30)
d_instruction = dButton(10, screen.get_height()-25*3 - 30)
f_instruction = fButton(10, screen.get_height()-25*2 - 30)
s_instruction = sButton(10, screen.get_height()-25 - 30)
space_instruction = spaceButton(10, screen.get_height() - 30) # LOWER OPACITY

phase_one, phase_two, phase_three = False, False, False

timer_started = False
bullet_timer = 0

bullets = []
obstacles = []

frames = 0
player_collided = False
start_time = 0

timer_of_invincibility_player = 3

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


    if space_pressed and started:
        space_pressed = False
        jumping = True

    if started:
        if left_pressed:
            player.move_direction("left")
        elif right_pressed:
            player.move_direction("right")
        elif down_pressed:
                 # REPLACE WITH CROUCH FRAME, maybe make a list of booleans that is sliced from -2 and when it changes from true to false play the getting up animation
            crouching = True

    for event in pygame.event.get():  # User did something

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  
            shooting = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            shooting = False
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and not(started) and card.rect.collidepoint(event.pos):
            started = True

        if not(started):
            print()

        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    screen.fill((0, 0, 0))

    # START SCREEN
    if not(started):
        screen.blit(card.image, card.rect)
        Card.hover(card)
        Card.scale(card)


    if started:

        current_time = frames // 100

        if boss.hp >= (2/3)*boss.starting_hp:
            boss.phase_one = True
        elif boss.hp >= (1/3)*boss.starting_hp:
            boss.phase_one = False
            boss.phase_two = True
        else:
            boss.phase_two = False
            boss.phase_three = True

        if player.rect.colliderect(boss.rect) and not(player_collided):
            if not(timer_started):
                start_time = frames // 100
                timer_started = True
            
            player.hp -= 100
            player_collided = True

        if current_time - start_time == timer_of_invincibility_player: # Time of invincibility for player is 3 seconds
            timer_started = False
            player_collided = False


        for obstacle in obstacles:

            obstacle_collided = False

            if obstacle.rect.colliderect(player.rect) and not(obstacle_collided):
                player.hp -= 100
                obstacle_collided = True

            Obstacle.check_reached_coord_obstacle(obstacle)

            if not(obstacle.reached_coord) and not(obstacle.hp == 0):
                Obstacle.move_obstacle(obstacle)
            else:
                obstacles.pop(obstacles.index(obstacle))

        for bullet in bullets:

            bullet_collided = False 

            if bullet.rect.colliderect(boss.rect) and not(bullet_collided):
                # MAKE THE ENEMY LIGHT UP
                if boss.hp > 0:
                    boss.hp -= 10

                

                bullet_collided = True

            for obstacle in obstacles:
                bullet_collided_with_obstacle = False
                if bullet.rect.colliderect(obstacle.rect) and not(bullet_collided_with_obstacle):
                    obstacle.hp -= 10

            Bullet.check_reached_coord(bullet)
            Bullet.calc_landing_coords(bullet)

            bullet_current_time = frames // 100

            if not(bullet.reached_coord) and not(bullet_collided): # IF THE BULLET DID COLLIDE THEN WAIT A FEW SECONDS UNTIL SHOOTING THE NEXT
                Bullet.move_bullet(bullet)
            else:
                bullets.pop(bullets.index(bullet))


        screen.blit(a_instruction.image, a_instruction.rect)
        screen.blit(d_instruction.image, d_instruction.rect)
        screen.blit(f_instruction.image, f_instruction.rect)
        screen.blit(s_instruction.image, s_instruction.rect)
        screen.blit(space_instruction.image, space_instruction.rect)

        for obstacle in obstacles:
            screen.blit(obstacle.image, obstacle.rect)

        screen.blit(boss.image, boss.rect)

        if shooting:
            bullet_current_time = frames // 100
            bullet = Bullet((player.x, player.y), player.image_size, player.normalized_angle)
            Bullet.calc_landing_coords(bullet)
            if len(bullets) < 1: # CONFIGURATE BULLET SPACING 
                # NORMALIZE SHOOTING SPPED 
                bullet_timer = frames // 100 # ONLY ADDING WHEN IT IS SHOT
                bullets.append(Bullet((player.x, player.y), player.image_size, player.normalized_angle))

            landing_coordinate = my_font.render(f"{bullet.bullet_landing_coord}", True, (255, 255, 255))

        if boss.phase_one:
            obstacle_current_time = frames // 100
            obstacle = Obstacle((boss.x, boss.y), boss.image_size, 50)
            if len(obstacles) < 1: # CHANGE THIS TO A TIME DIFFERENCE
                obstacles.append(Obstacle((boss.x, boss.y), boss.image_size, 50))

        cardinal_direction_display = my_font.render(f"NA: {player.normalized_angle}°", True, (255, 255, 255))
        if not(f_pressed): # Lock the direction, ONLY UPDATE THE FRAME WHEN MOVING
            player.normalize_angle(angle_pointed)

        screen.blit(player.image, player.rect)
        screen.blit(theta_display, (20, 20))
        screen.blit(cardinal_direction_display, (60 , 20))
        screen.blit(landing_coordinate, (120, 20))

        for bullet in bullets:
                screen.blit(bullet.image, bullet.rect)
        
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
            if not(down_pressed):
                screen.blit(player.image, player.rect) # CHANGE TO STANDING
            jump_time_started = False
            if down_pressed:
                screen.blit(player.crouching_image, player.rect_crouching) # CHANGE TO CROUCHING

        print(boss.hp)
    frames += 1
    
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
