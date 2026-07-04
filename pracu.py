#check whether there is a repeated digit or not 
while True:
    try:
        x = str(abs(int(input("Enter the number:"))))
        if len(x) == 1:
            print("no single sigit numbers are allowed")
            continue
        break
    except Exception:
        print("There is some issue in your input!")

norep = True

for ch in x:
    for ch2 in str(x.replace(ch,"",1)):
        if ch == ch2:
            norep = False
            break
    if not norep:
        break

if norep:
    print("not any repeated digit is present")
else:
    print("repeated digit is present")
    


