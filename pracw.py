#remove all zeroes

while True:
    try:
        x = str(abs(int(input("Enter the number:"))))
        if x == "0":
            print("Invalid Input!")
            continue
        break
    except Exception:
        print("Something is wrong!")

nozero = True

for  ch in x:
    if  ch == "0":
        nozero = False
        y = x.replace("0","",len(x))
        break
   
        

if nozero:
    print("there is not any zero.")

else:
    print(f"there is zero digit but the new number is {y}")
