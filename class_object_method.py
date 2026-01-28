"""
# class  it is bluprint of object

class student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def __str__(self):
        return f"name:{self.name} , Roll:{self.roll}"
    
# object it is instance of that class
s1=student("Abhishek",1234)
print(s1)
"""

# class example:
#     def __init__(self):
#         self.name="abhishek"
#         self.roll=1234
# s1=example()
# print(s1.name)


"""
class example:
    name="abhishek"
    roll=1234
s1=example()
print(s1.name)

"""

# class student:
#     def stud(self,name,roll):
#         self.name=name
#         self.roll=roll
#     def data(self):
#         return f"student name {self.name},and student roll {self.roll}"
# name=input("enter the name: ")
# roll=int(input("Enter the roll: "))
# s1=student()
# s1.stud(name,roll)
# print(s1.data())


"""
class student:
    class school:
        def prev(self,school_name,location):
            self.school_name=school_name
            self.location=location
        def show(self):
            return self.school_name,self.location
school_name=input("school_name: ")
location=input("school location: ")

s1_school=student.school()
s1_school.prev(school_name,location)
print(s1_school.show())
"""

# class student:
#     class school:
#         def prev(self,school_name,location):
#             self.school_name=school_name
#             self.location=location
#         def show(self):
#             return self.school_name,self.location
            
#     class detail:
#         def stud_data(self,name,roll):
#             self.name=name
#             self.roll=roll
#         def show(self):
#             return self.name,self.roll
        
# no_stud=int(input("Enter the no of student: "))

# for i in range(no_stud):

#     print(f".......stud{i+1}")
#     school_name=input("school_name: ")
#     location=input("school location: ")
#     name=input("enter your name: ")
#     roll=int(input("enter your roll_no: "))

#     detail=student.detail()
#     detail.stud_data(name,roll)
#     print(detail.show())
#     school=student.school()
#     school.prev(school_name,location)
#     print(school.show())

"..............................................................................xoxoxox..........................................."
# method in this start and stop are methods

# class car:
#     def start(self):
#         return "car is start position"
#     def stop(self):
#         return "car is now stopped"
# c1=car()
# print(c1.start())
# print(c1.stop())

".............................................................................xoxoxoxox.........................................."
"""
class student:
    def data(self,name,mark1,mark2,mark3):
        self.name=name
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3
    def average(self):
        avg=self.mark1 + self.mark2 + self.mark3 // 3
        return f"{self.name} your avarage mark is {avg}"

name=input("Enter your name: ")
science=int(input("Enter your Scienece mark : "))
physics=int(input("Enter your Physics mark : "))
math=int(input("Enter your Math mark : "))

result=student()
result.data(name,science,physics,math)
print(result.average())

"""
"..................................................................................................................................."

# static mathod that not use self parameter

class student:
    @staticmethod #decorator
    def college():
        return "THIS IS YOUR COLLEGE"
wel=student()
print(wel.college())




