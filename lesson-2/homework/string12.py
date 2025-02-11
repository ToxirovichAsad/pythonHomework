changer = True
list_of_words = []
print("Enter a word, when do you want to stop enter 'stop': ")
while changer:
    user_txt = input("Enter a word: ")
    if user_txt == "stop":
        changer = False
    else:
        list_of_words.append(user_txt)
text_without_list = "-".join(list_of_words)    
print(text_without_list)            
    