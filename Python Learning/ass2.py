# problem number 02 


def find_even(a, b):
    evn_num = []
    add_num = []
    
    for i in range(a, b + 1):
        if i % 2 == 0:
            evn_num.append(i)
        
        elif i % 2 != 0:
            add_num.append(i)
    
    print("even numbers is : ", evn_num)
    print("odd numbers is : ", add_num)
    
    return evn_num, add_num

a = int(input("enter the first number : "))
b = int(input("enter the second number : "))
find_even(a, b)


# problem number 03 - print digits of a number seperately

   
def num_split(n):
    
    num_list = []
    for i in range(n):
        x1 = n % 10
        num_list.append(x1)
        n = n // 10
        if n == 0:
            break
        
    print(num_list[::-1])
    
n = int(input("enter the number : "))
num_split(n)


problem number 04 - count digit in a number 

x1 = int(input("enter the first number : "))

print(len(str(x1)))

# problem number 05 - sum of digits in a number

def sum_digit(n):

    sum = 0
    for i in str(n):
        sum += int(i)
        
    print("sum of digits is : ", sum)
    
n = int(input("enter the number : "))
sum_digit(n)


# problem number 06 - divisible by 3 and 5

def div_num(n):
    
    divisibleby_35 = []
    for i in range(n):
        if i % 3 == 0 and i % 5 == 0:
            divisibleby_35.append(i)
    
    print(divisibleby_35)     
    
n = int(input("enter the number : "))
div_num(n)

# problem number 07 - simple calculator making function

def calculator_sim(a, b , op):
    
    if op == '+':
        return a + b
    elif op == '-':
        return a-b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    else:
        return "invalid operator enter correct operator.."
    
a = int(input("enter the first number : "))
b = int(input("enter the second number : "))
op = input("enter the operator :")
    
print(calculator_sim(a, b, op))


# problem number 08 - prime number check function

n = int(input("Number enter karo: "))
count = 0

for i in range(1, n+1):
    if n % i == 0:
        count += 1

if count == 2:
    print("Prime number")
else:
    print("Not a prime number")

# problem number 10 - number guessing system 


def num_gess(n):
    
    b = 25
    if n == b :
        return "this is a correct number"
    elif n > b :
        return "this is to high..!"
    elif n < b :
        return "this is to low ..!"
    else:
        return "invalid inpur"
    
n = int(input("enter the number : "))
print(num_gess(n))
