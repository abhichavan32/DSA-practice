class stud:
    def __init__(self,name,roll_no) -> None:
        self.name=name
        self.roll_no=roll_no
    def speak(self): # inside the constructor 
        print("hello my name is ", self.name)


stud1=stud("abhi","12")

print(stud1.name)
print(stud1.roll_no)
stud1.speak()


class Dog:
    def bark(self):
        print("Woof!")

d = Dog()   # create object 
d.bark()    # call method output is woof!
