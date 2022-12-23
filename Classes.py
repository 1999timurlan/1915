#class Human:
#    height=170
#class Student(Human):
#   pass
#class Worker(Human):
#   pass
#nick=Student()
#ann=Worker()
#print(nick.height)
#print(ann.height)

class Rec:
    def area(self,a,b):
        return a*b
rect=Rec()
print(rect.area(4,5))

class Day():
    year=2010
    month=6
    day=26
Day1=Day
Month=Day
Year=Day
print()
print(Day1.day)
print(Month.month)
print(Year.year)

class Hello:
    def __init__(self):
        print("Hello")
class Hello_world(Hello):
    def __init__(self):
        super().__init__()
        print("World")

hello_world=Hello_world()

class Class1:
    var=20
    def __init__(self):
        self.var=10
class Class2(Class1):
    def __init__(self):
        print(self.var)
        super().__init__()
        print(self.var)
        print(super().var)
clas=Class2()

class c1:
    pass
class c2:
    pass
class CA(c1,c2):
    pass

class Computer:
    def __init__(self):
        super().__init__()
        self.memory=120
class Display:
    def __init__(self):
        super().__init__()
        self.resolution="4K"
class SmartPhone(Display,Computer):
    def print_info(self):
        print(self.resolution)
        print(self.memory)

iphone=SmartPhone()
iphone.print_info()
print()
print()
print()
print()
print()
print()




class Rec:
    def area(self,a):
        return a*a
rect=Rec()
print(rect.area(5))


