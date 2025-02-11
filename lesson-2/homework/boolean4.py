first_number = float(input("Enter a number: "))
second_number = float(input("Enter another number: "))
thir_number = float(input("Enter another number: "))
if first_number == second_number == thir_number:
    print("The numbers are the same")
elif first_number == second_number or first_number == thir_number or second_number == thir_number:
    print("Two of the numbers are the same")
else:
    print("Numbers are different")
    