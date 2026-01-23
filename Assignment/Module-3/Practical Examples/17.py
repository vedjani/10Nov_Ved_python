# 17) Write a Python program to show hybrid inheritance.
class surname:
    def last_name(self):
        return "jani"
    
class boy(surname):
    def fname_b(self):
        return "ved"
    
class girl(surname):
    def fname_g(self):
        return "vedika"
    
class child(boy, girl):
    def child_name(self):
        return "there are two kids"
    
c = child()
print(f"{c.child_name()}: \n1) {c.fname_b()} {c.last_name()} \n2) {c.fname_g()} {c.last_name()}")