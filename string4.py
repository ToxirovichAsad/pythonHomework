user_inpt = input("Enter a word ")
pallindroming = user_inpt.strip()
checker=bool(pallindroming==pallindroming[::-1])
print(checker)
if(checker):
    print("It is a pallindrome")
else:
    print("It is not a pallindrome")
