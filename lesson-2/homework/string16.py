user_txt = input("Enter a string: ")
user_char = input("Enter a character: ")
changing_char = ""
for char in user_txt:
    if char == user_char:
        changing_char +=""
    else:
        changing_char += char
print("String with character removed:", changing_char)