# Create a mini-project where students combine conditional statements, loops, and functions
# to create a basic Python application, such as a simple calculator or a grade management
# system.

def add(a,b):
    print(a+b)

def sub(a,b):
    print(a-b)

def mul(a,b):
    print(a*b)

def div(a,b):
    print(a/b)

while True:
    print("1) add")
    print("2) subtract") 
    print("3) multiply")
    print("4) divide")
    print("\nenter '0' to exit")
    n1=int(input("enter number 1  = "))
    n2=int(input("enter number 2  = "))
    choice = int(input("choose (1/2/3/4): "))

    if choice==0:
        print("yhank you")
        break
    elif choice==1:
        add(n1,n2)
    elif choice==2:
        sub(n1,n2)
    elif choice==3:
        mul(n1,n2)
    elif choice==4:
        div(n1,n2)
    else:
        print("enter valid choice...!")
