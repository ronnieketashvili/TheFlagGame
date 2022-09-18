import csv
import pandas as pd

import screen
import soldier

csv_file = "MemoryTheFlagGame.csv"

df = {
    1: ["list of bushes", "list of mines", "X rate of soldier", "Y rate of soldier"],
    2: ["list of bushes", "list of mines", "X rate of soldier", "Y rate of soldier"],
    3: ["list of bushes", "list of mines", "X rate of soldier", "Y rate of soldier"],
    4: ["list of bushes", "list of mines", "X rate of soldier", "Y rate of soldier"],
    5: ["list of bushes", "list of mines", "X rate of soldier", "Y rate of soldier"],
    6: ["list of bushes", "list of mines", "X rate of soldier", "Y rate of soldier"],
    7: ["list of bushes", "list of mines", "X rate of soldier", "Y rate of soldier"],
    8: ["list of bushes", "list of mines", "X rate of soldier", "Y rate of soldier"],
    9: ["list of bushes", "list of mines", "X rate of soldier", "Y rate of soldier"]
}

df = pd.DataFrame(df)
# here supposed to be the change
df.to_csv(csv_file)
def getting_data_for_press(pressed_number):
    df[pressed_number][0] = screen.locations
    df[pressed_number][1] = screen.LIST
    df[pressed_number][2] = soldier.soldier.x
    df[pressed_number][3] = soldier.soldier.y
    df.to_csv(csv_file)



