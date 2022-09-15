import pygame
import consts
import random
import os
import soldier
pygame.init()
SCREEN = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
pygame.display.set_caption("FLAG GAME!")

def bushes_locations():
    locations_list = []
    for i in range(consts.BUSHES_NUMBER):
        x_rate = random.randint(0, 780)
        y_rate = random.randint(consts.SOLDIER_HEIGHT, 440)
        locations_list.append((x_rate, y_rate))
    return locations_list

locations = []
locations = bushes_locations()

def create_bushes():
    global locations
    for i in range(len(locations)):
        bush_picture = pygame.image.load('bush.png')
        bush = pygame.transform.scale(bush_picture, (consts.BUSHES_SIZE))
        SCREEN.blit(bush, (locations[i][0], locations[i][1]))
def opening_screen():
    SCREEN.fill(consts.SCREEN_COLOR)
    create_bushes()
    SCREEN.blit(soldier.soldier_image, (soldier.soldier.x, soldier.soldier.y))
    pygame.display.update()

def when_enter_pressed():


