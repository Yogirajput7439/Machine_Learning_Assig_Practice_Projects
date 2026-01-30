#problems number -01

def palindronee(name):
    
    namelist = name[::-1]
    
    if (name == namelist):
        print("this is a palindrone..")
        
    else:
        print("this is not an palindrone..")
    
    
name = input("enter your palindrone name = ")
palindronee(name)

# problem number -02

def averagee():
    
    # # listt = [5, 10, 15]
    listts = list(map(int, listt.split()))
    
    lenn = len(listts)
    countt = 0
    
    for i in listts:
        countt += i
        
    avg = (countt//lenn)
    print(avg)
    
listt = input("enter the number = ")
averagee()

# problem number -03 merge list 

def listmerge():
    
    mergelist = num1 + num2
    mergelist.sort()
    print(mergelist)

num1 = list(map(int, input("Enter numbers: ").split()))
num2 = list(map(int, input("Enter numbers: ").split()))
listmerge()

# problem number -04 make tuple odd even

def sorttuple():
    
    tupple1 = [12, 24, 23, 11, 36, 14, 44, 12, 32, 21, 45, 71]
    
    evnnum = []
    oddnum = []
    for i in tupple1:
        if (i % 2 == 0):
            evnnum.append(i)
            
        else:
            oddnum.append(i)
            
    evn = tuple(evnnum)
    odd = tuple(oddnum)
    print(f"this is a list od even numbers = {evn}")
    print(f"this is a list of odd number = {odd}")
    return evn, odd
    
sorttuple()

# problem number 05 the example using the functions -------

def keypress():
    
    college = {
        "sham" : 89,
        "ram" : 91,
        "jay" : 98,
        "viru" : 90    
    }
    
    if (ipt == "A" or "a"):
        newname = input("enter the name = ")
        newmark = int(input("enter the marks = "))
        college.update({f"{newname}" : newmark})
        print(college)
        
    elif (ipt == "B" or "b"):
        stdname = input("enter the name of that student you want to change thier mark : ")
        for key in college:
            
            if (key == stdname):
                newmark2 = int(input("enter the new marks of that student : "))
                college.update({f"{stdname}" : newmark2})
                print(college)
                break
            else:
                print("this is a wrong name...")
        
    elif (ipt == "C"):
        searchname = input("enter the student name = ")
        if searchname in college:
            print(college[searchname])
        else:
            print("you enterd the wrong name...")
                
    elif (ipt == "D"):
        print(college)
        
    else:
        print("you entered the wrong character...")
        
        
ipt = input("enter the A, B, C, D one of them : ")
keypress()

# problem number -06 - word li list ke name ke aage uska number character in word
def mapword():
    
    words =["apple","banana","kiwi","cherry","mango"]
    
    newword = {}
    
    for i in words:
        newword[i] = len(i)
    
    print(newword)
    
    
mapword()

# problem number 07 - take the input from the user of a string and pring the spaces in the string

def printspaces():
    
    # sentence = "ram and sham is a best duo in the whole class" -- example for making code
    count = 0
    thenum = sentence.count(" ")
        
    print(thenum)

sentence = input("enter the sentence that you like = ")
printspaces()

# problem number 08 - 
