# 23) Write a Python program to search for a word in a string using re.search().
import re


s = "Hello ved bhai kem chhe."
pat = "."

res = re.search(pat, s)

if res:
    print("Yes")
else:
    print("No")
