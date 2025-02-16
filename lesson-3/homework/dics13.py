
my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

inverted_dict = {value: key for key, value in my_dict.items()}

print(inverted_dict)
