# check if the number is power of 2 or not using log feature
import math

while True:
    try:
        x = int(input("Enter the number:"))
        if x<0:
            print("Invalid input!")
            continue
        elif x == 0:
            print("False")
            continue
        break
    except ValueError:
        print("Invalid Input!")

new = math.log(x,2)

if (new).is_integer():
    print("True")
else:
    print("False")




