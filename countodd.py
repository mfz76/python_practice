# to count the odd number in a given number


x = str(abs(int(input("Enter the number:").strip())))

count = 0

for value in x:
    if int(value) % 2 != 0:
     count += 1
     
print(count)