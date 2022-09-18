import csv
import pandas as pd

import screen
import soldier

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
def getting_data_for_press(press_number):
    df[press_number][0] = screen.locations
    df[press_number][1] = screen.LIST
    df[press_number][2] = soldier.soldier.x
    df[press_number][3] = soldier.soldier.y
    df.to_csv("MemoryTheFlagGame.csv")


df = pd.DataFrame(df)
print(df)

