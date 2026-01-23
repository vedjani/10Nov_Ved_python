# 13) Write a Python program to show single inheritance.

class parent:
    def parent(self):
        print("i am parent")
class child(parent):
    def child(self):
        print("i am child")

c=child()
c.child()
c.parent()