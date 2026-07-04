# check whether the number contains digit seven or not

while True:
    try:
        x = str(abs(int(input("Enter the number:"))))
        break
    except Exception:
        print("Somethings is wrong!")

noseven = True

for ch in x:
    if ch =="7":
        noseven = False

if noseven:
    print("not present")
else:
    print("its present")