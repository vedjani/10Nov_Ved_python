# 24) Write a Python program to match a word in a string using re.match().
import re


s = "Hello, World!"
match = re.match("Hello", s)

if match:
    print("found!")
else:
    print("not found.")