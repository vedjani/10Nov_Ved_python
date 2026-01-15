import re

text = "hello maru name ved chhe "
word = input("Enter word to search: ")

match = re.search(word, text)

if match:
    print("Word found!")
else:
    print("Word not found.")
