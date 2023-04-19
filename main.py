with open("books/frankenstein.txt") as f:
    file_contents = f.read()
words = file_contents.split()
dict = {}
for letter in file_contents.lower():
    if letter in dict:
        dict[letter] = dict[letter] + 1
    else:
        dict[letter] = 1
letters_list = []
for key in dict:
    if key.isalpha():
        letters_list.append(key)
letters_list.sort()
print("--- Begin report of books/frankenstein.txt ---")
print(f"{len(words)} words found in the document")
for letter in letters_list:
    print(f"The '{letter}' character was found {dict[letter]} times")
print("--- End report ---")

