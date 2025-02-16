my_tuple = (1,2,34,55,55,22,3,11)
second_largest = sorted(tuple(set(my_tuple)))[1]
print(second_largest)
