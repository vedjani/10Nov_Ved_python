# Write Python programs to demonstrate method overloading and method overriding

print("")
#Method overloading----------------------------------------------------------------
print("***** Method overloading *****")
print("")
class emp:
    def emp_info(self,id):
        print("ID=",id)
    def emp_info(self,name):
        print("NAME=",name)
    def emp_info(self,dept):
        print("DEPT=",dept)
em=emp()
em.emp_info(101)
em.emp_info("ved")
em.emp_info("tech")

print("")
#Method overriding-----------------------------------------------------------------
print("***** Method overriding *****")
print("")

class parent:
    def show(self,name):
        print("Parent Class Name=",name)
        
class child(parent):
    def show(self,name):
        print("Child Class Name=",name)
        
ch=child()
ch.show("ved2")
pa=parent()
pa.show("ved1")