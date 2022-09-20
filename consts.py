import MineField
import soldier

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 500
SCREEN_COLOR = (61, 145, 64)
SCREEN_ENTER_COLOR = (0, 0, 0)
ROWS = 25
COLUMN = 50
DISTANCE_BTW_ROWS = WINDOW_HEIGHT // ROWS
FLAG_SIZE = (80, 80)
FONT_NAME = "Calibri"
FPS = 60

SOLDIER_HEIGHT = 80
SOLDIER_WIDTH = 70
VEL = 20
COUNTER = 60
PREESED_NUMBER = 0
count = 0

BUSHES_SIZE = (220, 60)
BUSHES_NUMBER = 20

MINE_SIZE = (60, 20)

FINISH = False
MINEFIELD = MineField.creating_minefield()
MINES_LIST = MineField.mines_location(MINEFIELD)
soldier_full_location = soldier.solder_full_body_matrix()

# Database constants
BUSH_COORD = 0
MINES_COORD = 1
SOLDIER_COORD = 2
MATRIX_COORD = 3
DEFAULT_DATAFRAME = {
    "1": ["list of bushes", "list of mines", "soldier coordinates", "matrix"],
    "2": ["list of bushes", "list of mines", "soldier coordinates", "matrix"],
    "3": ["list of bushes", "list of mines", "soldier coordinates", "matrix"],
    "4": ["list of bushes", "list of mines", "soldier coordinates", "matrix"],
    "5": ["list of bushes", "list of mines", "soldier coordinates", "matrix"],
    "6": ["list of bushes", "list of mines", "soldier coordinates", "matrix"],
    "7": ["list of bushes", "list of mines", "soldier coordinates", "matrix"],
    "8": ["list of bushes", "list of mines", "soldier coordinates", "matrix"],
    "9": ["list of bushes", "list of mines", "soldier coordinates", "matrix"]
}

# Messages constants
LOSE_MESSAGE = "You Lost!"
LOSE_FONT_SIZE = int(0.15 * WINDOW_WIDTH)
LOSE_COLOR = (0, 0, 0)
LOSE_LOCATION = (200, 175)

WIN_MESSAGE = "You Won!"
WIN_FONT_SIZE = LOSE_FONT_SIZE
WIN_COLOR = (252, 5, 190)
WIN_LOCATION = (200, 175)

START_MESSAGE = "Welcome to the Flag Game!"
START_FONT_SIZE = int(0.05 * WINDOW_WIDTH)
START_COLOR = (245, 69, 73)
START_LOCATION = (80, 5)
