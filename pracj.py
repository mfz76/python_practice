#print the second smallest digit of the number


x = str(abs(int(input("Enter the number:"))))

smallest = 9
secondsmallest = 10

for ch in x:
    if "0"<= ch <="9":
        digit = int(ch)
        if digit < smallest:
            smallest = digit

for ch in x:
    if "0"<= ch <="9":
        digit = int(ch)
        if digit > smallest and digit < secondsmallest:
            secondsmallest = digit

print(secondsmallest)
