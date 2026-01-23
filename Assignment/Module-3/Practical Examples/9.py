# 9) Write a Python program to handle file exceptions and use the finally block for closing the file.
try:
    num1=int(input("enter one number:-"))
    num2=int(input("enter second number:-"))
    print(float(num1/num2))
except ZeroDivisionError as e:
    print(e)
finally:
    try:
        num3=int(input("enter new number tow bigger than zero:-"))
        print(float(num1/num3))
    except ZeroDivisionError:
        print("please learn math🙏🏻🔫")