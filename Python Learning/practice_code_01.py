class Students:
    college_name = "abc college sambajinagar"
    name = "yogi_bhai"
    
    def __init__(self):
        print("Green color is a beautifull color..")
        
    
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
        print("this is the all information of the students...")
        
s1 = Students("yogesh", 22, 89)
print(s1.name)
print(s1.age)
print(s1.marks)


# ---------  Questions number 1 

class Student:
    
    def __init__(self, name, sub1, sub2, sub3):
        self.name = name
        self.sub1 = sub1 
        self.sub2 = sub2
        self.sub3 = sub3
        
    def avr(self):
        print(f"The name of the studet is {self.name}")
        print(f"the marks of the student is {self.sub1}, {self.sub2}, {self.sub3}")
        
        avg1 = (self.sub1 + self.sub2 + self.sub3) / 3
        print("the average of the marks is :", avg1)
        
s1 = Student("yogesh", 22, 23, 24)
s1.avr()

x = ("a", "23", "re3")
print(str(x))
print(type(x))

name = "i love money"

print(name[:3])
print(name[3:6])
print(name[6:])     
print(name[-3:])
print(name[-6:-3])
print(name[-9:-6])

newname = name.join(" and ")
print(newname)
