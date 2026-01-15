# Write a Python program to create a class and access its properties using an object.
class MyClass:
    def info(self, name, age):
        self.name = name
        self.age = age      
MyClass.info("ved", 22)
print("Name = ", MyClass.name)
print("Age = ", MyClass.age)