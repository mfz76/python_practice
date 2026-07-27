#  find the sum of first n fibonacci numbers 

from sympy import fibonacci

while True:
    try:
        x = int(input("Enter the number:"))
        if x < 0:
            print("Invalid input!")
        break
    except ValueError:
        print("Invalid input!")

sum = 0

for i in range(x):
    sum = sum + fibonacci(i)

print(sum)
  

