#YESTERDA'S QUESTIONS FOR PRACTICE


#give the largest digit of the number
'''
x = str(abs(int(input("Enter the number:"))))


largest = 0

for ch in x:
    if   "0"<=   ch <="9":
        digit = int(ch)
        if digit > largest:
            largest = digit

print(largest)'''


#give the smallest digit of the number
'''
while True:
    try:
        x = str(abs(int(input("Enter the number:"))))
        break
    except Exception:
        print("Something is wrong!")
    
smallest = 9

for ch in x:
    if "0" <=  ch  <=  "9":
        digit = int(ch)
        if digit < smallest:
            smallest = digit


print(smallest)'''


# give the second largest digit of the number

'''
while True:
    try:
        x = str(abs(int(input("Enter the number: "))))
        if len(x) == 1:
            print("Invalid input: need at least a 2-digit number.")
            continue
        break
    except Exception:
        print("Try again! Something is wrong...")

largest = -1
secondlargest = -1

for ch in x:
    digit = int(ch)
    if digit > largest:
        largest = digit

print("The largest digit is", largest)

for ch in x:
    digit = int(ch)
    if secondlargest < digit < largest:
        secondlargest = digit

if secondlargest == -1:
    print("No second largest distinct digit found")
else:
    print("The second largest digit is", secondlargest) '''


#find the second smallest digit of the number


while True:
    try:
        x = str(abs(int(input("Enter the number:"))))
        if len(x) == 1:
            print("Dont enter single digit number!")
            continue
        break
    except Exception:
        print("Something is wrong!")


smallest = 9
secondsmallest = 10

for ch in x:
    if "0"  <= ch <= "9":
        digit = int(ch)
        if digit < smallest:
            smallest = digit

print("The Smallest digit is", smallest)

for ch in x:
    if "0"  <= ch <= "9":
        digit = int(ch)
        if smallest < digit < secondsmallest:
            secondsmallest = digit

if secondsmallest == 10:
    print("there is no second smallest digit in the nubmer.")
else:
    print("the second smallest digit is",secondsmallest)



