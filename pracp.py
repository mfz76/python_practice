#check whether a number contains digit 0

while True:
    try:
        x  =  str(abs(int(input("Enter the  number:"))))
        if len(x) == 1:
            print("dont enter single digit numbers!")
            continue
        break
    except Exception:
        print("Something is wrong!")

isnotpresent = True

for ch in x:
    if ch == "0":
        isnotpresent = False

if isnotpresent:
    print("the number does not contain digit zero.")
else:
    print("it does contain.")

