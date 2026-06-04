# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 13:38:45 2026

@author: MOHAMMAD FARAZ
"""
# first 

'''x = input("What is your name?\n")

print(f"Hello, {x} very nice to meet you!")'''


#second 

'''x = int(input("PLZ, Enter your age:").strip())

age = x + 10

print(f"10 years later your age will be {age}.")'''


# third 

'''x = int(input("Enter the  number a you wanna subtract from:\n"))
y = int(input("Enter the number b you wanna  subtract:\n"))


sub = x - y


print(f"Hence, the subtract is {sub}.")'''

# four

'''
x = int(input("Enter the number x on which you wanna perform operations on: ").strip())
y = int(input("Enter the number y on which you wanna perform operations on: ").strip())

char = input(
    "Enter the operation you wanna have:\n1. +\n2. -\n3. *\n4. /\n"
).strip()

if char == "+":
    print(x + y)

elif char == "-":
    ans = input("You wanna subtract from x or y? ").strip().lower()

    if ans == "x":
        print(x - y)
    elif ans == "y":
        print(y - x)
    else:
        print("Invalid choice. Enter either x or y.")

elif char == "*":
    print(x * y)

elif char == "/":
    ans = input("What is the dividend? (x or y): ").strip().lower()

    if ans == "x":
        if y == 0:
            print("Division by zero is not possible.")
        else:
            print(x / y)

    elif ans == "y":
        if x == 0:
            print("Division by zero is not possible.")
        else:
            print(y / x)

    else:
        print("Invalid choice. Enter either x or y.")

else:
    print("Invalid operator.")'''

#five 

'''
x = int(input("Enter the number to check?"))

if x%2 == 0:
    print("Its an even number.\n")
    
else :
    print("its an odd.\n")
'''


#six
'''
x = int(input("Enter the number to check:\n"))

if x == 0:
    print("its a zero")
    
elif x > 0:
    print("its positive")
    
elif x < 0:
    print("its negative")
'''

#seven 
'''
for i in range(1,21):
    print(i)
    '''
    
#eight
'''
for i in range(1,51):
    if i%2 == 0:
        print(i)
        '''
'''   
#nine

x = int(input("Enter the number till which you wanna sum:\n"))


sums = 0
for i in range(x+1):
    sums = sums + i
print(sums)       
'''

#ten

'''

x = int(input("Enter the number you wanna have table of:").strip())
for i in range(1,11):
       pro = 0
       pro = x*i
       print(f"{x}*{i}={pro}")


'''

# eleven

'''
x = int(input("Enter the first number to check for:"))
y = int(input("Enter the second number to check for:"))
z = int(input("Enter the third number to check for:"))

if x>y and x>z:
    print("x is the greatest")
elif y>x and y>z:
    print("y is the greatest")

else:
    print("z is the greatest of all")
    
'''


#twelve

'''
password = "123python"

x = input("Enter the password, whatever you think it is:")

if x == password :
    print("Access Granted")
    
else:
    print("Access Denied")

'''

#thirteen

'''


x = int(input("Enter the number:\n").strip())
print(len(str(abs(x))))

'''

#fourteen 
'''
x = input("Enter the number:").strip()

reverse = x[::-1]

print(reverse)
    
    
'''
















































