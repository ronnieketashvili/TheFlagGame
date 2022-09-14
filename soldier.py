import pygame
import screen
import consts


soldier_image = pygame.image.load('soldier.png.png')
soldier_image = pygame.transform.scale(soldier_image, (consts.SOLDIER_WIDTH,consts.SOLDIER_HEIGHT))

soldier = pygame.Rect(0,0,consts.SOLDIER_WIDTH,consts.SOLDIER_HEIGHT)
