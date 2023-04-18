with open("books/frankenstein.txt") as f:
    file_contents = f.read()
#words = file_contents.split()
dict = {}
for letter in file_contents.lower():
    if letter in dict:
        dict[letter] = dict[letter] + 1
    else:
        dict[letter] = 1
print(dict)
