#sum of all digits 

x =  input("Enter the number:").strip()

total = 0

for digit in x:
    total += int(digit)
    
print(total)