user_inp1=(input("Enter first text "))
user_inp12=(input("Enter second text "))
if(user_inp1 in user_inp12):
    print("Second word contains first word")
elif(user_inp12 in user_inp1):
    print("First word contains second word")
else:
    print("No match")