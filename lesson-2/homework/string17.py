user_input = input("Enter a string: ")
changing_vowels = ""
for char in user_input:
    if char in "aeiou":
        changing_vowels += "*"
    else:
        changing_vowels += char
print("String with vowels replaced by *:", changing_vowels)