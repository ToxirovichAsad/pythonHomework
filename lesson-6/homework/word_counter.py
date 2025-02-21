
import string

file_name = "sample.txt"
try:
    with open(file_name, "r") as file:
        text = file.read()
except FileNotFoundError:
    print(f"'{file_name}' not found. Please enter text to create the file.")
    text = input("Enter a paragraph: ")
    with open(file_name, "w") as file:
        file.write(text)


text = text.lower()
text = text.translate(str.maketrans("", "", string.punctuation))  # Remove punctuation found in internet 
words = text.split()

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

total_words = sum(word_count.values())
print(f"\nTotal words: {total_words}")
print("Top 5 most common words:")
for word, count in sorted_words[:5]:  
    print(f"{word} - {count} times")

with open("word_count_report.txt", "w") as report:
    report.write("Word Count Report\n")
    report.write(f"Total Words: {total_words}\n")
    report.write("Top 5 Words:\n")
    for word, count in sorted_words[:5]:
        report.write(f"{word} - {count}\n")

print("\nReport saved as 'word_count_report.txt'.")
