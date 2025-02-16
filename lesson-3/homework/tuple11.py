my_tuple  = (1, 2, 3, 4, 5,4,3,3,3,4,4,4)
element = 4
counter_list = []
for i in range(len(my_tuple)):
    if my_tuple[i] == element:
        counter_list.append(i)
        

print(counter_list)