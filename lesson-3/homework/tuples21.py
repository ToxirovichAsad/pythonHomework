my_tuple = (1,2,3,4,5)
repeater = 2
creating_tuple = tuple(my_tuple[i] for i in range(len(my_tuple)) for j in range(repeater))
print(creating_tuple)