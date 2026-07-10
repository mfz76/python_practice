# greates common divisor of two number without using math.gcd() or HCF

while True:
    try:
        x,y = map(int, input("Enter the number:").split(","))
        if x <= 0 or y <= 0:
            print("invalid input")
            continue
        break
    except ValueError:
        print("Invalid Input!")

if x >= y:
    for i in range(y,0,-1):
        if x % i == 0 and y % i == 0:
            print(f"the gcd is {i}")
            break
elif y > x:
    for i in range(x,0,-1):
        if x % i == 0 and y % i == 0:
            print(f"the gcd is {i}")
            break

'''
small = min(x, y)

for i in range(small, 0, -1):
    if x % i == 0 and y % i == 0:
        print(f"The GCD is {i}")
        break'''



