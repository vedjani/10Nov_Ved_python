# Write a Python program to sort a list using both sort() and sorted().
lis=[2,5,6,4,7,9,8,3,1]
print(type(lis))

print("before sort()",lis)
lis.sort()
print("after sort()",lis)
#only work in list and change og list
print("*************sorted************")
lis1=[2,5,6,4,7,9,8,3,1]
new_lis=sorted(lis1)
print(lis1)
print(new_lis)
#work in all & can't change og list , make new list

