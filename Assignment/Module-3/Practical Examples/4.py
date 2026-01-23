# 4) Write a Python program to create a file and print the string into the file.
str = input("Enter the string to write into the file = ")

file = open("4py.txt", 'w')
file.write(str)

file.close()