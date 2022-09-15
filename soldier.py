import pygame
import screen
import consts


soldier_image = pygame.image.load('soldier.png.png')
soldier_image = pygame.transform.scale(soldier_image, (consts.SOLDIER_WIDTH,consts.SOLDIER_HEIGHT))

def soldier_moving():
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_RIGHT] and soldier.x + consts.VEL + consts.SOLDIER_WIDTH < consts.WINDOW_WIDTH:
        soldier.x += consts.VEL
    if keys_pressed[pygame.K_UP] and soldier.y - consts.VEL > 0:
        soldier.y -= consts.VEL
    if keys_pressed[pygame.K_LEFT] and soldier.x - consts.VEL > 0:
        soldier.x -= consts.VEL
    if keys_pressed[pygame.K_DOWN] and soldier.y + consts.VEL + consts.SOLDIER_HEIGHT < BORDER.y:
        soldier.y += consts.VEL

BORDER = pygame.Rect(1000,500,consts.WINDOW_WIDTH,consts.WINDOW_HEIGHT)

def soldier_in_matrix(minefield):
    soldier_col = int(soldier.x) / 20
    soldier_row = int(soldier.y) / 20
    soldier_location_matrix = minefield[int(soldier_row) - 3][int(soldier_col) + 1]
    return soldier_location_matrix


soldier = pygame.Rect(0,0,consts.SOLDIER_WIDTH,consts.SOLDIER_HEIGHT)

def checking_minefield():
    soldier_moving()
    if soldier_in_matrix(consts.MINEFIELD) == 'mine':
        #soldier_image = pygame.image.load('injury_soldier.png')
        #soldier_image = pygame.transform.scale(soldier_image, (consts.SOLDIER_WIDTH,consts.SOLDIER_HEIGHT))
        #screen.draw_lose_message()
        consts.FINISH = True
        return consts.FINISH
    if soldier_in_matrix(consts.MINEFIELD) == 'flag':
        #screen.draw_win_message()
        consts.FINISH = True
        return consts.FINISH
    else:
        soldier_moving()


