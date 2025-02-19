def postive_factor(number1):
    for i in range(1, number1+1) :
        if number1%i == 0:
            print(i, "is a factor of ", number1)
while True:
    try:
        user_input = int(input("Enter a positive integer: "))
        if user_input > 0:
            break
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
postive_factor(user_input)

        
    