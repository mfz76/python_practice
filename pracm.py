#count digits smaller than 5

while True:
    try:
        x = str(abs(int(input("Enter the number:"))))
        if len(x) == 1:
            print("please don't enter single digit nubmers.")
            continue
        break
    except Exception:
        print("Something is wrong, try again!")

count = 0

for ch in x:
    if   "0" <= ch <= "9":
        digit = int(ch)
        if digit < 5:
            count += 1

print(f"hence, {count} smaller than 5.")