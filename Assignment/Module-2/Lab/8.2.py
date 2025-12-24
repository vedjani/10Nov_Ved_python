# Write a Python program to create a calculator using functions.
def add(a,b):
    print("your ans is:-",a+b)

def sub(a,b):
    print("your ans is:-",a-b)

def mul(a,b):
    print("your ans is:-",a*b)

def div(a,b):
    print("your ans is:-",a/b)




while True:
    print("1) add")
    print("2) subtract") 
    print("3) multiply")
    print("4) divide")
    print("\nenter '0' to exit")
    choice = int(input("choose (1/2/3/4): "))
    
    
    if choice==0:
        print("Thank you")
        break       
    elif choice==1:
        n1=int(input("enter number 1  = "))
        n2=int(input("enter number 2  = "))
        add(n1,n2)
    elif choice==2:
        n1=int(input("enter number 1  = "))
        n2=int(input("enter number 2  = "))
        sub(n1,n2)
    elif choice==3:
        n1=int(input("enter number 1  = "))
        n2=int(input("enter number 2  = "))
        mul(n1,n2)
    elif choice==4:
        n1=int(input("enter number 1  = "))
        n2=int(input("enter number 2  = "))
        div(n1,n2)
    else:
        print("enter valid choice...!")
        
   