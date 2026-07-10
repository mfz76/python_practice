# given a number find all its factors

while True:
    try:
        x = int(input("Enter the number:"))
        if x <= 0:
            print("Invalid Input!")
            continue
        break
    except ValueError:
        print("Invalid Input !")



for i in range(1,x+1):
    if x % i == 0:
        print(f"{i} is a factor.")