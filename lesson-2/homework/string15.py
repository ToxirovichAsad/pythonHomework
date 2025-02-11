user_input = input("Enter a string: ")
acronym = ""
for word in user_input.split():
    acronym += word[0].upper()
print("Acronym:", acronym)