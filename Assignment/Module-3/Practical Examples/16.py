# 16) Write a Python program to show hierarchical inheritance.
class Employee:
    def company(self):
        return"TCS"
        
class Manager(Employee):
    def post(self):
        return "Manager"
        
class Clerk(Employee):
    def post(self):
        return "Clerk"
        
m=Manager()
c=Clerk()

print(f"Manager works at {m.company()} as {m.post()}")
print(f"Clerk works at {c.company()} as {c.post()}")
