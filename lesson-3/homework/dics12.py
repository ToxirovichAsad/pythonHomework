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
count = sum(1 for value in my_dics.values() if value == target_is )
print(count)