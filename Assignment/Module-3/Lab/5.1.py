# Write a Python program to handle exceptions in a simple calculator (division by zero, invalid input).

try:
    num1=int(input("enter 1 number:- "))
    num2=int(input("enter 2 number:- "))

    
    print(f"output is = {num1/num2}")
   

except ZeroDivisionError:
    print("Cannot divide by zero")