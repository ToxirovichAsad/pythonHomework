txt = "abcabcdabcdeabcdefabcdefg"
vowels = "aeiouAEIOU"
result = ""
count = 0
previous = []

for i in range(len(txt)):
    count += 1
    result += txt[i]

   
    if count >= 3 and txt[i] not  in vowels and txt[i] not in previous:
        if i < len(txt) - 1:  
            result += "_"
            count = 0  
            previous.append(txt[i])



print(result)
