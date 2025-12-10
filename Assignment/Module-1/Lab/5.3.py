# Write a Python program to find a specific string in the list using a simple
# for loop and if condition.
List1 = ['apple', 'banana', 'mango']
n="mango"
for i in List1:
    if i==n:
        print(i)
        print(List1.index(n))
    