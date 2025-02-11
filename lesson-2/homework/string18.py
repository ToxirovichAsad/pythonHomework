user_input = input("Enter a string: ")
first_word = user_input.split()[0]
last_word = user_input.split()[-1]
if first_word == last_word:
    print("The first and last words are the same")
print("The first word is:", first_word)
print("The last word is:", last_word)