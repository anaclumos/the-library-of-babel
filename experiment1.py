possible_combinations = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

length = 2

all = ""

for i in range(0, len(possible_combinations)):
    for j in range(0, len(possible_combinations)):
        all = all + possible_combinations[i] + possible_combinations[j]

print(all)
print(len(all))
