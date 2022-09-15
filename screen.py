import pygame
import consts
import random
import os
import soldier
import MineField


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
    for i in range(len(locations)):
        bush_picture = pygame.image.load('bush.png')
        bush = pygame.transform.scale(bush_picture, (consts.BUSHES_SIZE))
        SCREEN.blit(bush, (locations[i][0], locations[i][1]))


def opening_screen():
    SCREEN.fill(consts.SCREEN_COLOR)
    create_bushes()
    SCREEN.blit(soldier.soldier_image, (soldier.soldier.x,soldier.soldier.y))
    pygame.display.update()


def when_enter_pressed():
    SCREEN. fill(consts.SCREEN_ENTER_COLOR)
    grid_create()
    add_mine_grid()
    pygame.display.update()

def grid_create():
    x_rate = 0
    y_rate = 0
    for i in range(consts. COLUMN) :
        x_rate += consts.DISTANCE_BTW_ROWS
        y_rate += consts.DISTANCE_BTW_ROWS
        pygame.draw.line(SCREEN, (0, 139, 0), (x_rate, 0), (x_rate, consts.WINDOW_HEIGHT))
        pygame.draw.line(SCREEN, (0, 139, 0), (0, y_rate), (consts.WINDOW_WIDTH, y_rate))


LIST = MineField.mines_location(consts.MINEFIELD)
def add_mine_grid():
    for i in range(0,len(LIST), 3):
        mine_picture = pygame.image.load('mine.png')
        MINE = pygame.transform.scale(mine_picture, (consts.MINE_SIZE))
        SCREEN.blit(MINE, (LIST[i][1] * 20, LIST[i][0]* 20)) #y = row, col = x

#def add_soldier():







def draw_lose_message():
    draw_message(consts.LOSE_MESSAGE, consts.LOSE_FONT_SIZE,
                 consts.LOSE_COLOR, consts.LOSE_LOCATION)


def draw_win_message():
    draw_message(consts.WIN_MESSAGE, consts.WIN_FONT_SIZE,
                 consts.WIN_COLOR, consts.WIN_LOCATION)


def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    SCREEN.blit(text_img, location)
