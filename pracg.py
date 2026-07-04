#find the largest digit of the given number

x = str(abs(int(input("Enter the number:"))))

largest = 0


for ch in x:
    if   "0"<=   ch  <= "9" :
        digit = int(ch)
        if digit > largest:
            largest = digit
                
print(largest)
