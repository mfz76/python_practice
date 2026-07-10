# check if a digit is a number is an armstrong number or not

while True:
        x = input("Enter the number:").strip()
        if x == "0":
            print("invalid input!")
            continue
        if not x.isdigit():
            print("invalid input!")
            continue
        break


length = len(x)
total = 0

for ch in x:
    if  "0"<=  ch <="9":
       digit =  int(ch)
       total = total + digit ** length

if total == int(x):
    print(f"{x} is a armstrong number.")
else:
    print(f"{x} is not a armstrong number.")



