# check if the number is power of 2 or not using bit-wise operators.all
while True:
    try:
        x = int(input("Enter the number:"))
        break
    except ValueError:
        print("Invalid input!")


if x > 0 and (x & (x-1)) == 0:
    print("its power of 2.")
else:
    print("its not power of 2.")