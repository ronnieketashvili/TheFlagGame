import pygame
import consts
import os

pygame.init()
size = (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT)
SCREEN = pygame.display.set_mode(size)
pygame.display.set_caption("FLAG GAME!")

bush_picture = pygame.image.load(os.path.join('bush.png'))
bush = pygame.transform.scale(bush_picture, (400,200))
SCREEN.blit(bush, (100, 100))




'''     
img = pygame.image.load('bushes.png')
PURPLE = (103,17,136)
img.set_colorkey(PURPLE)
screen.blit(img, (-100,-200))
pygame.display.flip()
'''
