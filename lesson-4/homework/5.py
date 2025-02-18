
conditons = True
while conditons:
    password = input("Enter your password: ")

    if len(password) < 8:
        print("Password is too short.")
        continue
    elif not any(char.isupper() for char in password):
        print("Password must contain an uppercase letter.")
        continue
    else:
        print("Password is strong.")
        conditons =False

