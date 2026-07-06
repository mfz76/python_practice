#sum of a digit of given number

while True:
    try:
        x = str(abs(int(input("Enter the number:"))))
        if len(x) == 1:
            print("dont enter single digit numbers")
            continue
        break
    except Exception:
        print("there must be something wrong!")


digit = 0


for ch in x:
    digit = digit + int(ch)

print("sum is",digit)