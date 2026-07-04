# remove all zeros
while True:
    try:
        x = str(abs(int(input("Enter the number: "))))
        if len(x) == 1:
            print("Don't enter single digit number!")
            continue
        break
    except Exception:
        print("Something is wrong!")

found_zero = False

for ch in x:
    if ch == "0":
        found_zero = True
        break

if found_zero:
    new = x.replace("0", "")
    print(new)
else:
    print("There is no zero digit in the given number.")