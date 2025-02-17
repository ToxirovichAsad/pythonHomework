
my_dics = {
    'name': 'Alice',
    'details': {
        'age': 25,
        'city': 'New York'
    },
    'hobbies': ['reading', 'traveling']
}

has_nested = any(isinstance(value, dict) for value in my_dics.values())

if has_nested:
    print("The dictionary has nested dictionaries.")
else:
    print("The dictionary does not have nested dictionaries.")
