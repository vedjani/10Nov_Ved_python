# 7) Write a Python program to handle exceptions in a calculator.
try:
    num1=int(input("enter num1 :- "))
    num2=int(input("enter num2 :- "))
    cal_inp=input("Please operation (+, -, *, /): ")
    if cal_inp == '+':
        print(num1+num2)
    elif cal_inp == '-':
        print(num1-num2)
    elif cal_inp == '*':
        print(num1*num2)
    elif cal_inp == '/':
        print(num1/num2)
    else:
        print("please enter valid symbol")
except ValueError:
    print("Invalid input! Please enter numbers only.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")