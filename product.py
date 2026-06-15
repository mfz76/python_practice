x = input("Enter the number you wish:").strip()
total = 1
for i in range(0,len(x)):
    total = total * int(x[i])
print(total)
 