import csv
import pandas as pd

df = {
    1: ["Memory number", "list of bushes", "list of mines", "X rate of soldier", "Y rate of soldier"],
    2: ["Memory number", "list of bushes", "list of mines", "X rate of soldier", "Y rate of soldier"],
    3: ["Memory number", "list of bushes", "list of mines", "X rate of soldier", "Y rate of soldier"],
    4: ["Memory number", "list of bushes", "list of mines", "X rate of soldier", "Y rate of soldier"],
    5: ["Memory number", "list of bushes", "list of mines", "X rate of soldier", "Y rate of soldier"],
    6: ["Memory number", "list of bushes", "list of mines", "X rate of soldier", "Y rate of soldier"],
    7: ["Memory number", "list of bushes", "list of mines", "X rate of soldier", "Y rate of soldier"],
    8: ["Memory number", "list of bushes", "list of mines", "X rate of soldier", "Y rate of soldier"],
    9: ["Memory number", "list of bushes", "list of mines", "X rate of soldier", "Y rate of soldier"]
}

df = pd.DataFrame(df)

df.to_csv("Memory TheFlagGame.csv")

print(df)
#with open('The Flag Game memory', 'w', newline='') as file:
#    writer = csv.writer(file)
#    writer.writerows(memory_list)