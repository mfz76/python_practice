# find the lcm of two numbers

a,b = map(int, input("Enter the number:").split(","))
i = 2
new  = 1

while a > 1 or b > 1:
    if a % i == 0 or b % i == 0:
        new = new * i

        if a % i == 0:
            a //= i

        if b % i == 0:
            b //= i

        
    else:
        i += 1

print(new)