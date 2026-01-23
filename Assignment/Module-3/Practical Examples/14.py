# 14) Write a Python program to show multilevel inheritance.
class Grandparent:
    def Grandparents(self):
        print("hello i am grandparents")
class Parent(Grandparent):
    def parents(self):
        print("hello i am parents")
class Child(Parent):
    def child(self):
        print("hello i am child")

ch=Child()
ch.Grandparents()
ch.parents()
ch.child()