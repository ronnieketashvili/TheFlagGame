import os
import screen
import soldier
import consts
import pandas as pd
from ast import literal_eval
import pygame

DATABASE = "MemoryTheFlagGame.csv"
df = pd.DataFrame(consts.DEFAULT_DATAFRAME)

def initialize_database():
    # Checks if the csv file even exists
    global df
    if os.path.isfile(DATABASE):
        df = pd.read_csv(DATABASE)
    else:
        df.to_csv(DATABASE)


def given_data_for_press(pressed_number):
    # Insert data game to the csv file
    df[pressed_number][0] = screen.BUSHES_LIST
    df[pressed_number][1] = consts.MINES_LIST
    df[pressed_number][2] = soldier.soldier.x, soldier.soldier.y
    df[pressed_number][3] = consts.MINEFIELD
    df.to_csv(DATABASE)


def get_proper_coordinates(pressed_number, column):
    # Access the stored information we request by locations
    df = pd.read_csv(DATABASE)
    return literal_eval(df[pressed_number][column])

def check_exist_memories(pressed_number):
    # Checks if information is saved in the same key value, if not, returns False and does not restart game
    if df[pressed_number][0] != "list of bushes":
        return True
    else:
        return False

def insert_info(key_number):
    # Restart the desired game by accessing the saved data, get it and putting it, in the required variables
    screen.BUSHES_LIST = get_proper_coordinates(key_number, consts.BUSH_COORD)
    consts.MINES_LIST = get_proper_coordinates(key_number, consts.MINES_COORD)
    soldier.soldier.x, soldier.soldier.y = get_proper_coordinates(key_number, consts.SOLDIER_COORD)
    consts.MINEFIELD = get_proper_coordinates(key_number, consts.MATRIX_COORD)
    pygame.display.update()

