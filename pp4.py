# print the multiplication table of a number from 1 to 10
while True:
    try:
        x = int(input("Enter the number:"))
        if x <= 0 :
            print("invalid input!")
            continue
        break
    except Exception:
        print("invalid input!")
for i in range(1,11):
    total = x * i 
    print(f"{x}*{i} = {total}")