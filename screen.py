import pygame
import consts
pygame.init()
size = (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("FLAG GAME!")

SCREEN_COLOR = (61,145,64)
screen.fill(SCREEN_COLOR)
pygame.display.flip()
'''  
img = pygame.image.load('bushes.png')
PURPLE = (103,17,136)
img.set_colorkey(PURPLE)
screen.blit(img, (-100,-200))
pygame.display.flip()
'''
finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True

pygame.quit()
pygame.quit()
