import pygame
import screen
import consts
pygame.init()

def soldier_image():
    # Editing the image of the soldier to the fitting size
    soldier_image = pygame.image.load('soldier.png.png')
    soldier_image = pygame.transform.scale(soldier_image,
                                           (consts.SOLDIER_WIDTH, consts.SOLDIER_HEIGHT))
    return soldier_image

soldier_image = soldier_image()
soldier = pygame.Rect(0, 0, consts.SOLDIER_WIDTH, consts.SOLDIER_HEIGHT)

keys_pressed = pygame.key.get_pressed()
def right_key():
    # Checking that the step will not lead to the soldier leaving the screen
   if soldier.x + consts.VEL + consts.SOLDIER_WIDTH < consts.WINDOW_WIDTH:
        soldier.x += consts.VEL
def left_key():
    if soldier.x - consts.VEL > 0:
        soldier.x -= consts.VEL

def up_key():
    if soldier.y - consts.VEL > 0:
        soldier.y -= consts.VEL

BORDER = pygame.Rect(1000, 500, consts.WINDOW_WIDTH,consts.WINDOW_HEIGHT)

def down_key():
    if soldier.y + consts.VEL +consts.SOLDIER_HEIGHT < BORDER.y:
        soldier.y += consts.VEL

def soldier_moving():
    global keys_pressed
    right_key()
    left_key()
    down_key()
    up_key()


def soldier_matrix():
    # checking soldier coordinates in the matrix
    soldier_col = int(soldier.x) // consts.VEL
    soldier_row = int(soldier.y) // consts.VEL
    return (soldier_row, soldier_col)

def soldier_legs_in_matrix(minefield):
    # Checking the position of the soldier's feet in the matrix
    soldier_row, soldier_col = soldier_matrix()
    legs_location_matrix = minefield[int(soldier_row) + 3][int(soldier_col) + 1]
    return legs_location_matrix


def soldier_body_in_matrix(minefield):
    # Checking the location of the soldier's body in the matrix, and returning it as a list
    body_locations = []
    soldier_row, soldier_col = soldier_matrix()
    for j in range(3):
        body_part1_location = minefield[int(soldier_row) + j][int(soldier_col)]
        body_locations.append(body_part1_location)
        body_part2_location = minefield[int(soldier_row) + j][int(soldier_col) + 1]
        body_locations.append(body_part2_location)
    return body_locations

def player_lose():
    # Changing of the screen in case of losing the game
    for i in range(20):
        screen.add_explosion()
    for j in range(20):
        screen.add_injured_soldier()
        screen.draw_lose_message()
    consts.FINISH = True

def player_win():
    # Changing of the screen in case of winning the game
    counter = 0
    while counter <= 35:
        screen.player_screen()
        screen.draw_win_message()
        counter += 1
        pygame.display.update()
    consts.FINISH = True


def checking_minefield():
    # Checking whether the soldier's feet touch the mine, or his body touches the flag
    if soldier_legs_in_matrix(consts.MINEFIELD) == 'mine':
        player_lose()
        return consts.FINISH
    elif 'flag' in soldier_body_in_matrix(consts.MINEFIELD):
        player_win()
        return consts.FINISH



