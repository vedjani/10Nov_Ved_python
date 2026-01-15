import re

text = input("Enter a string: ")
word = input("Enter word to match: ")

match = re.match(word, text)

if match:
    print("Word matched!")
else:
    print("Word not matched.")
