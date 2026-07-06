#reverse a number without converting it into string

while True:
    try:
        n = int(input("Enter the number:"))
        if len(str(n)) == 1 or n < 0 :
            print("Invalid Input!")
            continue
        break
    except Exception:
        print("invalid input!")

rev = 0

while n > 0:
    digit = n % 10 
    rev = rev * 10 + digit
    n = n  // 10

print(rev)

    