import pygame
import screen
import consts
pygame.init()

soldier_image = pygame.image.load('soldier.png.png')
soldier_image = pygame.transform.scale(soldier_image, (consts.SOLDIER_WIDTH,consts.SOLDIER_HEIGHT))

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

def soldier_in_matrix(minefield):
    soldier_col = int(soldier.x) // 20
    soldier_row = int(soldier.y) // 20
    legs_location_matrix = minefield[int(soldier_row) + 3][int(soldier_col) + 1]
    print(legs_location_matrix)
    print(soldier_row + 3, soldier_col + 3)
    return legs_location_matrix


soldier = pygame.Rect(0,0,consts.SOLDIER_WIDTH,consts.SOLDIER_HEIGHT)

def checking_minefield():
    if soldier_in_matrix(consts.MINEFIELD) == 'mine':
        count = 0
        h = 0
        for i in range(40):
            explotion_picture = pygame.image.load('explotion.png')
            explotion = pygame.transform.scale(explotion_picture, (80, 80))
            screen.SCREEN.blit(explotion, (soldier.x, soldier.y))
            pygame.display.update()
            count += 1
        for j in range(40):
            injured_soldier_picture = pygame.image.load('injury_soldier.png')
            injured_soldier = pygame.transform.scale(injured_soldier_picture, ((consts.SOLDIER_WIDTH, consts.SOLDIER_HEIGHT)))
            screen.SCREEN.blit(injured_soldier, (soldier.x, soldier.y))
            pygame.display.update()
            h += 1
        #screen.draw_lose_message()
        #consts.FINISH = True
        #return consts.FINISH
    elif soldier_in_matrix(consts.MINEFIELD) == 'flag':
        #screen.draw_win_message()
        consts.FINISH = True
        return consts.FINISH



