# find the smallest digit of the number
while True: 
    try:
        x = str(abs(int(input("Enter the number please:"))))
        break
    except ValueError:
        print("invalid input")

smallest = 9

for ch in x:
    if   "0"<=   ch   <= "9":
        digit = int(ch)
        if digit < smallest:
            smallest = digit

print(smallest)
