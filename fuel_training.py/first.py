# class Dog:
#     def bark(self):
#         print("Woof!")
# d = Dog()  
# d.bark() 



# class Student:
#     college = "ABC College"   

#     def __init__(self, name):
#         self.name = name      

# s1 = Student("Abhishek")

# print(s1.name)
# print(Student.college)

# method

# def new(name):
#     print(f"this is {name}")
# new("abhi")

# inheritance

# class person():
#     def new(self,name,age):
#         self.name=name
#         self.age=age
    

    
# s1=person()
# s1.new("abhishek",18)
# print(s1.name,s1.age)


class car:
    def start(self):
        print("car is start")
    def stop(self):
        print("clar is stop")
car=car()
car.start()
car.stop()


arr=[1,2,3,4,5,6,7,8,9]
k=3
start=0
end=len(arr)
for i in range(len(arr)):
    mid=start + end //2
    if mid[i]==k:
        print("elemnent in mid")
    elif mid[i] > k:
        end = mid -1
    else:
        start = mid +1
else:
    print(-1)
