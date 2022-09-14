import pygame
import screen
import consts


soldier_image = pygame.image.load('soldier.png.png')
soldier_image = pygame.transform.scale(soldier_image, (consts.SOLDIER_WIDTH,consts.SOLDIER_HEIGHT))

def soldier_moving():
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_RIGHT]:
        soldier.x += consts.VEL
    elif keys_pressed[pygame.K_UP]:
        soldier.y -= consts.VEL
    elif keys_pressed[pygame.K_LEFT]:
        soldier.x -= consts.VEL
    elif keys_pressed[pygame.K_DOWN]:
        soldier.y += consts.VEL

#def soldier_in_frame():

soldier = pygame.Rect(0,0,consts.SOLDIER_WIDTH,consts.SOLDIER_HEIGHT)
