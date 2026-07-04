# count the digit greater than 5

while True:
    try:
        x = str(abs(int(input("Enter the number:"))))
        if len(x) == 1:
            print("Dont enter single digit numbers!")
            continue
        break
    except Exception:
        print("Something is wront!")



count = 0

for ch in x:
    if  "0"<=   ch  <= "9":
        digit = int(ch)
        if digit > 5:
            count += 1 

print(f"hernce, there are {count} digits greater than 5.")