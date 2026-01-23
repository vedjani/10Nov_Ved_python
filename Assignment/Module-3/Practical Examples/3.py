# 3) Write a Python program to create a file and write a string into it.
str = input("Enter the string to write into the file = ")

file = open("v1.txt", 'w')
file.write(str)

file.close()