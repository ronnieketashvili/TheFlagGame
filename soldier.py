import pygame
import screen
import consts
pygame.init()

soldier_image = pygame.image.load('soldier.png.png')
soldier_image = pygame.transform.scale(soldier_image, (consts.SOLDIER_WIDTH, consts.SOLDIER_HEIGHT))

keys_pressed = pygame.key.get_pressed()
def right_key():
   if soldier.x + consts.VEL + consts.SOLDIER_WIDTH < consts.WINDOW_WIDTH:
        soldier.x += consts.VEL
def left_key():
    if soldier.x - consts.VEL > 0:
        soldier.x -= consts.VEL

def up_key():
    if soldier.y - consts.VEL > 0:
        soldier.y -= consts.VEL

def down_key():
    if soldier.y + consts.VEL +consts.SOLDIER_HEIGHT < BORDER.y:
        soldier.y += consts.VEL


def soldier_moving():
    global keys_pressed
    right_key(keys_pressed)
    left_key(keys_pressed)
    down_key(keys_pressed)
    up_key(keys_pressed)


BORDER = pygame.Rect(1000, 500, consts.WINDOW_WIDTH,consts.WINDOW_HEIGHT)

def soldierlegs_in_matrix(minefield):
    soldier_col = int(soldier.x) // 20
    soldier_row = int(soldier.y) // 20
    legs_location_matrix = minefield[int(soldier_row) + 3][int(soldier_col) + 1]
    return legs_location_matrix

def soldierbody_in_matrix(minefield):
    body_locations = []
    soldier_col = int(soldier.x) // 20
    soldier_row = int(soldier.y) // 20
    for i in range(3):
        body_part1_location = minefield[int(soldier_row) + i][int(soldier_col)]
        body_locations.append(body_part1_location)
        body_part2_location = minefield[int(soldier_row) + i][int(soldier_col) + 1]
        body_locations.append(body_part2_location)
    return body_locations



soldier = pygame.Rect(0,0,consts.SOLDIER_WIDTH,consts.SOLDIER_HEIGHT)

def checking_minefield():
    if soldierlegs_in_matrix(consts.MINEFIELD) == 'mine':
        for i in range(20):
            screen.add_explosion()
        for j in range(20):
            screen.add_injured_soldier()
            screen.draw_lose_message()
        consts.FINISH = True
        return consts.FINISH
    elif 'flag' in soldierbody_in_matrix(consts.MINEFIELD):
        counter = 0
        while counter <= 35:
            screen.player_screen()
            screen.draw_win_message()
            counter += 1
            pygame.display.update()
        consts.FINISH = True
        return consts.FINISH



