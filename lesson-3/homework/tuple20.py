my_tuple = (1, 2, 3, 4, 5, 4, 3, 3, 3, 4, 4, 4)
number__of_elements = 2

nested_tuple = tuple(my_tuple[i:i+number__of_elements] for i in range(0, len(my_tuple), number__of_elements))
print(nested_tuple)