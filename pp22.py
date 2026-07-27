# to  check whether the number is a happy number or not

while True:
    try:
        x = abs(int(input("Enter the number:")))
        if x == 0:
            print("invalid input!")
            continue
        break
    except ValueError:
        print("Invalid input!")



seen = set()



while x != 1 and x not in seen:
    seen.add(x)


    total = 0
    for digits in str(x):
        total +=  int(digits)**2

    x = total



if x == 1:
    print("it's a happy number.")
else:
    print("its not a happy number.")
    




