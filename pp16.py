#check if a number is a power of 2 without using log 


while True:
    try:
        x = int(input("Enter the number:"))
        if x == 0:
            print("Its not the power of 2.")
            continue
        elif x <= 0:
            print("Invalid input!")
            continue
        break
    except ValueError :
        print("Invalid input!")


while x % 2 == 0:
    x //= 2

if x == 1:
    print("it is the power of 2.")
else:
    print("its not the power of 2.")