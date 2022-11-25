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


def get_all_alphabet_combinations_list(length):
    print(f"making list of length {length}")
    result = []
    while length > 0:
        if len(result) == 0:
            result = possible_combinations
        else:
            new_result = []
            for i, v in enumerate(result):
                for i2, v2 in enumerate(possible_combinations):
                    new_result.append(v + v2)
            result = new_result
        length -= 1
    return result


def has_all_alphabet_combinations(string):
    for _, v1 in enumerate(possible_combinations):
        for _, v2 in enumerate(possible_combinations):
            if v1 + v2 not in string:
                return False
    return True


search_string_lower_bound = 2 * 26  # 26 letters, 2 times each
search_string_upper_bound = 2 * 26 * 26  # 26 letters, 2 times each, 26 combinations

for i in range(search_string_lower_bound, search_string_upper_bound):
    candidates = get_all_alphabet_combinations_list(i)
    for _, v in enumerate(candidates):
        print(v)
        if has_all_alphabet_combinations(v):
            print("Found it: ", v)
            exit(0)
