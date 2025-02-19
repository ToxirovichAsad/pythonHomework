def invest(amount, rate, years):
    
    for counter in range(1, years + 1):  
        amount += amount * rate  
        print(f"Year {counter}: $ {amount:.2f}")  


try:
    user_input_amount = float(input("Enter initial amount: "))
    user_input_rate = float(input("Enter annual percentage rate (e.g., 5 for 5%): ")) / 100 
    user_input_years = int(input("Enter how many years: "))


    invest(user_input_amount, user_input_rate, user_input_years)

except ValueError:
    print("Invalid input! Please enter numbers only.")
