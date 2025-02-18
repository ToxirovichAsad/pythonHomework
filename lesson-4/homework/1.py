list1 = []
list2 = []

while True:
    user_input = input("Enter number for list1  (type 'q', 'quit', or 'exit' to stop): ").strip().lower()
    
    if user_input in ['q', 'quit', 'exit']:
        break
    else:
        list1.append(int(user_input))
while True:
    user_input = input("Enter number for list2  (type 'q', 'quit', or 'exit' to stop): ").strip().lower()
    
    if user_input in ['q', 'quit', 'exit']:
        break
    else:
        list2.append(int(user_input))
common_list = set(list1).intersection(set(list2))
result = [x for x in list1 + list2 if x not in common_list]
print(result)

