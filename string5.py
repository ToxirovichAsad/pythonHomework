user_int= input("Enter  somthing ")
striping= user_int.strip()
lengthe = len(striping)
vowels= "aeiouAEIOU"
vowel_counter=0
consonants_counter=0
while(lengthe!=0):
    if(striping[lengthe-1] in vowels):
        vowel_counter+=1
    else:
        consonants_counter+=1
    lengthe-=1
print("There is ",vowel_counter," vowels in the text")
print("There is ",consonants_counter," consonants in the text")