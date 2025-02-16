my_set = {1,2,3,4,5,6,7,8,9,10}
counter_list = []
for number in my_set:
    if number % 2 != 0:
        counter_list.append(number)
setting_back = set(counter_list)
print(setting_back)
    