# 12) Write a Python program to demonstrate the use of local and global variables in a class.

# Global variable
college = "Tops Tech"

class Student:

    def show_details(self):
        # Local variable
        name = "ved"
        roll_no = 2311

        print("Student Name:", name)
        print("Roll No:", roll_no)
        print("College:", college)  

s1 = Student()
s1.show_details()

    