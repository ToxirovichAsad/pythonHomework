#1
def convert_cel_to_far(C):
    return round((C * 9/5 + 32),2)

#2
def convert_far_to_cel(F) :
    return round(((F - 32) * 5/9),2)
try:
    user_input_far = float(input("Enter a temperature in degrees F: "))
    print(user_input_far," degrees F = ", convert_far_to_cel(user_input_far)," degrees C")

    user_input_cel = float(input("Enter a temperature in degrees C: "))
    print(user_input_cel," degrees C = ", convert_cel_to_far(user_input_cel)," degrees F")
except ValueError:
    print("Invalid input! Please enter numbers only.")
