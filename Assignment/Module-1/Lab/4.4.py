#  Write a Python program to check if a person is eligible to donate blood
# using a nested if.

age=int(input("Enter your age:-"))
bldpr=int(input("Enter your blood pr :-"))
if age>=18:
    if bldpr>=50:
        print("you are eligible to donate blood")
    else:
        print("you are NOT eligible to donate blood")
else:
    print("you are NOT eligible to donate blood")
