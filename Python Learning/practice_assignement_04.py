# How was a class method --------
class student:
    
    subject = "math"
    college = "ABC college"
    year = "4th year"

std1 = student()
std2 = student()

print(std1.college, std1.subject, std1.year)
print(std2.year, std2.college, std2.subject)

# Using self in class ----------
class student:
    
    def __init__(self):
        print("constructer was called")
        
std1 = student()

class student:
    
    def __init__(self, name):
        self.name = name
        print(f"{self.name} is a good student")
        
std1 = student("ram")     
print(std1.name)  

# Learning the class using self and geting the new parameter in class --------

class student:
    college = "ABC College"
    
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        
        
std1 = student("sham", 9.0)
std2 = student("ram", 8.4)

print(f"{std1.name} have a {std1.gpa} gpa and their college is {std1.college}")
print(f"{std2.name} have a {std2.gpa} gpa and their college is {std2.college}")

# how to use self and otheer parameter in other function ----------

class laptop:
    
    storage_type = "ssd"
    
    def __init__(self, RAM):
        self.RAM = RAM
        
    def get_info(self):
        print(f"The laptop have {self.RAM} and {self.storage_type} type storage")
        
    @classmethod
    def get_storage_type(cls):
        print(f"storage type is {cls.storage_type}")
        
    @staticmethod
    def calc_discount(price, discount):
        final_price = price - ( price * discount / 100)
        print(f"The final price is {final_price}") 
        
l1 = laptop("16GB")

l1.get_info()
l1.get_storage_type()
l1.calc_discount(40_000, 25)

# The new example using private and protected method ------------

class bankaccount:
    
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        
    def get_balance(self):
        return self.__balance
    
    def set_balance(self, new_balance):
        self.__balance = new_balance
        
acc1 = bankaccount("Rahul", 50000)
print(acc1.get_balance())
acc1.set_balance(60000)
print(acc1.get_balance())

# using Inheritance in the other class ---------

class Employee:
    start_time = "9AM"
    end_time = "6PM"
    
class Teacher(Employee):
        def __init__(self, subject):
            self.subject = subject
            
t1 = Teacher("data science")
print(t1.subject, t1.start_time, t1.end_time)

# Another example using Inheritance in oops ------------

class Teacher:
    def __init__(self, salary):
        self.salary = salary
        
class Student():
    def __init__(self, gpa):
        self.gpa = gpa
        
class TA(Teacher, Student):
    def __init__(self, name, salary , gpa):
        super().__init__(salary)
        Student.__init__(self, gpa)
        self.name = name
        
ta = TA("rahul sharma", 40000, 8.5)
print(ta.salary, ta.name, ta.gpa)

# Import abd from abc and geting example -------------

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound():
        pass
    
class Lion(Animal):
    def make_sound(self):
        print("Roar...")
        
class Cow(Animal):
    def make_sound(self):
        print("Moo...")
        
lion = Lion()
lion.make_sound()
cow = Cow()
cow.make_sound()

