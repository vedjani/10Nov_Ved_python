# Write Python programs to demonstrate different types of inheritance (single, multiple,multilevel, etc.).
print("")
#single
class parent:
    def parent(self):
        print("this is parent class single")
class child(parent):
    def child(self):
        print("this is child class single")

print("-----single-----")
single=child()
single.parent()
single.child()
print("")

#multiple
class father:
    def father(self):
        print("father multiple inhe")
class mother:
    def mother(self):
        print("mother multiple inhe")
class son(father,mother):
    def son(self):
        print("son multiple inhe")
print("-----multiple-----")
multiple=son()
multiple.father()
multiple.mother()
multiple.son()
print("")

#multilevel
class grandparents():
    def grandparent(self):
        print("grandparent multilevel")
class parents(grandparents):
    def parents(self):
        print("parents multilevel")
class son(parents):
    def son(self):
        print("son multilevel")
print("-----multilevel-----")
multilevel=son()
multilevel.grandparent()
multilevel.parents()
multilevel.son()
