import pygame
import screen
import consts


soldier_image = pygame.image.load('soldier.png.png')
soldier_image = pygame.transform.scale(soldier_image, (consts.SOLDIER_WIDTH,consts.SOLDIER_HEIGHT))

def soldier_moving():
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_RIGHT] and soldier.x + consts.VEL + consts.SOLDIER_WIDTH < BORDER.x:
        soldier.x += consts.VEL
    if keys_pressed[pygame.K_UP] and soldier.y - consts.VEL > 0:
        soldier.y -= consts.VEL
    if keys_pressed[pygame.K_LEFT] and soldier.x - consts.VEL > 0:
        soldier.x -= consts.VEL
    if keys_pressed[pygame.K_DOWN] and soldier.y + consts.VEL + consts.SOLDIER_HEIGHT < BORDER.y:
        soldier.y += consts.VEL

BORDER = pygame.Rect(1000,500,consts.WINDOW_WIDTH,consts.WINDOW_HEIGHT)

def soldier_in_matrix():
    soldier_moving()
    soldier_col = soldier.x / 20
    soldier_row = soldier.y / 20
    if consts.MINEFIELD[int(soldier_row) + 4 ][int(soldier_col) + 1] == 'mine':
        screen.draw_lose_message()
        consts.FINISH = True
    elif consts.MINEFIELD[int(soldier_row) + 2][int(soldier_col) + 2]:
        screen.draw_win_message()
        consts.FINISH = True
    else:
        soldier_moving()




soldier = pygame.Rect(0,0,consts.SOLDIER_WIDTH,consts.SOLDIER_HEIGHT)
