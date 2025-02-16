my_dics = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 4,
    "g": 3,
    "h": 3,
    "i": 3,
    "j": 4,
    "k": 4,
    "l": 4
}

target_is = 3
my_list=[key for key, value in my_dics.items() if value == target_is]
print(my_list)
