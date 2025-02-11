user_txt = input("Enter a string: ")
checker = False
for char in user_txt:
    if char.isnumeric():
        print("The string contains a number")
        checker = True
        break
    

if checker==False:
    print("The string does not contain a number")