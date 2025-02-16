my_dicst = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
key1 = "name"
if key1 in my_dicst:
    my_dicst.pop(key1)
else:
    print("Key not found")
print(my_dicst)