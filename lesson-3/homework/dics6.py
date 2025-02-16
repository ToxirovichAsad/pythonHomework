first_dicst = {
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
second_dicst = {
    "john": 1,
    "jane": 2,
    "joe": 3,
    "jerry": 4,
}
concantenated_dicst = {**first_dicst, **second_dicst}
print(concantenated_dicst)