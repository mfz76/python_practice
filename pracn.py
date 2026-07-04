# reverse the number


while True:
    try:
         x = str(abs(int(input("Enter the number:"))))
         if len(x) == 1:
            print("dont enter single digit number, try again!")
         break
    except Exception:
        print("Enter the num")


rev = ""

for ch in reversed(x):
    rev = rev + ch

print(rev)

