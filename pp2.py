# find the factorial of a number using loop not recursion
while True:
    try:
        x = int(input("Enter the number:"))
        if x <= 0:
            print("Invalid Input!")
            continue
        break
    except Exception:
        print("Invalid Input!")

total  = 1
for i in range(1,x+1):
    total = total * i

print(total)
