# 8)Write a Python program to handle multiple exceptions (e.g., file not found, division by zero).
try:
    file=open("try",'r')
    fl_data=file.read()
    print(f"file data:-{fl_data}")

    num1=int(input("enter one number:-"))
    num2=int(input("enter second number:-"))
    print(float(num1/num2))
except FileExistsError as z:
    print(z)
except ZeroDivisionError as e:
    print(e)
