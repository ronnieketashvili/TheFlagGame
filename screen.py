import pygame
import random
import soldier
import consts


SCREEN = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
pygame.display.set_caption("FLAG GAME!")


def bushes_locations():
    # Adds each bush location, x & y coordinates, as a tuple to a list of bushes' locations.
    locations_list = []
    for i in range(consts.BUSHES_NUMBER):
        x_rate = random.randint(0, 780)
        y_rate = random.randint(consts.SOLDIER_HEIGHT, 440)
        locations_list.append((x_rate, y_rate))
    return locations_list


BUSHES_LIST = bushes_locations()


def create_bushes():
    # According to the list we received, add the bushes to the screen by their coordinates
    for i in range(len(BUSHES_LIST)):
        bush_picture = pygame.image.load('bush.png')
        bush = pygame.transform.scale(bush_picture, consts.BUSHES_SIZE)
        SCREEN.blit(bush, (BUSHES_LIST[i][0], BUSHES_LIST[i][1]))


def add_flag():
    # Adds the flag to the screen by its coordinates
    flag_picture = pygame.image.load('flag.png')
    flag = pygame.transform.scale(flag_picture, consts.FLAG_SIZE)
    SCREEN.blit(flag, (920, 420))


def restart_screen():
    # Restarting screen display
    SCREEN.fill(consts.SCREEN_COLOR)
    create_bushes()
    add_flag()


def start_message():
    # Printing the "Welcome to The Flag game" message
    if soldier.soldier.x == 0 and soldier.soldier.y == 0 and consts.count <= 35:
        draw_start_message()
        consts.count += 1


def player_screen():
    # Adds the soldier to the screen display
    restart_screen()
    SCREEN.blit(soldier.soldier_image, (soldier.soldier.x, soldier.soldier.y))
    start_message()
    pygame.display.update()


def when_enter_pressed():
    # Changing the screen and images when enter is pressed
    SCREEN. fill(consts.SCREEN_ENTER_COLOR)
    grid_create()
    add_mine_grid()
    add_night_soldier()
    pygame.display.update()


def grid_create():
    # Creating a grid to the screen that is displayed when enter is pressed
    x_rate = 0
    y_rate = 0
    for i in range(consts. COLUMN):
        x_rate += consts.DISTANCE_BTW_ROWS
        y_rate += consts.DISTANCE_BTW_ROWS
        pygame.draw.line(SCREEN, (0, 139, 0), (x_rate, 0), (x_rate, consts.WINDOW_HEIGHT))
        pygame.draw.line(SCREEN, (0, 139, 0), (0, y_rate), (consts.WINDOW_WIDTH, y_rate))


def add_mine_grid():
    # Adding mines picture according to their coordinates to the screen that is displayed when enter is pressed
    for i in range(0, len(consts.MINES_LIST), 3):
        mine_picture = pygame.image.load('mine.png')
        mine = pygame.transform.scale(mine_picture, consts.MINE_SIZE)
        SCREEN.blit(mine, (consts.MINES_LIST[i][1] * 20, consts.MINES_LIST[i][0] * 20))  # y = row, col = x


def add_night_soldier():
    # Adding night soldier picture to the screen that is displayed when enter is pressed
    soldier_night_picture = pygame.image.load('soldier_nigth.png')
    soldier_night = pygame.transform.scale(soldier_night_picture, (consts.SOLDIER_WIDTH, consts.SOLDIER_HEIGHT))
    SCREEN.blit(soldier_night, (soldier.soldier.x, soldier.soldier.y))  # y = row, col = x


def add_explosion():
    # Restarting the screen and adding explosion once the soldier stepped on a mine
    restart_screen()
    explosion_picture = pygame.image.load('explotion.png')
    explosion = pygame.transform.scale(explosion_picture, (180, 180))
    SCREEN.blit(explosion, (soldier.soldier.x - 70, soldier.soldier.y - 70))
    pygame.display.update()


def add_injured_soldier():
    # Restarting the screen and adding injured soldier once the soldier stepped on a mine
    restart_screen()
    injured_soldier_picture = pygame.image.load('injury_soldier.png')
    injured_soldier = pygame.transform.scale(injured_soldier_picture, (70, 100))
    SCREEN.blit(injured_soldier, (soldier.soldier.x, soldier.soldier.y))
    pygame.display.update()


def draw_lose_message():
    draw_message(consts.LOSE_MESSAGE, consts.LOSE_FONT_SIZE,
                 consts.LOSE_COLOR, consts.LOSE_LOCATION)
    pygame.display.update()


def draw_win_message():
    draw_message(consts.WIN_MESSAGE, consts.WIN_FONT_SIZE,
                 consts.WIN_COLOR, consts.WIN_LOCATION)


def draw_start_message():
    draw_message(consts.START_MESSAGE, consts.START_FONT_SIZE,
                 consts.START_COLOR, consts.START_LOCATION)


def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    SCREEN.blit(text_img, location)
