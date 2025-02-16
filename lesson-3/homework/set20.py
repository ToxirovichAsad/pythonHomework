first_set = {1, 2, 3, 4, 5,4,3,3,3,4,4,4}
second_set = {6, 7, 8, 91,1, 10}
if first_set.isdisjoint(second_set):
    print('Sets have no common elements')
else:
    print('Sets have common elements')