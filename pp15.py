# convert a decimal number to a binary without using bin 

while True:
    try:
        x = int(input("Enter the number:"))
        if x == 0:
            print("0")
        break
    except ValueError:
        print("invalid input!")

if x != 0:
    neg = False
    if x < 0:
        neg = True
        x = abs(x)




    remain = ""

    while x > 0:
        remain  +=  str(x%2)
        x //= 2

    remain = "".join(reversed(remain))


    if neg:
        print("-" + remain)
    else:
        print(remain)

