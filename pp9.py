# check if the number is perfect number or not


while True:
    try:
        x = int(input("Enter the number:"))
        if x == 1:
            print("1 is not a perfect number.")
        if x <= 0:
            print("Invalid Input")
            continue
        break
    except ValueError:
        print("Invalid Input!")

if x != 1:
    total = 0
    for i in range(1,x):
        if x % i == 0:
            total = total + i
    
    if total == x:
        print(f"{x} is a perfect nubmer.")
    else:
        print(f"{x} is not a perfect number.")