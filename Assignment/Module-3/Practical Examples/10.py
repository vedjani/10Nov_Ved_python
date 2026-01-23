# 10) Write a Python program to print custom exceptions.
age = int(input("Enter your age: "))

if age < 18:
    raise Exception("Age must be 18 or above")

