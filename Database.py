import os
import screen
import soldier
import consts
import pandas as pd
from ast import literal_eval

DATABASE = "MemoryTheFlagGame.csv"
df = pd.DataFrame(consts.DEFAULT_DATAFRAME)

def initialize_database():
    global df
    if os.path.isfile(DATABASE):
        df = pd.read_csv(DATABASE)
    else:
        df.to_csv(DATABASE)


def given_data_for_press(pressed_number):
    df[pressed_number][0] = screen.BUSHES_LIST
    df[pressed_number][1] = consts.MINES_LIST
    df[pressed_number][2] = soldier.soldier.x, soldier.soldier.y
    df.to_csv(DATABASE)


def get_proper_coordinates(pressed_number, column):
    df = pd.read_csv(DATABASE)
    return literal_eval(df[pressed_number][column])

def check_exist_memories(pressed_number):
    if df[pressed_number][0] != "list of bushes":
        return True
    else:
        return False



