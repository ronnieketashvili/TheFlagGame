import random

def building_minefield():
    mine_field = []
    for i in range(25):
        row = []
        for col in range(50):
            row.append('free')
        mine_field.append(row)
    return mine_field


def lay_mines(mine_field):
    for i in range(20):
        random_row = random.randint(0, 24)
        random_col = random.randint(0, 47)
        while 21 <= random_row <= 23 and 44 <= random_col <= 49:
            random_row = random.randint(0, 24)
            random_col = random.randint(0, 47)
        while 0 <= random_row <= 4 and 0 <= random_col <= 2:
            random_row = random.randint(0, 24)
            random_col = random.randint(0, 47)
        for j in range(3):
            mine_field[random_row][random_col+j] = 'mine'
    return mine_field


def mines_location(mine_field):
    mines_location_list = []
    for row in range(len(mine_field)):
        for col in range(len(mine_field[row])):
            if mine_field[row][col] == 'mine':
                mines_location_list.append((row, col))
    return mines_location_list


def flag_position(mine_field):
    for row in range(3):
        for col in range(4):
            mine_field[21 + row][46 + col] = 'flag'
    return mine_field


def creating_minefield():
    mine_field = building_minefield()
    mine_field = lay_mines(mine_field)
    mine_field = flag_position(mine_field)
    return mine_field


# For debugging purposes
''' 
def print_mine_field(mine_filed):
    for row in range(len(mine_filed)):
        for col in range(len(mine_filed[row])):
            print(mine_filed[row][col], " ", end="")
        print()
'''
