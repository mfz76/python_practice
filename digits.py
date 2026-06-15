# to find the largest digit out all digits in number

x = input("Enter the number: ").strip()

largest = int(x[0])

for i in range(len(x)):
   if int(x[i]) > int(x[0]):
       largest = x[i]
       
print(largest)