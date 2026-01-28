# Abstraction

"""hiding the implementation detail of class and show only essential featue"""
'''
class car:

    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def start(self):
        self.clutch=True
        self.acc=True
        return "starting......."
    
    def stop(self):
        self.clutch=True
        self.acc=True
        return "Stop..........."
maruti=car()
print(maruti.start())
print(maruti.stop())
'''

"........................................................................................................................."

# Encapsulation
"""wrapping the data and function into singe unit"""
"""
class Account:
    def __init__(self,bal,acc_no):
        self.bal=bal
        self.acc_no=acc_no

    def debit(self,amount):
        self.bal -= amount
        print(f"{amount} debited")

    def credit(self,amount):
        self.bal += amount
        print(f"{amount} debited")

    def show(self):
        print(f"{self.bal} your amount")

acc1=Account(100000,1234567890)
acc1.debit(50000)
acc1.credit(100000)
acc1.show()

"""
# 

'......................................................................................................................'

# class bank:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no=acc_no
#         self.__acc_pass=acc_pass
# acc1=bank("1234","abc")
# print(acc1.acc_no)
# print(acc1.__acc_pass)

# class person:
#     def __init__(self):
#         print("HEllO WORLD")

#     def __hello(self):
#         print("hello MF")
#     def welcome(self):
#         self.__hello()
# s1=person()
# s1.__hello()
# s1.welcome()

"..........................................................................................................."

# inheritance

"""class car:
    @staticmethod
    def start():
        print("car started....")

    @staticmethod
    def stop():
        print("car stop....")
class toyota(car):
    def __init__(self,name,color):
        self.color=color
        self.name=name
car1=toyota("fortuner","black")
print(car1.name)
print(car1.color)
car1.start()"""

class car:
    @staticmethod
    def start():
        print("car started....")

    @staticmethod
    def stop():
        print("car stop....")
class toyota(car):
    def __init__(self,brand):
        self.brand=brand

class fortuner(toyota):
    def __init__(self, type):
        self.type=type

car1=fortuner("disel")
car1.start()

