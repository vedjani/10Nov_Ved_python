# 18) Write a Python program to demonstrate the use of super() in inheritance.
class Parent:
    def show(self):
        print("Parent function")

class Child(Parent):
    def show(self):
        super().show()
        print("Child function")

obj = Child()
obj.show()
