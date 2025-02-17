
my_dict = {
    "b": 2,
    "d": 4,
    "e": 5,
    "f": 4,
    "c": 3,
    "g": 3,
    "h": 3,
    "a": 1,
    "i": 3,
    "j": 4,
    "k": 4,
    "l": 4
}

inverted_dict = {value: key for key, value in my_dict.items()}
print(inverted_dict)

sordet_by_keys = dict(sorted(inverted_dict.items()))
inverted_dict_back = {value: key for key, value in sordet_by_keys.items()}

print(inverted_dict_back)
